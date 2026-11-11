students = [
    {"name": "Ivan", "grade": 92},
    {"name": "Dima", "grade": 75},
    {"name": "Ilia", "grade": 88},
    {"name": "Vlad", "grade": 64},
    {"name": "Anna", "grade": 95},
]

sorted_by_name = sorted(students, key=lambda student: student["name"])

print("--- Сортування за ім'ям ---")
for s in sorted_by_name:
    print(f"Ім'я: {s['name']:5} | Оцінка: {s['grade']}")

students.sort(key=lambda student: student["grade"])

print("\n--- Сортування за оцінкою(за зростанням) ---")
for s in students:
    print(f"Ім'я: {s['name']:5} | Оцінка: {s['grade']}")