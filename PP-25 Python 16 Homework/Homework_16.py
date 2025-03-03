# 1. დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, დაუწერეთ დეკორატორი, 
# რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი

# 2. შექმენით მეტაკლასი, რომელიც სხვა კლასზე გამოყენების შემთხვევაში შეამოწმებს ამ კლასის მეთოდის სახელებს,
#    შემდეგი სახით: თუ მეთოდი იწყება _ ეს მეთოდი ვალიდური იქნება, თუ არ იწყება _, მაშინ აღზევდეს 
#    ValueError. მაგ: _test() - ეს მეთოდი იქნება ვალიდური, test() - ეს მეთოდი არ იქნება ვალიდური
#    და გამოიწვევს ValueError-ს. გაითვალისწინეთ რომ მეტაკლასმა უნდა შეამოწმოს მხოლოდ მეთოდები და არა ატრიბუტები!


# class account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance

# 1)

# def transaction_fee(func):
#     def wrapper(balance, amount):
#         fee = 1
#         total = amount + fee
#         if balance < total:
#             return "Not Enough funds"  
        
#         return func(balance - total, amount)
#     return wrapper

# @transaction_fee
# def transaction_proccess(balance, amount):
#     return f"Transaction completed, Blance Left: {balance}"

# balance = 100
# amount = 50
# print(transaction_proccess(balance, amount))

# balance = 10
# amount = 8
# print(transaction_proccess(balance, amount))

# 2)

class MetaClass(type):
    def __new__(cls, name, bases, class_dict):
        for attr_name, attr_value in class_dict.items():
            if callable(attr_value) and not attr_name.startswith("_"):
                raise ValueError("Method name must start with _")
        return super().__new__(cls, name, bases, class_dict)

class ValidClass(metaclass=MetaClass):
    def _valid_method(self): pass

try:
    class InvalidClass(metaclass=MetaClass):
        def invalid_method(self): pass
except ValueError as e:
    print(e)

# ეს როგორ დავწერე არ ვიცი სწორი თუა ეგეც არ ვიცი 
# მერე ერთი ორჯერ კიდე გადავხედავ ამ ლექციას რო უკეთ გავიგო 
# რა დონეზეც გავიგე ასე დავწერე