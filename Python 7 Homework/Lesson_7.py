# 1. მოცემულია სია:
# (სახელი, გვარი, ასაკი)

# დაწერეთ უსასრულო ციკლი, რომელშიც მომხმარებელს ჰკითხავთ სახელს, თუ სახელი იქნება მოცემულ სიაში, შემდეგ ჰკითხეთ გვარი და გვარიც თუ იქნება,
# დაბეჭდეთ მისი ასაკი, ხოლო თუ არ იქნება სახელი დაბეჭდეთ რომ არ არის მოცემული სახელი, შესაბამისად გვარი აღარ ჰკითხოთ, ანალოგიურად
# მოიქეცით გვარის კითხვის შემთხვევაშიც. ციკლი უნდა გაჩერდეს იმ შემთხვევაში თუ მომხმარებელი შემოიყვანს სიტყვას "stop".


persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33), 
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

while True:
    first_name = input("enter first name: ")

    if first_name.lower() == "stop":
        print("Exiting the program.")
        break

    person_found = next((person for person in persons if person[0] == first_name), None)
    
    if person_found:
        last_name = input("enter last name: ")

        if last_name.lower() == "stop":
            print("Exiting the program.")
            break

        if person_found[1] == last_name:
            print(f"{first_name} {last_name}'s age is {person_found[2]}.")
        else:
            print(f"The last nmae '{last_name}' is not found for '{first_name}'.")
    else:
        print(f"The first name '{first_name}' is not in the list.")


# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს ჯერ პირველ და მერე მეორე სიტყვას.
#    იპოვეთ ამ სიტყვებში საერთო სიმბოლოები, განსხვავებული სიმბოლოები, და გაერთიანებული სიმბოლოები(ანუ ორივეში ერთად რომელიცაა ყველა ერთად)
#    დაბეჭდეთ ყველა ზემოთჩამოთვლილი(გამოიყენეთ set)

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
set1 = set(word1)
set2 = set(word2)

common_chars = set1.intersection(set2)
different_chars = set1.symmetric_difference(set2)
union_chars = set1.union(set2)

print(f"Common characters: {common_chars}")
print(f"Different characters: {different_chars}")
print(f"Union of characters: {union_chars}")