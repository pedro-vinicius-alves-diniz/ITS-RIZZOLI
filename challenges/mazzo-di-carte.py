import random

mazzo = []
for i in range(40):
    i += 1
    mazzo.append(i)

print(f"Mazzo ordinato: {mazzo}\n")

cuori = mazzo[:10]
quadri = mazzo[10:20]
fiori = mazzo [20:30]
picche = mazzo[30:]
print(f"Cuori: {cuori}")
print(f"Quadri: {quadri}")
print(f"Fiori: {fiori}")
print(f"Picche: {picche}")

mazzo_mescolato = mazzo.copy()
mazzo_riordinato = []

indice = 0
n = 0



# MESCOLARE IL MAZZO
scelte1 = int(input("\nScegli un numero:\n1 -> Mescolare\n2 -> Exit\n\n"))

while scelte1 < 1 and scelte1 >2:
    print("\nDevi scegliere l'opzione 1 oppure 2.")
    scelte1 = int(input("Scegli un numero:\n1. Mescolare\n2.Exit\n\n"))

if scelte1 == 1:
    random.shuffle(mazzo_mescolato)
    print(f"\nMazzo mescolato con successo: {mazzo_mescolato}\n")
else:
    exit()


# RIORDINARE IL MAZZO
scelte2 = int(input("\nScegli un numero:\n1 -> Riordinare\n2 -> Exit\n\n"))
while scelte2 < 1 or scelte2 > 2:
    print("Devi scegliere l'opzione 1 oppure 2.")
    scelte2 = int(input("Scegli un numero:\n1 -> Riordinare\n2 -> Exit"))

if scelte2 == 1:
    for i in range(40):
        indice = 0
        i = mazzo_mescolato[indice]

        while i != mazzo[n]:
            indice += 1
            i = mazzo_mescolato[indice]

        mazzo_riordinato.append(i)
        n += 1

    print(f"\nMazzo riordinato riordinato con sucesso: {mazzo_riordinato}\n")
else:
    exit()










