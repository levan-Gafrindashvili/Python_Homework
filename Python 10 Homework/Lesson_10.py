# 1. გამოიყენეთ lambda ფუნქცია sorted() ფუნქციაში, იმისათვის რომ დაასორტიროს მოცემული ლისტი:
#    [(1, 3), (4, 2), (2, 5)] - მასში არსებული ელემენტების მეორე ელემენტის მიხედვით

# My_list = [(1, 3), (4, 2), (2, 5)]

# Sorted_list = sorted(My_list, key=lambda x: x[1])

# print(Sorted_list)

# 2. დაწერეთ ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ორ რიცხვს და პირველ რიცხვს გაყოფს მეორე რიცხვზე და დააბრუნებს შედეგს, 
# დაიჭირეთ ორი ერორი: ის რომ მომხმარებელმა ინტეჯერები შეიყვანოს და ნულზე რომ არ შეიძლება გაყოფა, თითოეული ერორისთვის გამოუტანეთ 
# შესაბამისი შეტყობინება. (ორივე ერორი უნდა იყოს შესაბამისი ერორებით დაჭერილი, არ გამოიყენოთ ზოგადი იქსეფშენი)

# def divide_numbers():
#     try:
#         num1 = int(input("Enter the first number (integer): "))
#         num2 = int(input("Enter the second number (integer): "))
        
#         result = num1 / num2
#         print(f"The result of division is: {result}")
    
#     except ValueError:
#         print("Error: Please enter valid integers.")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")

# divide_numbers()

# 3. მოცემულია პროდუქტების ლისტი:

# filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
# map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
# sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
# reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი

from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

# 1)
# filtered_products = list(filter(lambda product: product["price"] < 101, products))
# print("Products with price less than 100:", filtered_products)

# 2)
# mapped_products = list(map(lambda product: f"{product['name']} - ${product['price']}", products))
# print("Product names and prices:", mapped_products)

# 3)
# sorted_products = sorted(products, key=lambda product: product["price"])
# print("Products sorted by price:", sorted_products)

# 4)
total_price = reduce(lambda total, product: total + product["price"], products, 0)
print("Total price of all products:", total_price)