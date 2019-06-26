class Cuadrado:
    def __init__(self,lado):
        
        self.lado = lado
        

    def calcularArea(self):
         area = self.lado*self.lado
         print "El area del cuadrado es: ",area

    def calcularPerimetro(self):
         perimetro = self.lado*4
         print "El perimetro del cuadrado es: ",perimetro
        

cuadrado = Cuadrado(5)

if __name__ == "__main___":
    cuadrado.calcularArea()
    cuadrado.calcularPerimetro()
