class CalculatorFunctions:
    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Помилка! Введіть дійсне число.")

    def get_operation(self, allowed_ops):
        while True:
            op = input("Оберіть операцію (+, -, *, /) або 'exit' для виходу: ").strip()
            if op.lower() == "exit" or op in allowed_ops:
                return op
            print("Невідома операція! Спробуйте ще раз.")