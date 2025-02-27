# print("hello world")

# Firstname = "levani"
# LastName = "Gafrindashvili"
# Age = 21

# print( Firstname,LastName,Age)
# num1 = int(input('input first number:'))
# num2 = float(input('input second number:'))

# sum_numbers = num1 + num2

# print(sum_numbers)

# num1 = 20
# num2 = 10.5
# num3 = "25"
# is_equal = False

# print(type(is_equal))

# 1) დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება მართკუთხა სამკუთხედის კათეტების სიგრძეს(მთელი დადებითი რიცხვი) და გამოითვლის 
# ამ სამკუთხედის ჰიპოთენუზის სიგრძეს და ფართობს.


import math

a = int(input("Enter the first leg of the triangle: "))
b = int(input("Enterthe second leg of the triangle: "))

hypotenuse = math.sqrt(a**2 + b**2)

area = 0.5 * a * b

print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
print(f"The area of the triangle is: {area}")


# დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება წამების რაოდენობას და გამოიტანეთ საათების, წუთების და წამების
# რაოდენობას (მაგ. 20000 წამი არის  5 საათი, 33 წუთი, 20 წამი)

# total_seconds = int(input("Enter the number of seconds: "))

# seconds = total_seconds % 60

# minutes = (total_seconds % 3600) // 60

# hours = total_seconds // 3600

# print(f"{total_seconds} seconds is {hours} hours, {minutes} minutes, {seconds} seconds.")

# a = 5
# b = 6

# if a > b:
#     print("a is more")

# print("done")