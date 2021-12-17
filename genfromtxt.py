import random

citazioni_varie = {}

def cita_bastiat ():
     with open ("bastiat.txt", "r") as file_bastiat:
          quote_bastiat = file_bastiat.read().splitlines() 
     lista = len(quote_bastiat)-1
     indice = random.randint(0, lista)
     return quote_bastiat[indice]

def cita_mises ():
     with open ("mises.txt", "r") as file_mises:
          quote_mises = file_mises.read().splitlines() 
     lista = len(quote_mises)-1
     indice = random.randint(0, lista)
     return quote_mises[indice]

def aggiungi_cit(stringa):
     stringa_scritta = stringa[0].split(" ", 1)
     citazione = str(stringa_scritta[1])
     nome = str(stringa[1])
     if nome in citazioni_varie:
         risposta = "occupato"
         return risposta
     else:
         citazioni_varie[nome] = citazione
         return citazioni_varie[nome]
     
def la_mia_cit(messaggio):
    try:
        provv = messaggio.split(" ", 1)
        comando = provv[1]
        if comando in citazioni_varie:
            return "'"+citazioni_varie[comando]+"'"
        else:
            return "errore1"
    except:
        return "errore2"
