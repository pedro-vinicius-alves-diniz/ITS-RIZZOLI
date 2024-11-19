import random

mazzo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print(f"Mazzo ordinato: {mazzo}\n")

cuori = mazzo[:10]
quadri = mazzo[10:20]
fiori = mazzo [20:30]
picche = mazzo[30:]

mazzo_mescolato = []
mazzo_riordinato = []

indice = 0
n = 0

# MESCOLARE IL MAZZO
mazzo_mescolato = random.shuffle(mazzo)

for i in range(40):
    i = random.choice(mazzo)

    while i in mazzo_mescolato:
        i = random.choice(mazzo)

    mazzo_mescolato.append(i)

print(f"Mazzo mescolato: {mazzo_mescolato}\n")

# RIORDINARE IL MAZZO
for i in range(40):
    indice = 0
    
    i = mazzo_mescolato[indice]

    while i != mazzo[n]:
        indice += 1
        i = mazzo_mescolato[indice]

    mazzo_riordinato.append(i)
    n += 1

print(f"Mazzo riordinato: {mazzo_riordinato}\n")

print(f"Cuori sono {cuori}\n")
print(f"Quadri sono {quadri}\n")
print(f"Fiori sono {fiori}\n")
print(f"Picche sono {picche}")








