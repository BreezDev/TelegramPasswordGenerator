import random
import telebot
from telebot import types

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

def generate_password(message):
    words = message.text.split()
    password = "".join(random.sample(words, len(words)))
    bot.send_message(message.chat.id, f"Your generated password is: {password}")

@bot.message_handler(commands=['generate'])
def generate(message):
    bot.send_message(message.chat.id, "Please enter some words to use for your password.")
    bot.register_next_step_handler(message, generate_password)

bot.polling()
