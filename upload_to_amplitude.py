import json
import time
import certifi
import urllib
import urllib3
import logging
import os

from concurrent import futures
from urllib3.exceptions import HTTPError
from urllib.parse import urlencode
from zipfile import ZipFile
from concurrent.futures import as_completed


API_KEY = 'KEY_MY_PROJECT'
ENDPOINT = 'https://api2.amplitude.com/batch'

class Executor(futures.ThreadPoolExecutor):

	def __init__(self, max_workers):
		super(Executor, self).__init__(max_workers)
		self.track_futures = False
		self.futures = []

	def submit(self, fn, *args, **kwargs):
		def wrapped_fn(args, kwargs):
			return fn(*args, **kwargs)
		future = super(Executor, self).submit(wrapped_fn, args, kwargs)
		if self.track_futures:
			self.futures.append(future)
		return future

	def results(self):
		if not self.track_futures:
			raise Exception('Cannot get results from executor without future tracking')
		return (future.result() for future in as_completed(self.futures))

	def __enter__(self):
		self.track_futures = True
		return super(Executor, self).__enter__()

	def __exit__(self, exc_type, exc_val, exc_tb):
		try:
			for future in as_completed(self.futures):
				future.result()
			self.futures = []
			self.shutdown(wait=False)
			return False
		finally:
			super(Executor, self).__exit__(exc_type, exc_val, exc_tb)


def run_with_retry(f, tries, failure_callback=None):
	while True:
		try:
			return f()
		except Exception as e:
			print(e)
			tries -= 1
			if tries <= 0:
				logging.info('[%s] Failed to run %s Encountered %s (0 tries left, giving up)', os.getpid(), f, e.__class__.__name__)
				break
			else:
				if failure_callback:
					failure_callback()
				logging.info(
					'[%s] Raised %s, retrying (%s tries left)',
					os.getpid(), e.__class__.__name__, tries)


def send_req(json_events):
	data = {'api_key': API_KEY, 'events': json_events}

	def do_send():
		http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
		response = http.request('POST', ENDPOINT, body=json.dumps(data).encode('utf-8'))
		response.read()
		response.close()
		if response.status == 200:
			print("You're lucky")
		if response.status != 200:
			raise Exception('Bad response: ' + str(response.status) + ', body: ' + str(response.data) )
			return
	run_with_retry(do_send, tries=10, failure_callback=lambda: time.sleep(10))

def upload(events):
	start = time.time()
	with Executor(max_workers=64) as executor:
		for i in range(0, len(events), 10):
			executor.submit(send_req, events[i:i + 10])
	diff = time.time() - start
	logging.info('uploading %s events took %s', len(events), diff)

def main():
	import sys

	rootLogger = logging.getLogger()
	rootLogger.setLevel(logging.DEBUG)

	ch = logging.StreamHandler(sys.stdout)
	ch.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	rootLogger.addHandler(ch)

	filename = sys.argv[1]
	start = int(sys.argv[2])

	rownum = 0
	cur_events = []
	zf = ZipFile(filename, 'r', allowZip64=True)
	with zf.open(zf.infolist()[0]) as f:
		for line in f:
			rownum += 1
			if rownum <= start:
				continue

			event = json.loads(line.strip())
			
			
			if (
				'event_type' not in event or
					('user_id' not in event and 'device_id' not in event)
			):
				continue
			cur_events.append(event)
			if len(cur_events) >= 1000:
				logging.info('uploading %s events, row %s', len(cur_events), rownum)
				upload(cur_events)
				cur_events = []
		if cur_events:
			logging.info('uploading %s events, row %s', len(cur_events), rownum)
			upload(cur_events)


if __name__ == '__main__':
	main()
	
