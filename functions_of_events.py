
import datetime, time

################ FUNCTIONS OF EVENTS ###################
def event_click_create_account(new_event, events, user):
	event_name = 'click_create_account'
	new_event["event_type"] = event_name
	category_name = 'Register'
	new_event["category_name"] = category_name
	new_event["event_properties"] = {}
	new_event["user_properties"] = user["user_properties"]
	events.append(new_event.copy())

def event_enter_info(new_event, events):
	event_name = 'enter_info'
	new_event["event_type"] = event_name
	events.append(new_event.copy())

def event_account_created(new_event, events):
	event_name = 'account_created'
	new_event["event_type"] = event_name
	events.append(new_event.copy())

def event_account_verified(new_event, events):
	event_name = 'account_verified'
	new_event["event_type"] = event_name
	events.append(new_event.copy())

def event_login(new_event, events, user):
	event_name = 'login'
	new_event["event_type"] = event_name
	events.append(new_event.copy())
	user['user_id'] = future_id
	user_properties['status'] == 'just registered'
	return user

def event_click_signup_lesson(new_event, events, user):
	event_name = 'click_signup_lesson'
	new_event["event_type"] = event_name
	category_name = 'Signup for a lesson'
	new_event["category_name"] = category_name
	new_event["event_properties"] = {}
	new_event["user_properties"] = user["user_properties"]
	events.append(new_event.copy())

def event_choose_direction(new_event, events, user):
	event_name = 'choose_direction'
	new_event["event_type"] = event_name
	new_event["insert_id"] = random.choice(insert_id)
	event_properties = {}
	event_properties["direction"] = random.choice(directions_array)
	user['user_properties']['directions'].append(event_properties["direction"])
	new_event["event_properties"] = event_properties
	new_event["time"] = str(int(new_event["time"]) + 5) 
	user["last_time"] = new_event["time"]
	new_event["event_id "] +=1
	events.append(new_event.copy())

def event_choose_time(new_event, events, user):
	event_name = 'choose_time'
	new_event["event_type"] = event_name
	new_event["insert_id"] = random.choice(insert_id)
	event_properties = {}
	event_properties["interval"] = random.choice(interval_array)
	new_event["event_properties"] = event_properties
	new_event["time"] = str(int(new_event["time"]) + 10)
	user["last_time"] = new_event["time"]
	new_event["event_id "] +=1
	events.append(new_event.copy())

def event_record_confirmation(new_event, events, user):
	event_name = 'record_confirmation'
	new_event["event_type"] = event_name
	new_event["insert_id"] = random.choice(insert_id) 
	new_event["event_properties"] = {}
	new_event["time"] = str(int(new_event["time"]) + 15)
	user["last_time"] = new_event["time"]
	new_event["event_id "] +=1
	events.append(new_event.copy())
	return user
	
def event_click_pay_lessons(new_event, events, user):
	event_name = 'click_pay_lessons'
	new_event["event_type"] = event_name
	category_name = 'Payment for lessons'
	new_event["category_name"] = category_name
	new_event["event_properties"] = {}
	new_event["user_properties"] = user["user_properties"]
	new_event["insert_id"] = random.choice(insert_id)
	new_event["event_id "] +=1
	events.append(new_event.copy())

def event_choose_count_lessons(new_event, events, user):
	event_name = 'choose_count_lessons'
	new_event["event_type"] = event_name
	new_event["insert_id"] = random.choice(insert_id)
	event_properties = {}
	event_properties["count"] = random.randint(1,100)
	event_properties["direction"] = random.choice(user['user_properties']['directions'])
	direction = event_properties["direction"]
	count_lessons = event_properties["count"]
	new_event["event_properties"] = event_properties
	new_event["time"] = str(int(new_event["time"]) + 10)
	user["last_time"] = new_event["time"]
	new_event["event_id "] +=1
	events.append(new_event.copy())
	return user
	
def event_promo(new_event, events, user):
	promo = random.randint(0,2)
	if promo == 0:
		event_name = 'apply_promo_code'
		new_event["event_type"] = event_name
		new_event["insert_id"] = random.choice(insert_id)
		event_properties = {}
		event_properties["promocode"] = random.choice(promo_array)
		event_properties["discount_cost"] = round(count_lessons * 0.05,2)
		new_event["event_properties"] = event_properties
		new_event["time"] = str(int(new_event["time"]) + 5)
		user["last_time"] = new_event["time"]
		new_event["event_id "] +=1
		events.append(new_event.copy())
		return user

