from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging 

from telegram.ext import MessageHandler, Filters

updater = Updater(token='894268478:AAEkmO_QCIvNgmUGn-aReWFLSCxdyK-uvbI', use_context = True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="i'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
