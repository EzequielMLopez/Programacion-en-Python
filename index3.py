#Programa encargado de calcular el area de un triangulo

def main():

    from math import sqrt
    
    lad_izq = float(input("Ingrese el lado izquierdo del triangulo:"))
    lad_der = float(input("Ingrese el lado derecho del triangulo:"))
    base = float(input("Ingrese la base del triangulo:"))
    peri = lad_izq + lad_der + base
    s = peri / 2 #semi-perimetro
    area = sqrt(s * (s - lad_izq) * (s - lad_der) * (s - base))

    print ("El area es:",area,"\nY el perimetro es:",peri)
main()
