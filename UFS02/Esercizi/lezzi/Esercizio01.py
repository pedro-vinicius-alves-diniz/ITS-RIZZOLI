'''
Implementare delle funzioni che consentano di trovare il massimo, minimo, contare il numero di elementi su
una lista e ridefinire la funzione range senza usare le funzioni predefinite di python (len, max, min, range).
'''

class Esecizio1():
    def __init__(self):
        lista = []
        
        self.add(lista)

        print(f"Il numero di elementi sulla lista è {self.len(lista)}")
        print(f"Il minimo della lista è {self.min(lista)}")
        print(f"Il massimo della lista è {self.max(lista)}")
                
                
    def add(self, lista):
        while True:
            try:
                valore = int(input("Inserisca un valore. ('0' per uscire!): "))
                if valore == 0:
                    print("Uscito con sucesso")
                    break

                lista.append(valore)
            except:
                print(f"Errore nell'inserimento del valore. Provi un'altra volta")

    def min(self, lista):
        minn = 0
        for i in lista:
            if i == lista[0]:
                minn = i
            else:
                if i < minn:
                    minn = i
        
        return minn

    def max(self, lista):
        maxx = 0
        for i in lista:
            if i == lista[0]:
                maxx = i
            else:
                if i > maxx:
                    maxx = i
        
        return maxx

    def len(self, lista):
        lenn = 0
        for i in lista:
            lenn += 1

        
        return lenn

if __name__ == "__main__":
    Esecizio1()