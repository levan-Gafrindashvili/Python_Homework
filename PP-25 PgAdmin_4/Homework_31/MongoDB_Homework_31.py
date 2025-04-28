from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
students_collection = db["students"]

# students_collection.delete_many({})

students = [
    {
        "name": "John Doe",
        "age": 20,
        "grade": "B",
        "courses": ["Math", "Science"],
        "address": {"city": "New York", "zipcode": "10001"},
        "attendance": 85
    },
    {
        "name": "Alice Smith",
        "age": 19,
        "grade": "A",
        "courses": ["History", "Math"],
        "address": {"city": "Los Angeles", "zipcode": "90001"},
        "attendance": 92
    },
    {
        "name": "Bob Johnson",
        "age": 22,
        "grade": "C",
        "courses": ["Art", "Science"],
        "address": {"city": "Chicago", "zipcode": "60601"},
        "attendance": 70
    },
    {
        "name": "Emily Davis",
        "age": 21,
        "grade": "B",
        "courses": ["Math", "Physics"],
        "address": {"city": "New York", "zipcode": "10002"},
        "attendance": 88
    },
    {
        "name": "Chris Brown",
        "age": 18,
        "grade": "A",
        "courses": ["Chemistry", "Biology"],
        "address": {"city": "San Francisco", "zipcode": "94101"},
        "attendance": 95
    },
    {
        "name": "Daniel Wilson",
        "age": 23,
        "grade": "B",
        "courses": ["Math", "English"],
        "address": {"city": "Los Angeles", "zipcode": "90002"},
        "attendance": 90
    },
    {
        "name": "Laura Martinez",
        "age": 20,
        "grade": "C",
        "courses": ["Science", "History"],
        "address": {"city": "Miami", "zipcode": "33101"},
        "attendance": 65
    },
    {
        "name": "James Anderson",
        "age": 17,
        "grade": "B",
        "courses": ["Math", "Science"],
        "address": {"city": "New York", "zipcode": "10003"},
        "attendance": 75
    },
    {
        "name": "Olivia Thomas",
        "age": 22,
        "grade": "A",
        "courses": ["Physics", "Math"],
        "address": {"city": "Seattle", "zipcode": "98101"},
        "attendance": 93
    },
    {
        "name": "Sophia Jackson",
        "age": 19,
        "grade": "B",
        "courses": ["Art", "Math"],
        "address": {"city": "Los Angeles", "zipcode": "90003"},
        "attendance": 85
    }
]

students_collection.insert_many(students)

# 1)
print("\nNew York-ში მცხოვრები სტუდენტები:")
for student in students_collection.find({"address.city": "New York"}):
    print(student)

# 2)
print("\nსტუდენტები, რომლებსაც ასაკი > 18:")
for student in students_collection.find({"age": {"$gt": 18}}):
    print(student)

# 3)
print("\nსტუდენტები, რომლებსაც აქვთ კურსი Math:")
for student in students_collection.find({"courses": "Math"}):
    print(student)

# 4)
count_A = students_collection.count_documents({"grade": "A"})
print(f"\nA შეფასების მქონე სტუდენტების რაოდენობა: {count_A}")

# 5)
print("\nLos Angeles-ში მცხოვრები და attendance >= 90 სტუდენტები:")
for student in students_collection.find({"address.city": "Los Angeles", "attendance": {"$gte": 90}}):
    print(student)

# 6)
students_collection.update_one({"name": "John Doe"}, {"$set": {"grade": "A"}})

# 7)
students_collection.update_many({}, {"$set": {"graduated": False}})

# 8)
students_collection.update_many(
    {"grade": "B"},
    {"$addToSet": {"courses": "English"}}
)

# 9)
students_collection.delete_one({"name": "Alice Smith"})

# 10)
students_collection.delete_many({"attendance": {"$lt": 60}})

print("\nოპერაციები დასრულდა.")
