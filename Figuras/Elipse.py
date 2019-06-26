import math
class Elipse:
    def __init__(self,radio1,radio2): 
        self.radio1 = radio1
        self.radio2 = radio2
        

    def calcularArea(self):
         area = self.radio1 * self.radio2 * math.pi
         print "El area de la elipse es: ",area
        
    def calcularPerimetro(self):
         perimetro = 2 * math.pi * math.sqrt(((self.radio1**2)+(self.radio2**2))/2)
         print "El perimetro de la elipse es: ",perimetro
         
elipse = Elipse(5,3)
if __name__ == "__main___":
    elipse.calcularArea()
    elipse.calcularPerimetro()
