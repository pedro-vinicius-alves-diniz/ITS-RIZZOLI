# MODO DI QUANTITÀ DI NUMERII INSERITE IN MANIERA DINAMICA

numeri = []

n = int(input("Quanti numeri vorresti inserire?"))

while n < 2:
    n = int(input("Quanti numeri vorresti inserire?"))
    
for i in range(n - 1):
    i = float(input("Inserire un valore"))

    numeri.append(i)

max = max(numeri)
print(max)