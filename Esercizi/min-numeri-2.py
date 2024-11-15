numeri = []

n = int(input("Quanti numeri vorresti inserire? "))

while n < 2:
    print("La quantità minima di numeri inserite è 2")
    n = int(input("Quanti numeri vorresti inserire? "))

for i in range(n -1):
    i = float(input("Inserisce un valore "))

    numeri.append(i)

min = min(numeri)
print("Il minore numero è", min)