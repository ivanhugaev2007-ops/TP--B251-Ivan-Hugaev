numbers = [3, 1, 4]
print("Початковий список:", numbers)

numbers.append(9)
print("1. append(9):", numbers)

numbers.extend([2, 5])
print("2. extend([2, 5]):", numbers)

numbers.insert(1, 7)
print("3. insert(1, 7):", numbers)

numbers.remove(4)
print("4. remove(4):", numbers)

numbers_copy = numbers.copy()
print("5. copy():", numbers_copy)

numbers.sort()
print("6. sort():", numbers)

numbers.reverse()
print("7. reverse():", numbers)

numbers.clear()
print("8. clear():", numbers)