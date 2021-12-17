#pip install python-telegram-bot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import genfromtxt

TOKEN="token"
     
def nuovacit(update, contest):
     text = update.message.text
     try:
          stringa = text.split(" - ", 1)
          nuova_citazione = genfromtxt.aggiungi_cit(stringa)
          if nuova_citazione == "occupato":
               update.message.reply_text("mi spiace, comando gia' associato a una citazione")
          else:
               risposta = "Nuova citazione registrata:\n\n '%s'" %nuova_citazione
               update.message.reply_text(risposta)
     except:
          update.message.reply_text("qualcosa non va, prova a controllare cosa hai scritto:\
deve essere nella forma 'citazione - comando per richiamarla'")
          
def citami(update, context):
     messaggio = update.message.text
     risposta = genfromtxt.la_mia_cit(messaggio)
     if risposta == "errore1":
          update.message.reply_text("qualcosa non va, probabilmente il comando non esiste,\
o hai scritto male o si è cancellato in un bug, per cui devi reimpostarlo")
     elif risposta == "errore2":
          update.message.reply_text("qualcosa non va, prova a controllare cosa hai scritto:\
deve essere nella forma '/citami@Bastiat_Bot comando'")
     else:
          update.message.reply_text(risposta)
     
def bastiat(update, context):
     frase = genfromtxt.cita_bastiat()
     update.message.reply_text(f'{frase}')

def mises(update, context):
     frase = genfromtxt.cita_mises()
     update.message.reply_text(f'{frase}')

def aiuto(update, contest):
     testo_aiuto = "1. Per inviare una citazione random di un autore austriaco basta mandare un messaggio nella forma '/autore'\n\
Gli autori attualmente supportati sono solo mises e bastiat, rispettivamente /mises e /bastiat\n\n2. Per aggiungere una citazione personalizzata \
il messaggio deve essere così impostato: '/nuovacit citazione - comando per richiamarla'. Ad esempio: \n'/nuovacit no al baratto della \
libertà con ordine - Mattarella 25/4/19'.\nSe tutto va bene, verrà registrata. Una volta fatto ciò, per ricevere quella citazione come messaggio \
basterà usare il comando '/citami comando per richiamarla', tornando all'esempio di prima: '/citami Mattarella 25/4/19'\n\n\
Questo è quanto. Al momento le citazioni personalizzate sono salvate in RAM, quindi in caso di crash del bot verranno perse. Inoltre, una volta registrata \
la citazione personalizzata, essa non potrà essere né cancellata né modificata. Non preoccuparti, in futuro mi impegnerò a sistemare entrambi i problemi"
     update.message.reply_text(testo_aiuto)

def main():
     upd = Updater(TOKEN, use_context=True)
     disp = upd.dispatcher
     disp.add_handler(CommandHandler("bastiat", bastiat))
     disp.add_handler(CommandHandler("mises", mises))
     disp.add_handler(CommandHandler("nuovacit", nuovacit))
     disp.add_handler(CommandHandler("citami", citami))
     disp.add_handler(CommandHandler("help", aiuto))
     upd.start_polling()
     upd.idle()

if __name__=='__main__':
     main()
