def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка! Введіть коректне число.")


def get_operation():
    operations = ["+", "-", "*", "/"]
    while True:
        op = input("Оберіть операцію (+, -, *, /) або 'exit' для виходу: ").strip()
        if op.lower() == "exit" or op in operations:
            return op
        print("Невідома операція! Спробуйте ще раз.")