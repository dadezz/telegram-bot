import random

with open ("bastiat.txt", "r") as file_bastiat:
    quote_bastiat = file_bastiat.read().splitlines()
    
def cita_bastiat ():
    lista = len(quote_bastiat)-1
    indice = random.randint(0, lista)
    return quote_bastiat[indice]

print(cita_bastiat())
