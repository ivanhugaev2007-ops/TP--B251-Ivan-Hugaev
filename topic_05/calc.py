import functions
import operations

def main():
    while True:
        num1 = operations.get_number("\nВведіть перше число: ")
        op = operations.get_operation()
        num2 = operations.get_number("Введіть друге число: ")

        match op:
            case "+":
                result = functions.add(num1, num2)
            case "-":
                result = functions.sub(num1, num2)
            case "*":
                result = functions.mult(num1, num2)
            case "/":
                result = functions.div(num1, num2)

        print("Результат:", result)

        if not operations.get_continue_choice():
            print("Роботу калькулятора завершено.")
            break

if __name__ == "__main__":
    main()