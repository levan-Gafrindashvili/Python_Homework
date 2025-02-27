# import os
# file_path = 'test/satesto.txt'
# print(os.path.exists(file_path))

# if os.path.exists(file_path):
#     os.remove(file_path)
# else:
#     print("file Doesn't exist")

# os.remove('test.txt')

# print(os.getcwd())
# os.mkdir('test1')
# os.rmdir('test1')
# os.rmdir('test')

# print(os.path.isfile('test/main.txt'))

# import shutil

# shutil.rmtree('test')

# txt = "H W"
# name = "Someone"

# encoded_txt = txt.encode()
# Encoded_name = name.encode()

# print(encoded_txt)

# with open('test.bin', "a") "a" Append "w" Write ReWrite "r" Read

# with open("satesto.txt", "w") as file:
#     file.write(txt)

# with open('satesto.bin', 'wb') as f:
#     f.write(txt)

# with open('test.bin', 'rt') as f:
#     data = f.read ()
#     print(data)

# with open('test.png', 'rb') as f:
#     data = f.read()

# print(len(data))

# with open('copy.png', 'wb') as file:
#     file.write(data)

# import csv
# csv.reader() კითხულობს რიგებს
# csv.writer() წერს რიგს ან რიგებს
# csv.DictReader()
# csv.DictWriter()

# import csv

# with open('students.csv', 'w', newline='') as csvfile:
#     headers = csvfile.readline()

#     data = csv.reader(csvfile)

#     print(next(data))
#     print(next(data))
#     print(next(data))

#     for row in data:
#         print(data)

# import csv
# headers = ['name', 'last_name', 'age']:

# data = [
#     ['bob', 'walker', 25],
#     ['walter', 'white', 56],
#     ['soul', 'goodman' 30]
# ]

# with open('data.csv', 'w', newline='') as csvfile:
#     writer = csv.write(csvfile)
#     writer.writerow(data)
#     writer.writerows(data)

# with open('companies.csv') as csvfile, open('test.csv', 'w', newline='') as csvfile2:
#     reader = csv.DictReader(csvfile)

#     # for company in reader:
#     #     print()

#     headers = reader.fieldnames
#     # headers = ['Something1','Something2','Something3','Something4','Something5'('in billions'),]
    
#     # for row in reader:
#     data = [company for company in reader if company['industry'] == 'technology']

#     writer = csv.DictWriter(csvfile2, fieldnames=headers)
#     writer.writeheader()
#     writer.writerow(reader)

#     # writer = csv.DictWriter(csvfile2, fieldnames=headers)
#     # writer.writeheader()
#     # writer.writerow(reader)

#     print(headers)


# for i in range(10):
#     print(fake.first_name(), fake.last_name(), fake.city(), sep=',')

# import csv
# from faker import Faker
# import random

# people = []
# fake = Faker()

# for i in range(20):
#     people.append({'id': i + 1,
#                     'name': fake.name(),
#                     'email': fake.email(),
#                     'city': fake.city(),
#                     'age': random.randint(20, 60)
#                     })
    
# for person in people:
#     print(person)

# id: 1, name: sfhs, email:email, age: 20 - 60