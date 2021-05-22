person = {
    "name": "Alice Johnson",
    "age": 28,
    "city": "New York",
    "occupation": "Software Engineer",
    "skills": ["Python", "JavaScript", "Machine Learning"],
    "is_employed": True
}

# print(list(person))
# print(person.keys())
# print(person.values())
# print(person.items())
for item, key in person.items():
    print(item, key)