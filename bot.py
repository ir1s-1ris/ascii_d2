import telebot

bot = telebot.TeleBot("894268478:AAEkmO_QCIvNgmUGn-aReWFLSCxdyK-uvbI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

user = tb.get_me()

bot.polling()