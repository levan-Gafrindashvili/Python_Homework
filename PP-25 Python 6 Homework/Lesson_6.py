# 1. დაწერეთ პროგრამა, რომელიც შექმნის დიქტს, რომელშიც key-ები იქნება 1-დან 10-ის ცათვლით რიცხვები, ხოლო value-ები key-ს შესაბამისი
#    კვადრატები, ანუ {1: 1, 2: 4, 3: 9...}, არ დაწეროთ ხელით, გამოიყენეთ ციკლი(ბონუსი: გამოიყენეთ dictionary comprehension )

# ანუ keys გამოყენება მინოდა მაგრამ ვერ გამოვიყენე და ბოლოს range გამოვიყენე
# keys = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 

# dict = {x: x**2 for x in range[1, 11]}
# print(dict)


# 2. მოცემულია პროდუქტების ლისტი:
products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]

# ა. დაბეჭდეთ ყველა პროდუქტის დასახელება
# ბ. გამოითვალეთ ყველა პროდუქტის ღირებულების ჯამი(ანუ პროდუქტის ფასი უნდა გაამრავლოთ რაოდენობაზე და დააჯამოთ)

# for snack in products:
#     for name in snack:
#         print(name)

# total_value = 0
# for snack in products:
#     for name, details in snack.items():
#         total_value += details["price"] * details["quantity"]
#         print(f"total value{total_value}")


# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ხილის სახელს, მანამ სანამ, მომხმარებელი არ შეიყვანს სიტყვას stop,
#    ამის შემდეგ გამოიტანეთ დიქტის სახით ხილის დასახელება და ველიუ იქნება რამდენჯერაც შეიყვანა ეს ხილი, მაგალითად:

#    Enter your favorite fruit: banana
#    Enter your favorite fruit: apple
#    Enter your favorite fruit: banana
#    Enter your favorite fruit: stop

# შედეგი:

# {'banana': 2, 'apple': 1}

fruit_count = {}

while True:
    fruit = input("Enter fruit: ")
    
    if fruit.lower() == "stop":
        break
    
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1

print(fruit_count)
