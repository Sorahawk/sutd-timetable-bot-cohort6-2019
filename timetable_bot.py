from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime, date, time
from collections import Counter
import operator, random

updater = Updater(token=<YOUR_BOT_TOKEN>, use_context=True)
dispatcher = updater.dispatcher
job = updater.job_queue


subjects = {1.010: 'Freshmore Writing Programme', 1.011: 'Professional Practice Programme', 1.012: 'Career Planning & Resume Writing', 1.018: 'Design Integrated Project I',\
			2.001: 'HASS', 2.003: 'HASS', 3.007: 'Introduction to Design', 10.001: 'Advanced Math I', 10.002: 'Physics I', 10.004: 'Advanced Math II', 10.005: 'Physics II',\
			10.006: 'Chemistry and Biology', 10.007: 'Modelling the Systems World', 10.008: 'Engineering in Physical World', 10.009: 'The Digital World',\
			10.011: 'Intro to Physical Chemistry', 10.012: 'Introduction to Biology', 20.099: 'Urban Sketching'}

locations = {0: 'TBA', 1.101: 'Library', 1.102: 'Albert Hong Lecture Theatre 1', 1.203: 'Lecture Theatre 2', 1.308: 'Think Tank 1', 1.309: 'Think Tank 2', 1.310: 'Think Tank 3',\
			1.312: 'Think Tank 4', 1.313: 'Think Tank 5', 1.314: 'Cohort Classroom 1', 1.315: 'Cohort Classroom 2', 1.408:'Think Tank 6', 1.409: 'Think Tank 7', 1.410: 'Think Tank 8',\
			1.411: 'Capstone 1', 1.412: 'Capstone 2', 1.413: 'Cohort Classroom 3', 1.414: 'Cohort Classroom 4', 1.415: 'Think Tank 9', 1.416: 'Think Tank 10', 1.503: 'Think Tank 11',\
			1.505: 'Pi Lab', 1.506: 'Think Tank 12', 1.508: 'Yang Zheng Foundation Think Tank 13', 1.509: 'Think Tank 14', 1.510: 'Think Tank 15', 1.511: 'Capstone 3',\
			1.512: 'Capstone 4', 1.514: 'Cohort Classroom 6', 1.521: 'Studio 1', 1.605: 'Information Systems Lab', 1.606: 'Capstone 5', 1.607: 'Capstone 6', 1.608: 'Cohort Classroom 7',\
			1.609: 'Cohort Classroom 8', 1.610: 'Trading Lab', 1.611: 'Computer Lab', 1.612: 'LEET Lab', 1.614: 'SUTD-SMU Collaboration Office', 1.617: 'Studio 2',\
			2.101: 'Auditorium', 2.201: 'Think Tank 16', 2.202: 'Think Tank 17', 2.203: 'Think Tank 18', 2.204: 'IT Care Office', 2.304: 'Think Tank 19', 2.305: 'Think Tank 20',\
			2.307: 'Cohort Classroom 9', 2.308: 'Cohort Classroom 10', 2.310: 'Think Tank 21', 2.311: 'Think Tank 22',  2.312: 'ROOT Cove', 2.316: 'Game Lab', 2.403: 'Lecture Theatre 3',\
			2.404: 'Lecture Theatre 4', 2.405: 'Cohort Classroom 11', 2.406: 'Cohort Classroom 12', 2.408: 'Capstone 7', 2.409: 'Capstone 8', 2.411: 'Physics Lab',\
			2.412: 'Digital Systems Lab', 2.413: 'Think Tank 23', 2.414: 'The Writing Centre', 2.503: 'Think Tank 24', 2.504: 'A C Toh Think Tank 25', 2.505: 'Lecture Theatre 5',\
			2.506: 'Cohort Classroom 13', 2.507: 'Cohort Classroom 14', 2.509: 'Capstone 9', 2.510: 'Capstone 10', 2.512: 'Chemistry Lab', 2.513: 'Biology Lab', 2.514: 'Think Tank 26',\
			2.518: 'Studio 3', 2.519: 'Studio 4', 2.605: 'IDiA Lab', 2.606: 'Cohort Classroom 15', 2.607: 'Cohort Classroom 16', 2.610: 'Cognition Lab', 2.611: 'Future Living Lab',\
			2.614: 'Characterisation Lab', 2.619: 'Studio 5', 2.620: 'Studio 6',\
			3.102: 'One-Stop Centre', 3.201: 'Office of Student Affairs', 3.202: 'Lee Kuan Yew Centre for Innovative Cities', 3.204: 'Space Bar',\
			3.302: 'Office of International Relations / SUTD-ZJU Collaboration Office',\
			5.100: 'Fabrication Lab', 5.101: 'Maker Space 1', 5.201: 'Maker Space 2', 5.303: 'Career Development Centre',\
			61.103: 'Fitness Centre (Gym)', 61.105: 'Indoor Sports Hall 1', 61.106: 'Indoor Sports Hall 2', 61.208: 'Office of Housing'}


