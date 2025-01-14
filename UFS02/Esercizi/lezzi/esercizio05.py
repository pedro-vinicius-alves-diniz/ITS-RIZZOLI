'''
Creare un programma che chieda all’utente di inserire un numero n e stampi una stringa lunga n
caratteri dove i caratteri che la compongono saranno i caratteri @ e # alternati partendo con un
carattere @
Ad esempio se l’utente dice che la stringa dovrà essere lunga 5 caratteri la stringa stampata dovrà
essere: @#@#@
'''

class Esercizio05():
    def __init__(self):
        self.stringa = ""
        self.n = self.definire_n()

        print(self.n)
        print(self.update_stringa(self.n))

    def definire_n(self):
        n = int(input("Scegli la lunghezza della stringa: "))

        return n

    def update_stringa(self, n):
        for i in range(int(n)):
            if i % 2 == 0:
                self.stringa += "@"
            else:
                self.stringa += "#"
            
        return self.stringa
            

if __name__ == "__main__":
    Esercizio05()