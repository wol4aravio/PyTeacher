import os

import telebot

bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))


@bot.message_handler(commands=["start"])
def handle_command(message):
    bot.send_message(message.chat.id, "Hello, welcome to PyTeacher Bot!")


bot.polling()
