student = {"name": "Ivan", "group": "KB251", "course": 2}
print("Початковий словник:", student)

student.update({"age": 19, "city": "Chernihiv"})
print("1. update():", student)

print("2. keys():", list(student.keys()))

print("3. values():", list(student.values()))

print("4. items():", list(student.items()))

del student["city"]
print("5. del student['city']:", student)

student.clear()
print("6. clear():", student)