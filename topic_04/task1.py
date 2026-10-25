def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Помилка: ділення на нуль неможливе!"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено не число! Спробуйте ще раз.")

while True:
    num1 = get_number("\nВведіть перше число: ")
    operation = input("Введіть операцію (+, -, *, /): ").strip()
    num2 = get_number("Введіть друге число: ")

    match operation:
        case "+":
            print("Результат:", add(num1, num2))
        case "-":
            print("Результат:", sub(num1, num2))
        case "*":
            print("Результат:", mult(num1, num2))
        case "/":
            print("Результат:", div(num1, num2))
        case _:
            print("Помилка: невідома операція!")

    choice = input("\nБажаєте продовжити? (введіть 'q' для виходу, Enter — продовжити): ").strip().lower()
    if choice in ("q", "exit"):
        print("Роботу калькулятора завершено.")
        break