import generate_users
import functions_of_events
import datetime, time
		 

insert_id = generate_users.load_from_file('insert_id.txt')
session_id = generate_users.load_from_file('session_id.txt')
device_id = generate_users.load_from_file('device_id.txt')	
users_info = generate_users.generate_user_properties(10)

def generate_events(count_events):
	events = []
	unique_user_data = {}
	for i in range(count_events):
		new_event = {}
		platform = random.choice(list(platform_array.items()))
		new_event["platform"] = platform[0]
		new_event["os_name"] = random.choice(platform[1])
		new_event["device_id"] = random.choice(device_id)
		new_event["session_id"] = random.choice(session_id)
		new_event["insert_id"] = random.choice(insert_id)

		user = random.choice(users_info)
		user_properties = user['user_properties']
		new_event["user_id"] = user['user_id']

		day = random.randint(1,31)
		if user["last_time"] == 0:
			t = datetime.datetime(2021, 5, day, 0, 0)
			user["last_time"] = int(t.timestamp())
			new_event["time"] = user["last_time"]
		else:
			new_event["time"] = int(user['last_time']) + random.randint(500,100000)

		unique_user_data[user["user_id"]] = user

		#the user still hasn't created an account
		if user_properties['status'] == 'null':
			unique_user_data[user["user_id"]] = functions_of_events.generate_anonymous_user(user)

		#the user didn't have a trial lesson
		elif user_properties['status'] == 'just registered':
			unique_user_data[user["user_id"]] = functions_of_events.choose_actions_just_registered(user)
				
		#the user had a trial lesson, we are waiting for the user to pay for the lessons
		elif user_properties['status'] == 'had a trial lesson':
			unique_user_data[user["user_id"]] = functions_of_events.choose_actions_had_trial_lesson(user)

		#the user is studying in our school
		elif user_properties['status'] == 'studying':
			unique_user_data[user["user_id"]] = functions_of_events.choose_actions_studying(user)
		
	return events
