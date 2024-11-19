import math

class CalcolaAreaPerimetro():
    def __init__(self):
        l1, l2, l3 = map(int, input("Insira i valori dei lati ").split())

        self.verifica_triangolo(l1, l2, l3)
        

    # FUNZIONE PER VERFICARE SE I DATI INSERETI SONO UN TRIANGOLO
    def verifica_triangolo(self, lato1, lato2, lato3):
        if (lato1 > 0 or lato2 > 0 or lato3 > 0) and (lato1 < lato2 + lato3 and lato2 < lato1 + lato3 and lato3 < lato1 + lato2):
            print("È un triangolo.")
            perimetro = self.perimetro(lato1, lato2, lato3)
            area = self.area(lato1, lato2, lato3, perimetro/2)
            altezza = self.altezza(area, lato1)

            print("Il perimetro del triangolo è:", round(perimetro, 2))
            print("L'area del triangolo è:", round(area, 2))
            print("L'altezza del triangolo è:", round(altezza, 2))
        else:
            print("Non è un trinagolo.")


    # FUNZIONE PER CALCOLARE L'AREA DEL TRIANGOLO
    def perimetro(self, lato1, lato2, lato3):
        perimetro = lato1 + lato2 + lato3

        return perimetro

    #  FUNZIONE PER CALCOLARE L'AREA DEL TRIANGOLO
    def area(self, l1, l2, l3, sp):
        area = math.sqrt(sp*(sp-l1)*(sp-l2)*(sp-l3))

        return area

    # FUNZIONE PER CALCOLARE L'ALTEZZA DEL TRIANGOLO
    def altezza(self, area, lato1):
        altezza = 2*area/lato1

        return altezza       

if __name__ == "__main__":
    CalcolaAreaPerimetro()