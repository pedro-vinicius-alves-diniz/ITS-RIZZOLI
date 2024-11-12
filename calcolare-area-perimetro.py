import math

class CalcolaAreaPerimetro():
    def __init__(self):
        l1, l2, l3 = map(int, input("Insira i valori dei lati ").split())

        self.verifica_triangolo(l1, l2, l3)
        

    # FUNZIONE PER VERFICARE SE I DATI INSERETI SONO UN TRIANGOLO
    def verifica_triangolo(self, lato1, lato2, lato3):
        if lato1 < lato2 + lato3 and lato2 < lato1 + lato3 and lato3 < lato1 + lato2:
            print("È un triangolo.")
            self.area(lato1, lato2, lato3, self.tipo_di_triangolo(lato1,lato2, lato2))
            self.perimetro(lato1, lato2, lato3)
        else:
            print("Non è un trinagolo.")

    # FUNZIONE PER VERIFICARE IL TIPO DI TRIANGOLO D'ACCORDO CON I LATI
    def tipo_di_triangolo(self, l1, l2, l3):
        tipo = ""
        if l1 == l2 ==l3:
            print("Triangolo equilatero.")
            tipo = "equilatero"

            return tipo
        
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print("Triangolo isoscele.")
            tipo = "isoscele"

            return tipo
        
        else:
            print("Triangolo scaleno.")
            tipo = "scaleno"

            return tipo


    # FUNZIONE PER CALCOLARE L'AREA DEL TRIANGOLO
    def perimetro(self, lato1, lato2, lato3):
        perimetro = lato1 + lato2 + lato3

        print("Il perimeto è uguale a", perimetro)

    #  FUNZIONE PER CALCOLARE L'AREA DEL TRIANGOLO
    def area(self, l1, l2, l3, tipo):
        if tipo == "equilatero":
            area = (math.sqrt(3)/4)*l1*l1

            print("L'area del triangolo è uguale a", round(area, 2))
        elif tipo == "isoscele":
            altezza  = math.sqrt(l1**2 - (l2 / 2)**2)
            area = (l2 * altezza)/2

            print("L'area del triangolo è uguale a", round(area, 2))
        else:
            semi_perimetro = (l1 + l2 + l3)/2
            area = math.sqrt(semi_perimetro*(semi_perimetro - l1) * (semi_perimetro - l2) * (semi_perimetro - l3))

            print("L'area del triangolo è uguale a", round(area, 2))

        

if __name__ == "__main__":
    CalcolaAreaPerimetro()