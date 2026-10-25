import random

def play_game():
    choices = ["камінь", "ножиці", "бумага"]

    user_choice = input("Введіть ваш вибір (камінь, ножиці, бумага) або 'q' для виходу: ").strip().lower()

    if user_choice == "q":
        return False

    if user_choice not in choices:
        print("Помилка: некоректний вибір! Оберіть: камінь, ножиці або бумага.")
        return True

    computer_choice = random.choice(choices)
    print(f"Вибір користувача: {user_choice}")
    print(f"Вибір комп'ютера:  {computer_choice}")

    if user_choice == computer_choice:
        print("Результат: Нічия!")
    elif (
        (user_choice == "камінь" and computer_choice == "ножиці") or
        (user_choice == "ножиці" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камінь")
    ):
        print("Результат: Ви перемогли!")
    else:
        print("Результат: Переміг комп'ютер!")

    return True

def main():
    print("--- Гра «Камінь, ножиці, папір» ---")
    while True:
        if not play_game():
            print("Дякуємо за гру!")
            break
        print("-" * 35)

if __name__ == "__main__":
    main()