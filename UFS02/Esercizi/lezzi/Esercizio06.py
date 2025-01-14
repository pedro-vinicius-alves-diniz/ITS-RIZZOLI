'''
Creare una funzione che, data una lista di numeri ed un numero da cercare, restituisca il valore
booleano True se tale numero è presente nella lista, False altrimenti
'''
import random as rd

class Esercizio06():
    def __init__(self):
        self.lista = self.add_numeri()

        print(self.controla_numero(self.lista))


    def add_numeri(self):
        lista = []
        for i in range(10):
            valore = int(rd.randint(1, 100))
            lista.append(valore)

        return lista

    def controla_numero(self, lista):
        try:
            numero = int(input("Inserisci un numero tra 1 e 100: "))

            if numero in self.lista:
                return True
            else:
                return False
        except:
            print("Qualcosa è andato storto. Prova un'altra volta.")
            self.controla_numero()


if __name__ == "__main__":
    Esercizio06()