def event_bank_card_data_entry(new_event, events, user):
	event_name = 'bank_card_data_entry'
	new_event["event_type"] = event_name
	new_event["insert_id"] = random.choice(insert_id)
	event_properties = {}
	event_properties["payment_system"] = random.choice(payment_system_array)
	new_event["event_properties"] = event_properties
	new_event["time"] = str(int(new_event["time"]) + 8)
	user["last_time"] = new_event["time"]
	new_event["event_id "] +=1
	events.append(new_event.copy())
	return user

def event_click_confirm_payment(new_event, events, user):
	event_name = 'click_confirm_payment'
	new_event["event_type"] = event_name
	new_event["insert_id"] = random.choice(insert_id)
	event_properties = {}
	if promo == 0:
		event_properties["total_cost"] = count_lessons * 15 * 0.95
	else:
		event_properties["total_cost"] = count_lessons * 15 * 0.95 
	event_properties["direction"] = random.choice(user['user_properties']['directions'])
	new_event["event_properties"] = event_properties
	new_event["time"] = str(int(new_event["time"]) + 9)
	user["last_time"] = new_event["time"]
	user['user_properties']['status'] = 'studying'
	new_event["event_id "] +=1
	events.append(new_event.copy())
	return user

def event_click_start_lesson(new_event, events, user):
	event_name = 'click_start_lesson'
	new_event["event_type"] = event_name
	category_name = 'Lesson'
	new_event["category_name"] = category_name
	event_properties = {}
	event_properties["direction"] = random.choice(user['user_properties']['directions'])
	new_event["event_properties"] = event_properties
	new_event["user_properties"] = user["user_properties"]
	user['user_properties']['lessons_count']+=1
	if user['user_properties']['lessons_count'] > 70 and user['user_properties']['directions'][0] not in user['user_properties']['directions_finished']:
		user['user_properties']['directions_finished'].append(event_properties["direction"] )
	new_event["event_id "] +=1
	events.append(new_event.copy())
	return user

def event_click_allow_camera(new_event, events, user):
	event_name = 'click_allow_camera'
	new_event["event_type"] = event_name
	new_event["event_properties"] = {}
	new_event["user_properties"] = user["user_properties"]
	new_event["event_id "] +=1
	events.append(new_event.copy())

def event_click_allow_microphone'(new_event, events, user):
	event_name = 'click_allow_microphone'
	new_event["event_type"] = event_name
	new_event["event_properties"] = {}
	new_event["user_properties"] = user["user_properties"]
	new_event["event_id "] +=1
	events.append(new_event.copy())

def event_fail(new_event, events, user):
	probability_of_failure = random.randint(1,10)
	if probability_of_failure >= 7:
		event_name = 'click_technical_trouble'
		new_event["event_type"] = event_name
		new_event["event_properties"] = {}
		new_event["user_properties"] = user["user_properties"]
		new_event["event_id "] +=1
		events.append(new_event.copy())

def event_rate_lesson(new_event, events, user):
	probability_of_assessment = random.randint(0,2)
	if probability_of_assessment == 0:
		event_name = 'rate_lesson'
		new_event["event_type"] = event_name
		new_event["event_properties"] = {}
		new_event["user_properties"] = user["user_properties"]
		new_event["event_id "] +=1
		events.append(new_event.copy())

def event_click_change_direction(new_event, events):
	event_name = 'click_change_direction'
	new_event["event_type"] = event_name
	category_name = 'Training'
	new_event["category_name"] = category_name
	new_event["event_properties"] = {}
	new_event["user_properties"] = user["user_properties"]
	new_event["event_id "] +=1
	events.append(new_event.copy())

