# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს უსასრულოდ შეეკითხება ჯერ სახელს, შემდეგ გვარს და რაიმე ფაილში ჩაწერს 
#    სახელს და გვარს ერთ ხაზზე თავისი ნუმერაციით, ყველა ახალი სახელი და გვარი უნდა იყოს ახალ ხაზზე ჩაწერილი, მაგალითად:
   
#     პროგრამა ჩერდება იმ შემთხევაში, თუ მომხმარებელმა სახელის ადგილას შეიყვანა სიტყვა stop

#    Enter your first name: Otar
#    Enter your last name: Tumanishvili
#    Enter your first name: Nika
#    Enter your last name: Papaskiri
#    Enter your first name: stop

#    ფაილში უნდა ჩაიწეროს შემდეგი სახით:
#    1. Otar Tumanishvili
#    2. Nika 


# file_name = "names.txt"

# with open(file_name, "a") as file:

#     while True:
#         first_name = input("Enter first Name: ")
#         if first_name == "stop":
#             break

#         last_name = input("Enter last Name: ")
#         if last_name == "stop":
#             break

#         file.write(f"- {first_name} {last_name}\n")

# (აქ ის ვერ გავიგე მეორეჯერ რო მინდა ჩაწერა ვერ ვწერ აღარ წერს სწორად ფაილში)


# 2. თანდართულ ფაილში "persons.txt" მოცემულია ადამიანების სია შემდეგი ფორმატით:
#    სახელი და გვარი, ასაკი, ქალაქი

#    Evelyn Cook, 75, Nixonland
#    Dr. Briana Davidson, 22, South Hunterside
#    ...
#    ...

#    თქვენი დავალებაა არსებული ფაილიდან წაიკითხოთ ინფორმაცია, შექმნათ ორი ახალი ტექსტური ფაილი (.txt გაფართოებით), ერთ ფაილში
#    ჩაწერეთ ყველა პიროვნება რომლის ასაკი ნაკლებია 50-ზე, ხოლო მეორე ფაილში ჩაწერეთ ყველა პიროვნება, რომლის ასაკი მეტია 50-ზე,
#    ფორმატი დაცული უნდა იყოს ისეთი სახით, როგორიც არის ორიგინალ "persons.txt" ფაილში ანუ თითო პიროვნება თითო ხაზზე!


input_file = "persons.txt"
output_file_under_50 = "under_50.txt"
output_file_over_50 = "over_50.txt"
infile = open(input_file, "r")
under_50_file = open(output_file_under_50, "w")
over_50_file = open(output_file_over_50, "w")
    
for line in infile:
    line = line.strip()
    
    parts = line.split(", ")
    
    name, age, city = parts[0], int(parts[1]), parts[2]
    
    if age < 50:
        print(line, file=under_50_file)
    else:
        print(line, file=over_50_file)
