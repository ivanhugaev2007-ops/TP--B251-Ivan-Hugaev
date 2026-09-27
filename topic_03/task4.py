def find_insert_position(sorted_list, new_element):
    for index, value in enumerate(sorted_list):
        if value >= new_element:
            return index

    return len(sorted_list)


numbers = [10, 20, 30, 40, 50]
new_val = 25

pos = find_insert_position(numbers, new_val)
print("Відсортований список:", numbers)
print(f"Нове число: {new_val}")
print(f"Позиція для вставки: {pos}")

numbers.insert(pos, new_val)
print("Список після вставки:", numbers)