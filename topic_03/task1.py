def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):

    return x / y

while True:
    num1 = float(input("\nВведіть перше число: "))
    operation = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

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

    choice = input("\nБажаєте продовжити? (введіть 'q' для виходу, Enter — продовжити): ")
    if choice in ("q", "exit"):
        print("Роботу калькулятора завершено.")
        break