class Rectangulo:
    def __init__(self,lado1,lado2):
        
        self.lado1 = lado1
        self.lado2 = lado2
        

    def calcularArea(self):
         area = self.lado1*self.lado2
         print "El area del rectangulo es: ",area
        
    def calcularPerimetro(self):
         perimetro = (self.lado1*2)+(self.lado2*2)
         print "El area del rectangulo es: ",perimetro
         
rectangulo = Rectangulo(5,3)

if __name__ == "__main___":
    rectangulo.calcularArea()
    rectangulo.calcularPerimetro()

