import requests

def get_exchange_rate(valcode):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data:
            return data[0]["rate"]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Помилка мережі при запиті до API НБУ: {e}")
        return None

def convert_currency():
    allowed_currencies = ("USD", "EUR", "PLN")

    currency = input("Введіть тип валюти (USD, EUR, PLN): ").strip().upper()
    if currency not in allowed_currencies:
        print(f"Помилка: валюта '{currency}' не підтримується! Доступні: USD, EUR, PLN")
        return

    try:
        amount = float(input(f"Введіть кількість {currency}: "))
        if amount < 0:
            print("Помилка: сума не може бути від'ємною!")
            return
    except ValueError:
        print("Помилка (ValueError): необхідно ввести числове значення суми!")
        return

    rate = get_exchange_rate(currency)
    if rate is not None:
        uah_result = amount * rate
        print(f"Офіційний курс {currency}/UAH від НБУ: {rate:.4f} грн")
        print(f"Результат: {amount} {currency} = {uah_result:.2f} UAH")
    else:
        print("Не вдалося отримати курс валют від сервера НБУ.")

def main():
    print("--- Конвертер іноземної валюти в UAH (за курсом НБУ) ---")
    convert_currency()

if __name__ == "__main__":
    main()