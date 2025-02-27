# 1. დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს რიცხვს, რა რიცხვსაც გადავცემთ, იმდენჯერ შეეკითხება მომხმარებელს 
#    სახელს, გვარს და ასაკს. ანუ თუ გადავეცით 3, 3-ჯერ შეეკითხება მომხმარებელს აღნიშნულ ინფორმაციას, ინფუთის 
#    საფუძველზე csv ფაილში ჩაწერეთ შესაბამისი ინფორმაცია შემდეგი სახით, მაგალითად:

#    ID,first_name,last_name,age
#    1,John,Doe,25
#    2,Alice,White,30

#    და ა.შ.
   
#    გამოიყენეთ try, ecxept იმისათვის რომ მომხმარებელმა ასაკის შემოყვანის დროს აუცილებლად ინტეჯერი შემოიყვანოს!
#    ფაილში ჩასაწერად აუცილებლად გამოიყენეთ csv მოდულიდან writer და DictWriter!


# import csv
# def collect_user_data(num_entries):
#     with open('user_data.csv', mode='w', newline='') as file:
#         fieldnames = ['ID', 'first_name', 'last_name', 'age']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()  
#         for i in range(1, num_entries + 1):
#             while True:
#                     first_name = input(f"Input First Name {i}: ")
#                     last_name = input(f"Input Last Name {i}: ")
#                     age = int(input(f"Input age {i}: ")) 

#                     writer.writerow({'ID': i, 'first_name': first_name, 'last_name': last_name, 'age': age})
#                     break 
# num_entries = int(input("Input number of users: "))
# collect_user_data(num_entries)


# 2. მიმაგრებულ students.csv ფაილიდან წაიკითხეთ ინფორმაცია, გაფილტრეთ Grade-ის მიხედვით შემდეგნაირად:
#    ყველა სტუდენტი, რომელსაც 50-ზე ნაკლები ქულა აქვს შეინახეთ ახალ ფაილში(failed_students.csv)
#    ყველა სტუდენტი, რომელსაც 50-ზე მეტი ქულა აქვს შეინახეთ ახალ ფაილში(passed_students.csv)

#    ფაილებიდან ინფორმაციის წასაკითხად და ჩასაწერად აუცილებლად გამოიყენეთ DictReader და DictWriter!


import csv

def filter_students():

    with open("students.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)

    failed_file = open('failed_students.csv', 'w', newline='')
    passed_file = open('passed_students.csv', 'w', newline='')

    fieldnames = ['ID', 'First Name', 'Last Name', 'Grade']
    failed_writer = csv.DictWriter(failed_file, fieldnames=fieldnames)
    passed_writer = csv.DictWriter(passed_file, fieldnames=fieldnames)

    failed_writer.writeheader()
    passed_writer.writeheader()

    for row in reader:
            grade = int(row['Grade'])
            if grade < 50:
                failed_writer.writerow(row) 
            else:
                passed_writer.writerow(row)

    csvfile.close()
    failed_file.close()
    passed_file.close()

filter_students()