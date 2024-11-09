# 1Chiedere in input N numeri con N>= 5 e trovare si MIN che il MAX (se volete usare vettore per salvare numeri)

n = int(input("Quanti numeri vuoi inserire? "))

while n < 5:
    print("Devi inserire almeno 5 numeri. Riprova")
    n = int(input("Quanti numeri vuoi inserire? "))
    
numeri = []

for i in range(n):
    numeri.append(int(input("Insira un numero: ")))

massimo = max(numeri)
minimo = min(numeri)

print("Il massimo è:", massimo)
print("Il minimo è:", minimo)