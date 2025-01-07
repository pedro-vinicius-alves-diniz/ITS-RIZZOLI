# Creare una lista A di soli numeri interi e poi dividerli in due liste diverse chiamate PARI e DISPARI

import random as rd

"""

listaA = []
listaPari = []
listaDispari = []

for i in range(20):
    valore = rd.randint(0, 1000)
    while valore in listaA:
        valore = rd.randint(0, 1000)
    
    listaA.append(valore)

for i in listaA:
    if i % 2 == 0:
        listaPari.append(i)
    else:
        listaDispari.append(i)

print(listaA)
print(listaPari)
print(listaDispari)

"""

#########################################################################################################

# Creare due liste diverse a caso, Concatenare le due liste ordinandole in modo decrescente
"""

listaX = []
listaY = []

for i in range(10):
    X = rd.randint(0, 1000)
    Y = rd.randint(0, 1000)

    listaX.append(X)
    listaY.append(Y)

print(listaX)
print(listaY)

listaZ = listaX + listaY
listaZ.sort(reverse=True)
print(listaZ)

"""

#########################################################################################################

# Scambiare il primo e l'ultimo valore di una lista
"""
lista = []

for i in range(20):
    valore = rd.randint(0, 1000)
    lista.append(valore)

primo = lista[0]
ultimo = lista[-1]

print(lista)
print(primo)
print(ultimo)

lista[0] = ultimo
lista[-1] = primo
print("Lista modificata:", lista)

"""

#########################################################################################################

# Programma per leggere un elenco di parole e restituire la lunghezza del più lungo
from faker import Faker

"""
lista = []
lenn = []
fake = Faker()
indici = []

for i in range(20):
    parola = fake.word()
    while parola in lista:
        parola = fake.word()

    lista.append(parola)

for i in lista:
    lenn.append(len(i))


piulungo = max(lenn)

if lenn.count(piulungo) > 1:
        print("Ci sono più di una parola più lunghe")
else:
    print("C'è sono una parola più lunga")


for i, x in enumerate(lista):
    if len(x) == piulungo:
        indici.append(i)

print(indici)

if len(indici) > 1:
    print(f"Le parole più lunghe sono: ")
    for i in indici:
        print(lista[i])
else:
    print(f"La parola più lunga è '{lista[lenn.index(piulungo)]}'")
"""

#########################################################################################################

# Sia data una lista stampare l'indice dell'elemento 'SPTSX' e interrompre il ciclo

"""
indici = ['SPX','SX5E','NKY','UKX','SPTSX','AS51','SMI']

while True:
    for i in indici:
        if i == "SPTSX":
            print(indici.index(i))
            exit()
"""

#########################################################################################################

# Sia data una lista stampare l'indice di tutti gli elementi saltando l'indice dell'elemento 'SX5E' nella condizione
# e ritornare al for (continue)

"""
indici = ['SPX','SX5E','NKY','UKX','SPTSX','AS51','SMI']

for i in indici:
    if i != "SX5E":
        print(indici.index(i))
        
    print("continue")
"""

#########################################################################################################

'''ESERCIZIO: RANDOM
Generare 10000 numeri interi random compresi tra 0 e 1000000, stampare il numero generato più grande,
il numero generato più piccolo e la media dei numeri generati.'''

lista = []

for i in range(10000):
    valore = int(rd.randint(0,1000000))
    while valore in lista:
        valore = int(rd.randint(0,1000000))

    lista.append(valore)

print(f"Il massimo è: {max(lista)}")
print(f"Il minimo è: {min(lista)}")
print(f"La media dei numeri generati è: {round(sum(lista)/len(lista))}")
