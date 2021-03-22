import os

import requests
import telebot

from pyteacher.bot_tools import parse_register_message
from pyteacher.models import User

bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))


@bot.message_handler(commands=["start"])
def handle_command_start(message):
    bot.send_message(message.chat.id, "Hello, welcome to PyTeacher Bot!")


@bot.message_handler(commands=["register"])
def handle_command_register(message):
    repo_url = parse_register_message(message.text)
    if repo_url is None:
        bot.send_message(message.chat.id, "No repo provided")
    user = User(telegram_user_id=message.from_user.id, repo_url=repo_url)
    response = requests.post("http://pyteacher_api:8000/register", data=user.dict())
    if response.ok:
        bot.send_message(message.chat.id, "Successfully registered!")
    else:
        bot.send_message(message.chat.id, "Smth went wrong. Try again later")


bot.polling()
