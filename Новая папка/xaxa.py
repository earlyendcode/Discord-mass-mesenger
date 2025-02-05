import requests
import json
import time
from colorama import Fore, Style
import os

print(Fore.RED + Style.BRIGHT + r'''
          _____                ____        _   
         |_   _| __ _   _  ___| __ )  ___ | |_ 
           | || '__| | | |/ _ \  _ \ / _ \| __|
           | || |  | |_| |  __/ |_) | (_) | |_ 
           |_||_|   \__,_|\___|____/ \___/ \__|



                                                                by.xaoc
''' + Style.RESET_ALL)


def load_tokens(filename):
    try:
        with open(filename, 'r') as file:
            tokens = [line.strip() for line in file.readlines()]
            time.sleep(2)
            print(
                Fore.GREEN + f"========== ╚ Найдено {len(tokens)} Токенов ╝ ==========" + Fore.RESET)
            return tokens
    except FileNotFoundError:
        print(Fore.YELLOW + "Файл с токенами не найден. Убедитесь, что 'token.txt' существует." + Fore.RESET)
        return []


def get_friends(token):
    url = "https://discord.com/api/v9/users/@me/relationships"
    headers = {
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(Fore.RED + f"Ошибка при получении друзей: {response.status_code}, {response.text}" + Fore.RESET)
        return []


def send_message(token, recipient_id, message):
    try:
        url = "https://discord.com/api/v9/users/@me/channels"
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }
        payload = {"recipient_id": recipient_id}

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            channel_id = response.json().get("id")
            message_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
            message_payload = {"content": message}
            message_response = requests.post(message_url, headers=headers, json=message_payload)

            if message_response.status_code == 200:
                print(Fore.GREEN + f"Сообщение успешно отправлено пользователю с ID {recipient_id}." + Fore.RESET)
            elif message_response.status_code == 429:
                print(Fore.YELLOW + "Превышение лимита скорости. Ожидание..." + Fore.RESET)
                time.sleep(int(message_response.headers.get("Retry-After", 1)))
                return send_message(token, recipient_id, message)
            else:
                print(
                    Fore.RED + f"Ошибка при отправке сообщения: {message_response.status_code}, {message_response.text}" + Fore.RESET)
                raise Exception("Ошибка при отправке сообщения.")
        else:
            print(Fore.RED + f"Ошибка при создании канала: {response.status_code}, {response.text}" + Fore.RESET)
            raise Exception("Ошибка при создании канала.")
    except Exception as e:
        print(Fore.RED + f"Непредвиденная ошибка: {e}" + Fore.RESET)
        return False
    return True


def greet_friends(token, message, delay):
    friends = get_friends(token)
    if not friends:
        print(Fore.YELLOW + "У пользователя нет друзей или возникла ошибка при их получении." + Fore.RESET)
        return

    for friend in friends:
        if friend['type'] == 1:
            recipient_id = friend['id']
            if not send_message(token, recipient_id, message):
                print(Fore.YELLOW + "Перехожу к следующему токену..." + Fore.RESET)
                break


def main():
    tokens = load_tokens("token.txt")
    if not tokens:
        return
    message = input("Введите текст для спама: ")
    try:
        rate_limit = float(
            input("Введите задержку между сообщениями (в секундах, от 1 до 10): "))
        if rate_limit < 5 or rate_limit > 10:
            print(Fore.YELLOW + "Рекомендуется установить задержку между 5 и 10 секундами." + Fore.RESET)
    except ValueError:
        print(Fore.RED + "Ошибка: Введите число в формате секунд (например, 5.0)." + Fore.RESET)
        return

    for token in tokens:
        print(Fore.MAGENTA + f"Использую токен: {token}" + Fore.RESET)
        greet_friends(token, message, rate_limit)


if __name__ == "__main__":
    main()
