#pip install python-telegram-bot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import genfromtxt

TOKEN="token"

def bastiat(update, context):
     frase = genfromtxt.cita_bastiat()
     update.message.reply_text(f'{frase}')

def mises(update, context):
     frase = genfromtxt.cita_mises()
     update.message.reply_text(f'{frase}')

def main():
     upd= Updater(TOKEN, use_context=True)
     disp=upd.dispatcher
     disp.add_handler(CommandHandler("bastiat", bastiat))
     disp.add_handler(CommandHandler("mises", mises))
     upd.start_polling()
     upd.idle()

if __name__=='__main__':
     main()
