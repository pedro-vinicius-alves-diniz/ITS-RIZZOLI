import random

mazzo = []
mazzo_mescolato = []

for i in range(40):
    i+=1 
    mazzo.append(i)

print(mazzo)

for i in range(40):
    i = random.randint(1, 40)

    while i in mazzo_mescolato:
        i = random.randint(1, 40)

    mazzo_mescolato.append(i)

print(mazzo_mescolato)