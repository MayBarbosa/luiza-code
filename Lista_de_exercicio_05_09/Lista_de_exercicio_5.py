class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        print(self.lado*self.lado)

    def perimetro(self):
        print(self.lado + self.lado + self.lado + self.lado)

