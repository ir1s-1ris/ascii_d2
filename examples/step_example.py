# -*- coding: utf-8 -*-
"""
This Example will show you how to use register_next_step handler.
"""

import telebot
from telebot import types

API_TOKEN = '894268478:AAEkmO_QCIvNgmUGn-aReWFLSCxdyK-uvbI'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None

location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
custom_keyboard = [[ location_keyboard, contact_keyboard ]]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
bot.send_message(chat_id=chat_id, 
...                  text="Would you mind sharing your location and contact with me?", 
...                  reply_markup=reply_markup)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am Example bot.
What's your name?
""")
    bot.register_next_step_handler(msg, process_name_step)

location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
custom_keyboard = [[ location_keyboard, contact_keyboard ]]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
bot.send_message(chat_id=chat_id, 
...                  text="Would you mind sharing your location and contact with me?", 
...                  reply_markup=reply_markup)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'How old are you?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Age should be a number. How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Male') or (sex == u'Female'):
            user.sex = sex
        else:
            raise Exception()
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
    except Exception as e:
        bot.reply_to(message, 'oooops')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling()
