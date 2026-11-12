import sys
from student import Student
from file_manager import FileManager


def get_element_input() -> Student:
    name = input("Please enter the name: ").strip()
    phone = input("Please enter the phone: ").strip()
    email = input("Please enter the email: ").strip()
    group = input("Please enter the group: ").strip()
    return Student(name, phone, email, group)


def main():
    if len(sys.argv) < 2:
        print("Помилка: не вказано CSV-файл для завантаження!")
        print("Використання: python lab_03.py <ім'я_файлу.csv>")
        return

    csv_file_name = sys.argv[1]
    group_list = FileManager.load_from_csv(csv_file_name)

    print("\n--- Завантажений список студентів із файлу ---")
    group_list.print_all()
    print("---------------------------------------------\n")

    while True:
        choice = input(
            "Please enter the command [C - add new elem, D - delete elem, P - print all List, U - update element, X - exit]: "
        ).strip()

        match choice:
            case "C" | "c":
                new_student = get_element_input()
                group_list.add_student(new_student)
                print("New element has been added")
            case "D" | "d":
                name = input("Please enter the name for delete: ").strip()
                if group_list.delete_student(name):
                    print("Element has been deleted")
                else:
                    print("Element hasn't been found")
            case "P" | "p":
                group_list.print_all()
            case "U" | "u":
                name = input("Please enter the name of the student to update: ").strip()
                pos = group_list.find_position(name)
                if pos < len(group_list) and group_list.students[pos].name == name:
                    old = group_list.students[pos]
                    print(f"Updating data for {name} (leave empty to keep current value):")
                    new_name = input(f"Enter new name [{old.name}]: ").strip()
                    new_phone = input(f"Enter new phone [{old.phone}]: ").strip()
                    new_email = input(f"Enter new email [{old.email}]: ").strip()
                    new_group = input(f"Enter new group [{old.group}]: ").strip()
                    group_list.update_student(name, new_name, new_phone, new_email, new_group)
                    print("Element has been successfully updated")
                else:
                    print("Element hasn't been found")
            case "X" | "x":
                FileManager.save_to_csv(csv_file_name, group_list)
                print("Exit")
                break
            case _:
                print("Wrong operation")


if __name__ == "__main__":
    main()