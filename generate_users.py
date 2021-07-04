import json
import random
import info

def generate_user_properties(count):
	users_array = []
	user_id_array = load_from_file('user_id.txt')
	for i in range(count):
		user_properties = {}
		user_properties["age"] = random.randint(18,50)
		user_properties["gender"] = random.choice(info.gender)
		user_properties["type_of_employment"] = random.choice(info.employment_array)
		user_properties["status"] = random.choice(info.status_array)
		user_properties["language"] = random.choice(info.language_array)

		user_properties["lessons_count"] = 0
		user_properties["directions"] = []
		user_properties["directions_finished"] = []
		user_properties["user_id"] = user_id_array[i]
		user_properties["last_time"] = 0

		place_info = random.choice(list(info.country_array.items()))
		user_properties["country"] = place_info[0]
		user_properties["city"] = random.choice(place_info[1])

		if user_properties["status"] == "had a trial lesson":
			user_properties["lessons_count"] = 1
			user_properties["directions"].append(random.choice(info.directions_array))

		elif user_properties["status"] == "studying":
			user_properties["lessons_count"] = random.randint(1,200)
			count_directions = random.randint(1,3)

			for i in range(count_directions):
				random_direction = random.choice(info.directions_array)
				if random_direction not in user_properties["directions"]:
					user_properties["directions"].append(random_direction)
				if user_properties["lessons_count"] > 90:
					user_properties["directions_finished"].append(user_properties["directions"][0])

		users_array.append(user_properties)

	return users_array
		

def write_to_json_file(array, name_file):
	with open('data.json', 'w', encoding='utf-8') as f:
		for i in array:
			json.dump(i, f)
			f.write('\n')


def load_from_file(name):
	array = []
	f = open(name, 'r')
	for line in f:
		array.append(line.rstrip())
	f.close()
	return array



	





