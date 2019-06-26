op=input("Seleccione una opcion:")
if op==1:
    from Cuadrado import cuadrado as cu
    cu.calcularArea()
    cu.calcularPerimetro()
elif op==2:
    from Rectangulo import rectangulo as cu2
    cu2.calcularArea()
    cu2.calcularPerimetro()
elif op==3:
    from Circulo import circulo as cu3
    cu3.calcularArea()
    
    cu3.calcularPerimetro()
elif op==4:
    from Elipse import elipse as cu4
    cu4.calcularArea()
    cu4.calcularPerimetro()
elif op==5:
    from Triangulo import triangulo as cu5
    cu5.calcularArea()
    cu5.calcularPerimetro()
else:
    print"No hay ninguna opcion"
    
         

