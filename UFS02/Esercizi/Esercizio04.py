'''
Creare un programma che chieda all’utente di inserire una stringa di lunghezza pari. Se l’utente inserisce una
stringa dispari, il programma dovrà chiedergli di reinserirla fino a che non inserisca una stringa di lunghezza
pari.
'''

class Esercizio04():
    def __init__(self):
        while True:
            self.stringa = input("Insersci una stringa di lunghezza pari: ")
            
            if len(self.stringa) % 2 == 0:
                return print("Benissímo, ce l'hai fatta!")
            else:
                print("Erro: la stringa ha una lunghezza dispari. Prova un'altra volta.")


if __name__ == "__main__":
    Esercizio04()