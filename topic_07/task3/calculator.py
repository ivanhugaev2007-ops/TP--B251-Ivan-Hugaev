from operations import Operations
from functions import CalculatorFunctions


class Calculator:
    def __init__(self):
        self.ops = Operations()
        self.ui = CalculatorFunctions()
        self.actions = {
            "+": self.ops.add,
            "-": self.ops.subtract,
            "*": self.ops.multiply,
            "/": self.ops.divide,
        }

    def run(self):
        print("--- ООП Калькулятор запущено ---")
        while True:
            op = self.ui.get_operation(self.actions.keys())
            if op.lower() == "exit":
                print("Вихід із програми.")
                break

            a = self.ui.get_number("Введіть перше число: ")
            b = self.ui.get_number("Введіть друге число: ")

            try:
                result = self.actions[op](a, b)
                print(f"Результат: {a} {op} {b} = {result}\n")
            except ZeroDivisionError as err:
                print(f"Помилка: {err}\n")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()