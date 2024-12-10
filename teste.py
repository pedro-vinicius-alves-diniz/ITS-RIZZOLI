# for i in range(20):
#     valore= input("Inserisci un numero pare: ").lower()

#     if valore == "fine":
#         print("Finito")
#         exit()


while True:
    try:
        a = int(input("Inserisice un numero: "))
        
        while a%2 != 0:
            print("Inserisce un numero pare")
            a = int(input("Inserisice un numero: "))
            
        break
    except:
        print("Numero non intero")

print(a)