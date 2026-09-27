def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, *, /): ").strip()
num2 = float(input("Введіть друге число: "))

if operation == "+":
    print("Результат:", add(num1, num2))
elif operation == "-":
    print("Результат:", sub(num1, num2))
elif operation == "*":
    print("Результат:", mult(num1, num2))
elif operation == "/":
    print("Результат:", div(num1, num2))
else:
    print("Помилка: невідома операція!")