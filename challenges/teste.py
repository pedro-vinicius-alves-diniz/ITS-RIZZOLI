import random

mazzo = []
mazzoMescolato = []

for i in range(40):
    i+=1
    mazzo.append(i)

print(mazzo)

for i in range(40):
    mazzoMescolato.append(0)

for i in range(40):
    n = random.randint(1, 40)
    y = 0
    
    while y < 40:
        if mazzoMescolato[y] == n:
            n = random.randint(1, 40)
            y = 0
        else:
            y +=1


    mazzoMescolato[i] = n

print(mazzoMescolato)