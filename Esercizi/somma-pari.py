somma = 0

for i in range(10):
    i = int(input("Inserisci un numero intero: "))

    if i%2 == 0:
        somma += i

print(somma)