import json

def add_person(count):
    try:
        with open('PP-25 Python 20 Homework\persons.json', 'r') as f:
            data = json.load(f)

    except FileNotFoundError:
        data = []

    for _ in range(count):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        new_id = max([person["id"] for person in data], default=0) + 1
        data.append({"id": new_id, "name": name, "age": age})

    with open('PP-25 Python 20 Homework\persons.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    count = int(input("Enter the number of people: "))
    add_person(count)