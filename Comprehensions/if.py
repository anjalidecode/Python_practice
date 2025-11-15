people = [
    {"name": "Alice", "age": 28, "status": "single"},
    {"name": "Bob", "age": 32, "status": "married"},
    {"name": "Charlie", "age": 23, "status": "single"},
    {"name": "David", "age": 30, "status": "single"},

]

invited_guests = [person["name"] for person in people if person["age"] >= 25 and person["status"] =="single" ]
print(invited_guests)