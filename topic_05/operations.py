def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка (ValueError): введіть коректне число!")

def get_operation():
    valid_ops = ("+", "-", "*", "/")
    while True:
        op = input("Введіть операцію (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print(f"Помилка: невідома дія '{op}'! Доступні: +, -, *, /")

def get_continue_choice():
    choice = input("\nБажаєте продовжити? ('q' для виходу, Enter — продовжити): ").strip().lower()
    return choice not in ("q", "exit")