def event_choose_new_direction(new_event, events, user):
	event_name = 'choose_new_direction'
	new_event["event_type"] = event_name
	new_event["insert_id"] = random.choice(insert_id)
	event_properties = {}
	new_direction = random.choice(directions_array)
	while new_direction in user['user_properties']['directions']:
		new_direction = random.choice(directions_array)
		event_properties["new_direction"] = new_direction
		num_direction = random.randint(0,len(user['user_properties']['directions'])-1)
		event_properties["old_direction"] = user['user_properties']['directions'][num_direction]
		if isinstance(user['user_properties']['directions'], list) == True:
			if len(user['user_properties']['directions']) > 1:
				user['user_properties']['directions'][num_direction] = new_direction
			else:
				user['user_properties']['directions'] = new_direction
		else:
			dir = user['user_properties']['directions']
			user['user_properties']['directions'] = [dir]
		new_event["event_properties"] = event_properties
		new_event["time"] = str(int(new_event["time"]) + 7)
		user["last_time"] = new_event["time"]
		new_event["event_id "] +=1
		events.append(new_event.copy())
	return user

def event_choose_new_direction(new_event, events, user):
	event_name = 'click_change_teacher'
	new_event["event_type"] = event_name
	category_name = 'Training'
	new_event["category_name"] = category_name
	event_properties = {}
	event_properties["teacher_id"] = random.choice(user_id)
	new_event["event_properties"] = event_properties
	new_event["user_properties"] = user["user_properties"]
	new_event["event_id "] +=1
	events.append(new_event.copy())

def event_click_transfer_lesson(new_event, events, user):
	event_name = 'click_transfer_lesson'
	new_event["event_type"] = event_name
	category_name = 'Training'
	new_event["category_name"] = category_name
	event_properties = {}
	new_event["user_properties"] = user["user_properties"]
	new_event["event_id "] +=1
	events.append(new_event.copy())

def event_choose_new_time(new_event, events, user):
	event_name = 'choose_new_time'
	new_event["event_type"] = event_name
	new_event["insert_id"] = random.choice(insert_id)
	event_properties = {}
	event_properties["direction"] = random.choice(user['user_properties']['directions'])
	event_properties["new_interval"] = random.choice(interval_array)
	event_properties["old_interval"] = random.choice(interval_array)
	while event_properties["old_interval"] == event_properties["new_interval"]:
		event_properties["new_interval"] = random.choice(interval_array)
	new_event["event_properties"] = event_properties
	new_event["time"] = str(int(new_event["time"]) + 5)
	user["last_time"] = new_event["time"]
	new_event["event_id "] +=1
	events.append(new_event.copy())

################## BEHAIVOUR GRAPH ##################

def generate_anonymous_user(user, events, new_event):
	future_id = new_event["user_id"]
	new_event["user_id"] = "null"
	event_click_create_account(new_event, events, user)
	event_enter_info(new_event, events)
	event_account_created(new_event, events)
	event_account_verified(new_event, events)
	user = event_login(new_event, events, user)
	return user


def choose_actions_just_registered():
	user = event_click_signup_lesson(new_event, events, user)
	user = event_choose_direction(new_event, events, user)
	user = event_choose_time(new_event, events, user)
	user = event_record_confirmation(new_event, events, user)
	return user



def choose_actions_had_trial_lesson():
	event_click_pay_lessons(new_event, events, user)	
	user = event_choose_count_lessons(new_event, events, user)
	user = event_promo(new_event, events, user)
	user = event_bank_card_data_entry(new_event, events, user)
	user = click_confirm_payment(new_event, events, user)
		

def choose_actions_studying():
	probability = random.randint(1,7)
	if probability == 1:
		user = event_click_signup_lesson(new_event, events, user)
		user = event_choose_direction(new_event, events, user)
		user = event_choose_time(new_event, events, user)
		user = event_record_confirmation(new_event, events, user)

	if probability == 2:
		user = event_click_start_lesson(new_event, events, user)
		event_click_allow_camera(new_event, events, user)
		event_click_allow_microphone(new_event, events, user)
		event_fail(new_event, events, user)	
		event_rate_lesson(new_event, events, user)	

	if probability == 3:
		event_click_pay_lessons(new_event, events, user)	
		user = event_choose_count_lessons(new_event, events, user)
		user = event_promo(new_event, events, user)
		user = event_bank_card_data_entry(new_event, events, user)
		user = click_confirm_payment(new_event, events, user)

	if probability == 4:
		event_click_change_direction(new_event, events)
		event_choose_new_direction(new_event, events, user)

	if probability == 5:
		event_click_transfer_lesson(new_event, events, user)
		event_choose_new_time(new_event, events, user)

	if probability == 6:
		event_choose_new_direction(new_event, events, user)



