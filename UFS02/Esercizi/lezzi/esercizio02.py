'''
Creare un programma che permetta all’utente di effettuare la moltiplicazione tra due numeri senza utilizzare
l’operatore * ma calcolando il risultato attraverso somme ripetute (numeri positivi).
'''

class Esercizio02():
    def __init__(self):
        
        self.sceltaFattori()

        print(f"Il risultado della molteplicazione è uguale a {self.molteplicare(self.fattore1, self.fattore2)}")


    def sceltaFattori(self):
        try:
            self.fattore1 = int(input("Inserisci il primo fattore: "))
            self.fattore2 = int(input("Inserisci il secondo fattore: "))
        except:
            print("Qualcosa è andato storto. Prova un'altra volta.")
            self.sceltaFattori()

    def molteplicare(self, f1, f2):
        risultato = 0

        for i in range(f2):
            risultato +=f1
        
        return risultato


if __name__ == "__main__":
    Esercizio02()