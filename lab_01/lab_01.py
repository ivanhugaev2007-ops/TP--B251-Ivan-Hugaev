globalList = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "KB-221"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@gmail.com", "group": "KB-221"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@gmail.com", "group": "KB-222"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@gmail.com", "group": "KB-222"}
]


def printAllList(listForPrinting):
    for item in listForPrinting:
        item_str = (f"Name = {item['name']}, "
                    f"Phone = {item['phone']}, "
                    f"Email = {item['email']}, "
                    f"Group = {item['group']}")
        print(item_str)


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
    return


def getElement():
    name = input("Please enter the name: ")
    phone = input("Please enter the phone: ")
    email = input("Please enter the email: ")
    group = input("Please enter the group: ")
    return {"name": name, "phone": phone, "email": email, "group": group}


def deleteElem(listForDel, name):
    indexForDel = findPosition(listForDel, name)
    if indexForDel < len(listForDel) and listForDel[indexForDel]["name"] == name:
        del listForDel[indexForDel]
        return True
    else:
        return False


def updateElement(listForUpdate):
    name = input("Please enter the name of the student to update: ")
    index = findPosition(listForUpdate, name)

    if index < len(listForUpdate) and listForUpdate[index]["name"] == name:
        old_elem = listForUpdate.pop(index)
        print(f"Updating data for {name} (leave empty to keep current value):")

        new_name = input(f"Enter new name [{old_elem['name']}]: ")
        new_phone = input(f"Enter new phone [{old_elem['phone']}]: ")
        new_email = input(f"Enter new email [{old_elem['email']}]: ")
        new_group = input(f"Enter new group [{old_elem['group']}]: ")

        updated_elem = {
            "name": new_name if new_name.strip() else old_elem["name"],
            "phone": new_phone if new_phone.strip() else old_elem["phone"],
            "email": new_email if new_email.strip() else old_elem["email"],
            "group": new_group if new_group.strip() else old_elem["group"]
        }

        addElemToSortedList(listForUpdate, updated_elem)
        print("Element has been successfully updated")
    else:
        print("Element hasn't been found")


def main():
    while True:
        chouse = input(
            "Please enter the command [C - add new elem, D - delete elem, P - print all List, U - update element, X - exit]: ")
        match chouse:
            case "C" | "c":
                newElem = getElement()
                addElemToSortedList(globalList, newElem)
                print("New element has been added")
            case "D" | "d":
                nameElemForDel = input("Please enter the name for delete: ")
                if deleteElem(globalList, nameElemForDel):
                    print("Element has been deleted")
                else:
                    print("Element hasn't been found")
            case "P" | "p":
                printAllList(globalList)
            case "U" | "u":
                updateElement(globalList)
            case "X" | "x":
                print("Exit")
                break
            case _:
                print("Wrong operation")


if __name__ == "__main__":
    main()
