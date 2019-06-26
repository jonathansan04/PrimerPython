import math
class Triangulo:
    def __init__(self,base,altura):
        
        self.base = base
        self.altura = altura
        

    def calcularArea(self):
         area = (self.base*self.altura)/2
         print "El area del triangulo es: ",area
        
    def calcularPerimetro(self):
         hipotenusa = math.sqrt((self.base**2)+(self.altura**2))
         
         perimetro = (self.base)+(self.altura)+(hipotenusa)
         print "El perimetro del triangulo es: ",perimetro
triangulo = Triangulo(5,3)
if __name__ == "__main___":
    triangulo.calcularArea()
    triangulo.calcularPerimetro()

