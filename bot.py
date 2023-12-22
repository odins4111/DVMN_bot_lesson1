import requests
import time
import telegram
from dotenv import load_dotenv
import os
import argparse


def get_homework_status(token_tg, token_devman, chat_id):
    timestamp = ""
    url = "https://dvmn.org/api/long_polling/"
    headers = {"Authorization": token_devman}
    payload = {"timestamp": timestamp}
    response = requests.get(url, headers=headers, json=payload)
    response.raise_for_status()
    homeworks_roster = response.json()
    if homeworks_roster["status"] == "timeout":
        timestamp = homeworks_roster["timestamp_to_request"]
    elif homeworks_roster["new_attempts"][0]["is_negative"] == False:
        text_message = "У вас проверили работу - ({0}) \n\nПреподавателю все понравилось, можно приступать к следующему уроку!".format(
            homeworks_roster["new_attempts"][0]["lesson_title"]
        )
        strat_telegram_bot(text_message, token_tg, chat_id)
    else:
        text_message = "У вас проверили работу -{0}\n\nК сожалению, в работе нашлись ошибки".format(
            homeworks_roster["new_attempts"][0]["lesson_title"]
        )
        strat_telegram_bot(text_message, token_tg, chat_id)


def strat_telegram_bot(text_message, token_tg, chat_id):
    bot = telegram.Bot(token=token_tg)
    bot.send_message(chat_id=chat_id, text=text_message)


def main():
    load_dotenv()
    TOKEN_TG = os.environ["TOKEN_TG"]
    TOKEN_DEVMAN = os.environ["TOKEN_DEVMAN"]
    parser = argparse.ArgumentParser(
        description="Скрипт позволяет получать результаты провеки работ на сервисе dvmn.org"
    )
    parser.add_argument(
        "-id",
        help="id чата телаграм",
    )
    args = parser.parse_args()
    if args.id:
        try:
            while True:
                get_homework_status(TOKEN_TG, TOKEN_DEVMAN, args.id)
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass


if __name__ == "__main__":
    main()
