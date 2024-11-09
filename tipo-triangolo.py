









      
class TipoTriangolo():
    def __init__(self):
        l1, l2, l3 = map(int, input("Insira tre lati").split())

        self.verificare_tipo_triangolo(l1, l2, l3)

    def verificare_tipo_triangolo(self, l1, l2, l3):
        pass

if __name__ == "__main__":
    TipoTriangolo()