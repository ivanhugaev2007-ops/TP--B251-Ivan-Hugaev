import logging
from functions import get_number, get_operation
from operations import add, divide, multiply, subtract


logging.basicConfig(
    filename="calc.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)


def main():
    logging.info("Програма-калькулятор запущена.")
    ops_map = {"+": add, "-": subtract, "*": multiply, "/": divide}

    while True:
        op = get_operation()
        if op.lower() == "exit":
            logging.info("Роботу калькулятора завершено користувачем.")
            print("Вихід із програми.")
            break

        a = get_number("Введіть перше число: ")
        b = get_number("Введіть друге число: ")

        logging.info(f"Введені дані: a={a}, b={b}, операція='{op}'")

        try:
            result = ops_map[op](a, b)
            logging.info(f"Результат операції: {a} {op} {b} = {result}")
            print(f"Результат: {result}\n")
        except ZeroDivisionError as err:
            logging.error(f"Помилка ділення: {a} {op} {b} -> {err}")
            print(f"Помилка: {err}\n")


if __name__ == "__main__":
    main()