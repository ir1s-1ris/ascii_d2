from telegram.ext import Updater
import logging 

updater = Updater(token='894268478:AAEkmO_QCIvNgmUGn-aReWFLSCxdyK-uvbI', use_context = True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
	context.bot.send_message(chat_id=update.essage.chat_id, text="i'm a bot, please talk to me!")

updater.start_polling()
