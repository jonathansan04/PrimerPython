import math
class Circulo:
    def __init__(self,radio):
        
        self.radio = radio
        

    def calcularArea(self):
         area = math.pi * self.radio**2
         print "El area del circulo es: ",area
        
    def calcularPerimetro(self):
         perimetro = math.pi * 2 * self.radio
         print "El perimetro del circulo es: ",perimetro

circulo = Circulo(2)

if __name__ == "__main___":
    circulo.calcularArea()
    circulo.calcularPerimetro()



                
        
    
    
        
    
    
