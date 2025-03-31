# 1. შექმენით მთელი რიცხვების მინიმუმ 5 ელემენტიანი სია, გამოთვალეთ ყველა რიცხვის ჯამი და საშუალო, არ გამოიყენოთ ჩაშენებული ფუნქციები!

# numbers = [2, 5, 8, 12, 3]
# # ჯამის გამოთვლა
# sum_of_numbers = 0
# for number in numbers:
#     sum_of_numbers += number

# # საშუალოს გამოთვლა
# average = sum_of_numbers / len(numbers)

# print("Sum:", sum_of_numbers)
# print("Average:", average)

# 2. მოცემულია სია ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1], დაწერეთ ლოგიკა, როემლიც ამ ლისტში დატოვებს უნიკალურ
# ელემენტებს, ანუ არ განმეორდება ელემენტები. არ გამოიყენოთ set!

# my_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]

# unique_list = []

# for item in my_list:
#     if item not in unique_list:
#         unique_list.append(item)

# print(unique_list)

# 3. დააგენერირეთ 20 ელემენტიანი რიცხვების სია, რომელიც შევსებული იქნება -50 დან 50-მდე შემთხვევითი რიცხვებით და შექმენით მეორე 
# სია, რომელიც პირველი სიიდან იქნება შევსებული მხოლოდ ლუწი რიცხვებით და დაბეჭდეთ ორივე სია, გამოიყენეთ აუცილებლად ლისტის გენერატორი!

import random

first_list = [random.randint(-50, 50) for _ in range(20)]

even_list = [num for num in first_list if num % 2 == 0]

print("first_list:", first_list)
print("even_list :", even_list)
