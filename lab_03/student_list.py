from student import Student


class StudentList:
    def __init__(self):
        self.students: list[Student] = []

    def find_position(self, name: str) -> int:
        index = 0
        for item in self.students:
            if item.name < name:
                index += 1
            else:
                break
        return index

    def add_student(self, student: Student) -> None:
        pos = self.find_position(student.name)
        self.students.insert(pos, student)

    def delete_student(self, name: str) -> bool:
        pos = self.find_position(name)
        if pos < len(self.students) and self.students[pos].name == name:
            del self.students[pos]
            return True
        return False

    def update_student(self, name: str, new_name: str = "", new_phone: str = "", new_email: str = "", new_group: str = "") -> bool:
        pos = self.find_position(name)
        if pos < len(self.students) and self.students[pos].name == name:
            old = self.students.pop(pos)
            updated = Student(
                name=new_name if new_name else old.name,
                phone=new_phone if new_phone else old.phone,
                email=new_email if new_email else old.email,
                group=new_group if new_group else old.group,
            )
            self.add_student(updated)
            return True
        return False

    def print_all(self) -> None:
        if not self.students:
            print("Список порожній.")
            return
        for s in self.students:
            print(s)

    def __len__(self) -> int:
        return len(self.students)