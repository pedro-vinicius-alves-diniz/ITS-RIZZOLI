# Dati a e b, risolvere l'equazione ax + b = 0

class EquaPrimoGrado():
    def __init__(self):
        a = int(input("Insira il valore di a: "))
        b = int(input("Insira il valore di b: "))

        self.calcolare(a, b)

    def calcolare(self, a, b):
        x = -b/a

        print("Il risultado finale è", round(x, 2))


if __name__ == "__main__":
    EquaPrimoGrado()