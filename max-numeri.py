# Dati tre numeri in input trovare il maggiore

# PRIMO MODO DI INPUT
a = float(input("Inserire il valore di a: "))
b = float(input("Inserire il valore di b: "))
c = float(input("Inserire il valore di c: "))

# SECONDO MODO DI INPUT
a, b, c = map(float, input('Insirire i valori di a, b e c: ').split())


print(a, b, c)
print("O maior número é o:", max(a, b, c))

#TERZO MODO DI INPUT
numeri = []

for i in range(3):
    i = float(input("Inserie un valore"))

    numeri.append(i)

print("Il maggiore numero è", max(numeri))