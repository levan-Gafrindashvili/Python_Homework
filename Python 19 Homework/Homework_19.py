# დააგენერირეთ სტუდენტის დიქშენერების 100 ელემენტიანი სია
# სახელების, გვარების და იმეილების რენდომულად დასაგენერირებლად
# გამოიყენეთ faker მოდული

# სტუდენტს უნდა ჰქონდეს შემდეგი key-ები და შესაბამისი value-ები:
# first_name - გამოიყენეთ faker
# last_name - გამოიყენეთ faker
# email - გამოიყენეთ faker
# age - 18დან 70 წლამდე(შემთხვევითი პრინციპით)
# is_active - (True ან False) რანდომულად

# არსებული სია json მოდულის დახმარებით ჩაწერეთ ფაილში

# შემდეგ წაიკითხეთ ეს ფაილი json მოდულის დახმარებით, 
# გაფილტრეთ სტუდენტები is_active ქის მიხედვით, ისეთი სტუდენტები რომლის is_active
# არის True, შეიტანეთ ლისტში და ჩაწერეთ ახალ ფაილში

import json
from faker import Faker
import random
fake = Faker()
students = []

for _ in range(100):
    student = {
        "first_name": fake.name(),
        "last_name": fake.name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }
    students.append(student)

with open("PP-25 Python 19 Homework\students.json", "w") as file:
    json.dump(students, file, indent=4)

for student in students:
    if student["is_active"]:
        print(student)

# students_by_age = sorted(students, key=lambda x: x["age"]) # აქ ასაკითაც მაინტერესება და დავალაგე
# # print(students_by_age[1:5])
# for student in students_by_age:
#     print(student)