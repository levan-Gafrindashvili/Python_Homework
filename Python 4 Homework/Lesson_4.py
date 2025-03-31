# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს წინადადებას, პირველ სიტყვას და მეორე სიტყვას და შემოყვანილ წინადადებაში
# პირველ სიტყვას ჩაანაცვლებს მეორე სიტყვით

# sentence = input("input sentence: ")
# word1 = input("input first word: ")
# word2 = input("input second word: ")

# modified_sentence = sentence.replace(word1, word2, 1)

# print("new sentence:", modified_sentence)

# 2. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოყვანილ წინადადებაში იპოვის ყველაზე გრძელ სიტყვას და დაბეჭდავს მას

# sentence = input("input sentence: ")

# words = sentence.split()

# longest_word = max(words, key=len)

# print("longest word is:", longest_word)

# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ სიტყვას შეამოწმებს არის თუ არა ერთმანეთის ანაგრამა
# ანაგრამა არის ერთ სიტყვაში ასოების გადაადგილებით მიღებული მეორე სიტყვა, მაგალითად ("listen", "silent" ), ("Triangle", "Integral")
# და ა.შ. უნდა იყოს case-insensitive, ანუ მომხმარებელი დიდი ასოებით შემოიყვანს თუ არა ტექსტს, არ უნდა ჰქონდეს მნიშვნელობა.
# არ გამოიყენოთ sorted() ფუნქცია.

word1 = input("input first word: ").lower()
word2 = input("input second word: ").lower()

if len(word1) != len(word2):
    print("this words arn't anagrams.")
else:
    char_count1 = {}
    char_count2 = {}
    
    for char in word1:
        char_count1[char] = char_count1.get(char, 0) + 1
        
    for char in word2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    if char_count1 == char_count2:
        print("these words are anagrams.")
    else:
        print("these words arn't anagrams.")