classes = []
exams = []

def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="Tick tock, you're late o'clock!")
	get_user_id(update, context)


def nextClass(update, context):
	current_date = str(date.today())
	current_time = str(datetime.now().strftime("%H:%M"))

	for className in classes:
		if current_date > className[0]:
			pass
		else:
			if (current_date == className[0] and current_time <= className[1]) or current_date < className[0]:
				d = className[0].split('-')
				day = date(int(d[0]), int(d[1]), int(d[2]))
				dayDate = day.strftime("%A, %d %B")
				classDetails = "{} @ {} ({})\n{}\n{} to {}".format(subjects[className[3]], locations[className[4]], className[4], dayDate, className[1], className[2])
				break

	context.bot.send_message(chat_id=update.message.chat_id, text=classDetails)
	get_user_id(update, context)


def today(update, context):
	current_date = str(date.today())
	current_time = str(datetime.now().strftime("%H:%M"))

	classList = ''
	for className in classes:
		if current_date == className[0]:
			d = className[0].split('-')
			day = date(int(d[0]), int(d[1]), int(d[2]))
			dayDate = day.strftime("%A, %d %B")
			classDetails = "{} @ {} ({})\n{}\n{} to {}\n\n".format(subjects[className[3]], locations[className[4]], className[4], dayDate, className[1], className[2])
			classList += classDetails

	if classList == '':
		classList = 'There are no classes today. Hooray!'

	context.bot.send_message(chat_id=update.message.chat_id, text=classList)
	get_user_id(update, context)


def nextDay(update, context):
	current_date = str(date.today())
	current_time = str(datetime.now().strftime("%H:%M"))

	for className in classes:
		if current_date >= className[0]:
			pass
		else:
			chosenDate = className[0]
			break

	classList = ''
	for className in classes:
		if chosenDate == className[0]:
				d = className[0].split('-')
				day = date(int(d[0]), int(d[1]), int(d[2]))
				dayDate = day.strftime("%A, %d %B")
				classDetails = "{} @ {} ({})\n{}\n{} to {}\n\n".format(subjects[className[3]], locations[className[4]], className[4], dayDate, className[1], className[2])
				classList += classDetails

	context.bot.send_message(chat_id=update.message.chat_id, text=classList)
	get_user_id(update, context)


def allClass(update, context):
	current_date = str(date.today())
	current_time = str(datetime.now().strftime("%H:%M"))

	classList = ''
	for className in classes:
		if current_date > className[0]:
			pass
		else:
			if (current_date == className[0] and current_time <= className[1]) or current_date < className[0]:
				d = className[0].split('-')
				day = date(int(d[0]), int(d[1]), int(d[2]))
				dayDate = day.strftime("%A, %d %B")
				classDetails = "{} @ {} ({})\n{}\n{} to {}\n\n".format(subjects[className[3]], locations[className[4]], className[4], dayDate, className[1], className[2])
				classList += classDetails

	context.bot.send_message(chat_id=update.message.chat_id, text=classList)
	get_user_id(update, context)


def nextExam(update, context):
	current_date = str(date.today())
	current_time = str(datetime.now().strftime("%H:%M"))

	for examName in exams:
		if current_date > examName[0]:
			pass
		else:
			if (current_date == examName[0] and current_time <= examName[1]) or current_date < examName[0]:
				d = examName[0].split('-')
				day = date(int(d[0]), int(d[1]), int(d[2]))
				dayDate = day.strftime("%A, %d %B")
				examDetails = "{} {} Exam @ {} ({})\n{}\n{} to {}\n\n".format(subjects[examName[3]], examName[5], locations[examName[4]], examName[4], dayDate, examName[1], examName[2])
				break

	context.bot.send_message(chat_id=update.message.chat_id, text=examDetails)
	get_user_id(update, context)


