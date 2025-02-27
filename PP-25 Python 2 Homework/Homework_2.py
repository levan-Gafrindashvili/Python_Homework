# 1. დაწერეთ პროგრამა რომელიც მომხმარებელს ჰკითხავს წონას(კგ) და სიმაღლეს(მ), შეყვანილი მონაცემების 
# საფუძველზე გამოითვლის BMI-ს(Body Mass Index). ფორმულა: წონა გაყოფილი სიმაღლის კვადრატზე
# თუ BMI ნაკლებია 19-ზე, გამოიტანეთ ინფო რომ ის არის underweight
# თუ BMI არის 19 და 25 შორის, გამოიტანეთ ინფო რომ ის არის normalweight
# თუ BMI მეტია 25-ზე, გამოიტანეთ ინფო რომ ის არის overweight


# height = float(input("Enter your height "))
# weight = float(input("Enter your weight "))
# x = weight/(height/100)**2

# print(x)
# if x < 18.5:
#     print('Underweight')
# if x>=18.5 and x<25:
#     print("Normal")
# if x >= 25 and x < 30:
#    print('Overweight')
# if x >= 30:
#    print('Obese')


# 2. დაწერეთ კალკულატორის პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და არითმეტიკულ ოპერატორს,
# შესაბამისი ოპერატორის საფუძველზე გამოითვლის ამ ორი რიცხვის შედეგს.(გამოიყენეთ Match-Case მეთოდი)

# x = int(input("Enter The First Number  "))
# y = int(input("Enter The Second Number  "))
# Operator = input("Enter an Arithmetic Operator (+, -, *, /, //, %, **): ")

# if Operator == "+":
#     result = x + y
# elif Operator == "-":
#     result = x - y
# elif Operator == "*":
#     result = x * y
# elif Operator == "/":
#     result = x / y
# elif Operator == "//":
#     result = x // y
# elif Operator == "%":
#     result = x % y
# elif Operator == "**":
#     result = x ** y

# print(result)

# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება 3 რიცხვს, ჯერ შეამოწმეთ ეს რიცხვები არ უდრიდეს ერთმანეთს,
# თუ რომელიმე ორი ერთმანეთს უდრის, დაპრინტეთ რომ შეიყვანოს განსხვავებული რიცხვები. თუ რიცხვები განსხვავებულია, 
# იპოვეთ ყველაზე დიდი რიცხვი

num1 = float(input("first number: "))
num2 = float(input("second number: "))
num3 = float(input("third number: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("input different number!")
else:
    largest = max(num1, num2, num3)
    print(f"biggest number is: {largest}")
