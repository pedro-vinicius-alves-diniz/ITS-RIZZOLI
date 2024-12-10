# Creare una lista A di soli numeri interi e poi dividerli in due liste diverse chiamate PARI e DISPARI

import random as rd
import faker
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

# Programma per leggere un elenco di parole e restituire la lunghezza del più lungo
lista = []
fake = faker()

for i in range(20):
    parola = fake