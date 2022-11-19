# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:24:40 2022

@author: User
"""

from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = "5747445854:AAEOCummZWP5c99hWk6BkafsJB2Z0SYwHko "
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum. Xush kelibsiz?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    bot.reply_to(message, javob(msg))

bot.infinity_polling()


    