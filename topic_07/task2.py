class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"Студент: {self.name:<6} | Вік: {self.age}"


students = [
    Student("Ivan", 19),
    Student("Dima", 20),
    Student("Ilia", 18),
    Student("Vlad", 21),
    Student("Anna", 19),
]

sorted_by_name = sorted(students, key=lambda s: s.name)

print("--- Сортування студентів за ім'ям (lambda s: s.name) ---")
for st in sorted_by_name:
    print(st)

sorted_by_age = sorted(students, key=lambda s: s.age)

print("\n--- Сортування студентів за віком (lambda s: s.age) ---")
for st in sorted_by_age:
    print(st)