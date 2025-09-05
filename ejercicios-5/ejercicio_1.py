class  Rectangulo():
    ladoA = 0
    ladoB = 0
    area = 0
    color = "blanco"
    perimetro= 0
    def cuantoValeA(self, valor):
        self.ladoA = valor
    def cuantoValeB(self, valor):
        self.ladoB = valor
    def area(self):
        self.area = self.ladoA * self.ladoB
        print("El area de este rectangulo es ", self.area )
    def perimetro(self):
        self.perimetro = 2*(self.ladoA + self.ladoB)
        print("El perimetro de este rectangulo es ", self.perimetro)

rectangulo1 = Rectangulo()
rectangulo1.cuantoValeA(7.5)
rectangulo1.cuantoValeB(4.6)
rectangulo1.area()
rectangulo1.perimetro()

class triangulo:
    cateto1= 0 
    cateto2= 0
    hipotenusa = 0
    area = 0
    perimetro = 0
    def cuantovaleCateto1(self, valor):
        self.cateto1 = valor
    def cuantoValeCateto2(self, valor):
        self.cateto2 = valor
    def cuantoValeHipotenusa(self, valor):
        self.hipotenusa = valor
    def area(self):
        self.area = (self.cateto1 * self.cateto2)/2
        print("El area de este triangulo es ", self.area)
    def perimetro(self):
        self.perimetro= self.cateto1 + self.cateto2 + self.hipotenusa
        print("El perimetro de este triangulo es ", self.perimetro)

triangulo1 = triangulo()
triangulo1.cuantovaleCateto1(12)
triangulo1.cuantoValeCateto2(10)
triangulo1.cuantoValeHipotenusa(27)
triangulo1.area()
triangulo1.perimetro()