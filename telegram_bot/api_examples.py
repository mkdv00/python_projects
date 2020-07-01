# coding: utf-8
import telebot
import random
import time
from dates_bot import *
from horoscope import generate_prophecies

bot = telebot.TeleBot('1163507099:AAH6JWVFT8PY3g-Gtf9L3lTiFjr-b4Qgrg0')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Гороскоп')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

# Text for bot
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        hello_answer = get_hello_answer()
        bot.send_message(message.chat.id, random.choice(hello_answer))
    elif message.text.lower() == 'пока':
        bye_answer = get_bye_answer()
        bot.send_message(message.chat.id, random.choice(bye_answer))
    elif message.text.lower() == 'я тебя люблю':
        love_answer = get_love_answer()
        bot.send_message(message.chat.id, random.choice(love_answer))
    elif message.text.lower() == 'как дела?' or message.text.lower() == 'как дела':
        how_are_you_answer = get_how_are_you_answer()
        bot.send_message(message.chat.id, random.choice(how_are_you_answer))
    elif message.text.lower() == 'хорошо' or message.text.lower() == 'отлично':
        good_answer = get_good_answer()
        bot.send_message(message.chat.id, random.choice(good_answer))
    elif message.text.lower() == 'что делаешь?' or message.text.lower() == 'что делаешь':
        what_are_you_doing_answer = get_what_are_you_doing_answer()
        bot.send_message(message.chat.id, random.choice(what_are_you_doing_answer))
    elif message.text.lower() == 'ты тупой' or message.text.lower() == 'ты глупый':
        bad_words_answer = get_bad_words_answer()
        bot.send_message(message.chat.id, random.choice(bad_words_answer))
    elif message.text.lower() == 'гороскоп':
        prophecies = generate_prophecies()
        bot.send_message(message.chat.id, prophecies)
    else:
        do_not_understand_words = get_answer_do_not_understand()
        bot.send_message(message.chat.id, random.choice(do_not_understand_words))


@bot.message_handler(content_types=['sticker'])
def start_sticker(message):
    print(message)


bot.polling()
