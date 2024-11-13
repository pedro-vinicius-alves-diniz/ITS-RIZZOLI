import math 
# Dati a, b e c in input calcolare le radici dell'equazione ax**2 + bx + c = 0


class EquazioneSecondoGrado():
    def __init__(self):
        a, b, c = map(float, input("Inserisce i valori di a, b e c: ").split())

        while a == 0:
            print("Non è un'equazione di secondo grado. L'a deve essere diverso da 0.")
            a = float(input("Inserisci il valore di a: "))
        
        self.formula_resolutiva(a , b, c)

    def calcolare_discriminante(self, a, b, c):
        discriminante = b*b-4*a*c

        return discriminante

    def formula_resolutiva(self, a, b, c):
        discriminante = self.calcolare_discriminante(a, b, c)

        if discriminante < 0:
            print("L'equazione non ha soluzioni reali.")
        else:
            x1 = ((b*-1) + math.sqrt(discriminante))/2*a
            x2 = ((b*-1) - math.sqrt(discriminante))/2*a

            print("Le due soluzioni sono", round(x1, 2), " and", round(x2, 2))


if __name__ == "__main__":
    EquazioneSecondoGrado()