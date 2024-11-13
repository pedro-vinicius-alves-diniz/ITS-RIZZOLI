# Richiesti 3 lati in input dire in output di che tipo di triangolo si tratta, se isoscele, scaleno o equilatero      

class TipoTriangolo():
    def __init__(self):
        l1, l2, l3 = map(int, input("Insira tre lati: ").split())

        self.tipo_di_triangolo(l1, l2, l3)

    def verifica_triangolo(self, lato1, lato2, lato3):
        if lato1 < lato2 + lato3 and lato2 < lato1 + lato3 and lato3 < lato1 + lato2:
            self.tipo_di_triangolo(lato1, lato2, lato3)
        else:
            print("Non è un trinagolo.")

    def tipo_di_triangolo(self, l1, l2, l3):
        if l1 == l2 ==l3:
            print("Triangolo equilatero.")
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print("Triangolo isoscele.")
        else:
            print("Triangolo scaleno.")


if __name__ == "__main__":
    TipoTriangolo()