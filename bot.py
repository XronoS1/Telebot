from datetime import datetime
from pycbrf.toolbox import ExchangeRates
import telebot
from telebot import types
bot = telebot.TeleBot("2109414517:AAEE9FOgM1km0yK__7a9lmod4hk7SRsRMS4")



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.row("/help", "USD", "EUR")
    bot.send_message(message.chat.id, 'Привет! Выбери валюту, чтобы узнать ее цену!', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею показывать курс Доллара и Евро')


@bot.message_handler(content_types=['text'])
def answer(message):
    rates = ExchangeRates(datetime.now())
    if message.text == 'USD':
        bot.send_message(message.from_user.id, text=f"Цена USD составляет {float(rates['USD'].value)}")
    elif message.text == 'EUR':
        bot.send_message(message.from_user.id, text=f"Цена EUR составляет {float(rates['EUR'].value)}")

    else:
        bot.send_message(message.chat.id, 'У меня нет такой информации')


bot.polling(none_stop=True, interval=0)

