# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ ტექსტს და ამ ტექსტში დათვლის რამდენი სიმბოლო იყო მაღალ რეგისტრში
#    შეყვანილი და ასევე ამ ტექსტს გადააქცევს uppercase-ად ანუ მაღალ რეგისტრში დააბრუნებს, მაგალითად, მომხმარებელმა თუ შეიყვანა ტექსტი
#    Hello woRld, ფუნქციამ უნდა დააბრუნოს რომ 2 დიდი ამ ტექსტში და ეს ტექსტი აქციოს HELLO WORLD-ად.

# word = input("Enter A Word:  ")

# def extract_vowels(string):
#     vowels = "aeiou"
#     for character in string:
#         if character.lower() in vowels:
#             string = string.replace(character, " ")
#     return string

# print(f"extracted vowels:  {extract_vowels(word)}")

# 2. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს ე.წ. camel case ცვლადებს და დააბრუნებს snake case სახით, ანუ თუ გადავცემთ ცვლადს
#    firstName დააბრუნებს first_name, name დააბრუნებს ისევ name, preferredFirstName დააბრუნებს preferred_first_name, lastName დააბრუნებს
#    last_name და ასე შემდეგ.

word = input("Enter A Word:  ")

def camel_to_snake(string):
    result = []
    for character in string:
        if character.isupper():
            result.append("_")
            result.append(character)
        else:
            result.append(character)
    return ''.join(result)

print(camel_to_snake(word))