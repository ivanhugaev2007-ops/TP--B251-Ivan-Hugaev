import re

PRIORITY = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
}


def to_rpn(expression: str) -> str:
    tokens = re.findall(r"\d+(?:\.\d+)?|[+\-*/^()]", expression)
    output = []
    stack = []

    for token in tokens:
        if re.match(r"^\d+(?:\.\d+)?$", token):
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Помилка: неузгоджені дужки у виразі!")
            stack.pop()
        elif token in PRIORITY:
            while (
                stack
                and stack[-1] != "("
                and (
                    (token != "^" and PRIORITY.get(stack[-1], 0) >= PRIORITY[token])
                    or (token == "^" and PRIORITY.get(stack[-1], 0) > PRIORITY[token])
                )
            ):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        op = stack.pop()
        if op in ("(", ")"):
            raise ValueError("Помилка: неузгоджені дужки у виразі!")
        output.append(op)

    return " ".join(output)


def calculate_rpn(rpn_expression: str) -> float:
    tokens = rpn_expression.split()
    stack = []

    for token in tokens:
        if re.match(r"^\d+(?:\.\d+)?$", token):
            stack.append(float(token))
        elif token in PRIORITY:
            if len(stack) < 2:
                raise ValueError("Помилка синтаксису: недостатньо операндів!")

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Помилка: ділення на нуль неможливе!")
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)

    if len(stack) != 1:
        raise ValueError("Помилка у структурі виразу!")

    return stack[0]


def main():
    print("=== Лабораторна робота №4: Зворотний польський запис ===")
    print("Підтримуються операції: +, -, *, /, ^ та круглі дужки ( )")
    print("Введіть 'exit' для завершення роботи.\n")

    while True:
        expr = input("Введіть математичний вираз: ").strip()
        if expr.lower() in ("exit", "q"):
            print("Роботу програми завершено.")
            break
        if not expr:
            continue

        try:
            rpn = to_rpn(expr)
            result = calculate_rpn(rpn)
            print(f"ЗПЗ: {rpn}")
            print(f"Результат: {result}\n")
        except (ValueError, ZeroDivisionError) as err:
            print(f"{err}\n")


if __name__ == "__main__":
    main()