def allExams(update, context):
	current_date = str(date.today())
	current_time = str(datetime.now().strftime("%H:%M"))

	examList = ''
	for examName in exams:
		if current_date > examName[0]:
			pass
		else:
			if (current_date == examName[0] and current_time <= examName[1]) or current_date < examName[0]:
				d = examName[0].split('-')
				day = date(int(d[0]), int(d[1]), int(d[2]))
				dayDate = day.strftime("%A, %d %B")
				examDetails = "{} {} Exam @ {} ({})\n{}\n{} to {}\n\n".format(subjects[examName[3]], examName[5], locations[examName[4]], examName[4], dayDate, examName[1], examName[2])
				examList += examDetails

	context.bot.send_message(chat_id=update.message.chat_id, text=examList)
	get_user_id(update, context)


def find_room(update, context):
	target_location = ''.join(update.message.text.split(' ')[1:]).lower() # remove all whitespace from location input and lower all letters to lowercase

	if target_location[:3] == 'cc0':
		target_location = 'cohortclassroom' + target_location[3:]
	elif target_location[:3] == 'tt0':
		target_location = 'thinktank' + target_location[3:]
	elif target_location[:2] == 'cc' or target_location[:2] == 'f0':
		target_location = 'cohortclassroom' + target_location[2:]
	elif target_location[:2] == 'lt':
		target_location = 'lecturetheatre' + target_location[2:]
	elif target_location[:2] == 'tt':
		target_location = 'thinktank' + target_location[2:]
	elif target_location[:3] == 'bio':
		target_location = 'biology' + target_location[3:]
	elif target_location[:3] == 'gym':
		target_location = 'fitnesscentre' + target_location[3:]
	elif target_location[:3] == 'ish':
		target_location = 'indoorsportshall' + target_location[3:]
	elif target_location[:3] == 'lky':
		target_location = 'leekuanyew' + target_location[3:]

	# search by closest result by matching unique letters, then check for highest match that is unique score, then check if highest match >= 6
	result_found = False
	search_results = {}
	for room_id in locations:
		room_name = locations[room_id].replace(' ', '').lower()

		if target_location == room_name:
			room_result_id = room_id
			room_result_name = locations[room_id]
			
			building = str(room_result_id).split('.')[0]
			level = str(room_result_id).split('.')[1][0]

			context.bot.send_message(chat_id=update.message.chat_id, text="{} ({})\nBuilding {}, Level {}".format(room_result_name, room_result_id, building, level))
			get_user_id(update, context)
			result_found = True
			break
		else:
			common_letters = Counter(target_location) & Counter(room_name)
			total_common = sum(common_letters.values())
			search_results[room_id] = total_common

	if not result_found:
		highest_common_id = max(search_results.items(), key=operator.itemgetter(1))[0]
		highest_common_value = max(search_results.items(), key=operator.itemgetter(1))[1]

		failed_search = False
		for room_id in search_results:
			if (search_results[room_id] == highest_common_value and room_id != highest_common_id) or highest_common_value < 5:
				context.bot.send_message(chat_id=update.message.chat_id, text="Can't find what you're trying to look for.")
				get_user_id(update, context)
				failed_search = True
				break

		if not failed_search:
			building = str(highest_common_id).split('.')[0]
			level = str(highest_common_id).split('.')[1][0]

			context.bot.send_message(chat_id=update.message.chat_id, text="{} ({})\nBuilding {}, Level {}".format(locations[highest_common_id], highest_common_id, building, level))
			get_user_id(update, context)


def send_message_to_user(update, context):
	split_message = update.message.text.split()
	target_user = split_message[1]
	message = ' '.join(split_message[2:])
	context.bot.send_message(chat_id=target_user, text=message)


start_handler = CommandHandler('start', start)
nextClass_handler = CommandHandler('next_class', nextClass)
today_handler = CommandHandler('today', today)
nextDay_handler = CommandHandler('next_day', nextDay)
allClass_handler = CommandHandler('all_class', allClass)
nextExam_handler = CommandHandler('next_exam', nextExam)
allExams_handler = CommandHandler('all_exams', allExams)
findRoom_handler = CommandHandler('find', find_room)
sendDM_handler = CommandHandler('sendUser', send_message_to_user)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(nextClass_handler)
dispatcher.add_handler(today_handler)
dispatcher.add_handler(nextDay_handler)
dispatcher.add_handler(allClass_handler)
dispatcher.add_handler(nextExam_handler)
dispatcher.add_handler(allExams_handler)
dispatcher.add_handler(findRoom_handler)
dispatcher.add_handler(sendDM_handler)

updater.start_polling()
