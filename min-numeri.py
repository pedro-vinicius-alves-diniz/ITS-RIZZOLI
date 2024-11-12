# Dati quatro numeri in input trovare il minore

numeri = []

for i in range(4):
    i = float(input("Inserisce un valore "))

    numeri.append(i)

min = min(numeri)
print("Il valore minimo tra i quattri numeri è", min)

