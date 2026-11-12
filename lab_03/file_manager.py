import csv
from student import Student
from student_list import StudentList


class FileManager:
    @staticmethod
    def load_from_csv(file_name: str) -> StudentList:
        student_list = StudentList()
        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name=row["name"],
                        phone=row["phone"],
                        email=row["email"],
                        group=row["group"],
                    )
                    student_list.add_student(student)
            return student_list
        except FileNotFoundError:
            print(f"Помилка: файл '{file_name}' не знайдено! Створено порожній список.")
            return student_list

    @staticmethod
    def save_to_csv(file_name: str, student_list: StudentList) -> None:
        fieldnames = ["name", "phone", "email", "group"]
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list.students:
                writer.writerow(student.to_dict())
        print(f"Дані успішно збережено у файл '{file_name}'.")