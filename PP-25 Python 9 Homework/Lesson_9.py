# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს, თუ რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი და საბოლოოდ დააჯამებს
#    ყველა შეყვანილ რიცხვს, თუ არგუმენტად არ გადაეცა არანაირი რიცხვი, მაშინ ფუნქციამ 5-ჯერ ჰკითხოს მომხმარებელს რიცხვის 
#    შეყვანა და დააჯამოს ეს 5 რიცხვი. დააბრუნეთ საბოლოო ჯამი

def numbers(times=5):
    total = 0
    for i in range(times):
        number = int(input(f"Enter number {i+1}: "))
        total += number
    return total

# ამაზე დარწმუნებული არ ვარ  მგონი სწორად მიწერია

# 2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#    ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები

def separate_numbers(arguments):
    odd_numbers = []
    even_numbers = []
    
    for num in arguments:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return odd_numbers, even_numbers

odd, even = separate_numbers(1, 2, 3, 4, 5, 6, 7, 8)
print("Odd numbers:", odd)
print("Even numbers:", even) 

# 3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
#    და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
#    შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
#    ჰქონდეს მნიშვნელობა!)

def count_words(sentence):
    sentence = sentence.lower()
    sentence = ''.join(char for char in sentence if char.isalnum() or char.isspace())
    
    words = sentence.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

sentence = "This is a test. This test is fun."
result = count_words(sentence)
print(result)


# 4. დაწერეთ რეკურსიული ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და დააბრუნებს 1-დან ამ რიცხვის ჩათვლით ყველა რიცხვის ჯამს

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)

result = sum_numbers(5)
print(result)

# აქ სიტყვა რეკურსიულმა დამაბნია ძაან და დაგუგლვა მომიწია რო ჩემ ენაზე გამეგო 
# მგონი წესით რაც იყო ამ დავალებაში სწორად დავწერე