import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('en')
Faker.seed()


def generated_person():
	yield Person(
		full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
		email=faker_ru.email(),
		mobile=faker_ru.msisdn(),
		current_address=faker_ru.address(),
		permanent_address=faker_ru.address(),
		first_name=faker_ru.first_name(),
		last_name=faker_ru.last_name(),
		salary=random.randint(10000, 100000),
		age=random.randint(10, 80),
		department=faker_ru.job(),

	)


def generated_file():
	path = f'/home/andrei/Desktop/automation_qa_course/files/filetest{random.randint(0, 999)}.txt'
	file = open(path, 'w+')
	file.write(f'Hello World {random.randint(0, 999)}')
	file.close()
	return file.name, path


def generated_subject():
	subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
	            "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
	return subjects[random.randrange(len(subjects))]


def generated_state():
	states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
	return states[random.randrange(len(states))]


def generated_color():
	yield Color(
		color_name=['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Voilet', 'Indigo', 'Magenta', 'Aqua']
	)


def generated_date():
	yield Date(
		year=faker_en.year(),
		month=faker_en.month_name(),
		day=faker_en.day_of_month(),
		time="12:00",
	)
