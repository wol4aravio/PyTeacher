import os

import telebot

bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))


@bot.message_handler(commands=["start"])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to PyTeacher Bot!")


bot.polling()
