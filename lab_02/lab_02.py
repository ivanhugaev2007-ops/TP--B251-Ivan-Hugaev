import csv
import sys


def findPosition(listForFinding, nameForFinding):
    index = 0
    for item in listForFinding:
        if item["name"] < nameForFinding:
            index += 1
        else:
            break
    return index


def addElemToSortedList(listForAdd, newElem):
    positionForInsert = findPosition(listForAdd, newElem["name"])
    listForAdd.insert(positionForInsert, newElem)


def load_from_csv(file_name):
    students_list = []
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "name": row["name"],
                    "phone": row["phone"],
                    "email": row["email"],
                    "group": row["group"],
                }
                addElemToSortedList(students_list, student)
        return students_list
    except FileNotFoundError:
        print(f"Помилка: файл '{file_name}' не знайдено! Створено порожній список.")
        return []


def save_to_csv(file_name, students_list):
    fieldnames = ["name", "phone", "email", "group"]
    with open(file_name, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students_list:
            writer.writerow(student)
    print(f"Дані успішно збережено у файл '{file_name}'.")


def printAllList(listForPrinting):
    if not listForPrinting:
        print("Список порожній.")
        return
    for item in listForPrinting:
        item_str = (
            f"Name = {item['name']}, "
            f"Phone = {item['phone']}, "
            f"Email = {item['email']}, "
            f"Group = {item['group']}"
        )
        print(item_str)


def getElement():
    name = input("Please enter the name: ").strip()
    phone = input("Please enter the phone: ").strip()
    email = input("Please enter the email: ").strip()
    group = input("Please enter the group: ").strip()
    return {"name": name, "phone": phone, "email": email, "group": group}


def deleteElem(listForDel, name):
    indexForDel = findPosition(listForDel, name)
    if indexForDel < len(listForDel) and listForDel[indexForDel]["name"] == name:
        del listForDel[indexForDel]
        return True
    return False


def updateElement(listForUpdate):
    name = input("Please enter the name of the student to update: ").strip()
    index = findPosition(listForUpdate, name)
    if index < len(listForUpdate) and listForUpdate[index]["name"] == name:
        old_elem = listForUpdate.pop(index)
        print(f"Updating data for {name} (leave empty to keep current value):")
        new_name = input(f"Enter new name [{old_elem['name']}]: ").strip()
        new_phone = input(f"Enter new phone [{old_elem['phone']}]: ").strip()
        new_email = input(f"Enter new email [{old_elem['email']}]: ").strip()
        new_group = input(f"Enter new group [{old_elem['group']}]: ").strip()

        updated_elem = {
            "name": new_name if new_name else old_elem["name"],
            "phone": new_phone if new_phone else old_elem["phone"],
            "email": new_email if new_email else old_elem["email"],
            "group": new_group if new_group else old_elem["group"],
        }
        addElemToSortedList(listForUpdate, updated_elem)
        print("Element has been successfully updated")
    else:
        print("Element hasn't been found")


def main():
    if len(sys.argv) < 2:
        print("Помилка: не вказано CSV-файл для завантаження!")
        print("Використання: python lab_02.py <ім'я_файлу.csv>")
        return

    csv_file_name = sys.argv[1]
    globalList = load_from_csv(csv_file_name)

    print("\n--- Завантажений список студентів із файлу ---")
    printAllList(globalList)
    print("---------------------------------------------\n")

    while True:
        choice = input(
            "Please enter the command [C - add new elem, D - delete elem, P - print all List, U - update element, X - exit]: "
        ).strip()

        match choice:
            case "C" | "c":
                newElem = getElement()
                addElemToSortedList(globalList, newElem)
                print("New element has been added")
            case "D" | "d":
                nameElemForDel = input("Please enter the name for delete: ").strip()
                if deleteElem(globalList, nameElemForDel):
                    print("Element has been deleted")
                else:
                    print("Element hasn't been found")
            case "P" | "p":
                printAllList(globalList)
            case "U" | "u":
                updateElement(globalList)
            case "X" | "x":
                save_to_csv(csv_file_name, globalList)
                print("Exit")
                break
            case _:
                print("Wrong operation")


if __name__ == "__main__":
    main()