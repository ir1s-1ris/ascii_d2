from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging 

from telegram.ext import MessageHandler, Filters

from telegram import InlineQueryResultArticle, InputTextMessageContent

from telegram.ext import InlineQueryHandler




#token
updater = Updater(token='894268478:AAEkmO_QCIvNgmUGn-aReWFLSCxdyK-uvbI', use_context = True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#commanda start
def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="i'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#otvev bota echo
def echo(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

#obrabotka komandi /caps 'message'
def caps(update, context):
	text_caps = ' '.join(context.args).upper()
	context.bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

#Obrabotka inline zaprosov
def inline_caps(update, context):
	query = update.inline_query.query
	if not query:
		return
	results = list()
	results.append(
		InlineQueryResultArticle(
			id=query.upper(),
			title='Caps',
			input_message_content=InputTextMessageContent(query.upper())
			)
		)
	context.bot.answer_inline_query(update.inline_query.id, results)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling()
