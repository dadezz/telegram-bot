import random

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
