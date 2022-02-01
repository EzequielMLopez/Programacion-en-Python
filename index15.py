#Programa: index15.py
#Proposito: Desglosar en diversos billetes el monto que se ingresa por
#           teclado
#Autor: Ezequiel Lopez
#Fecha: 01/02/2022

def main():
    
    #Datos base 
    bi500 = 500
    bi200 = 200
    bi100 = 100
    bi50 = 50
    bi20 = 20
    bi10 = 10
    bi5 = 5
    mon2 = 2
    mon1 = 1
    coci = 0
    rest = 0

    #Datos de entrada
    num = int(input("Ingrese valor en euros:"))

    #Operaciones
    if(num > bi500):
        coci = num / bi500
        rest = num % bi500
        print("%d billetes de %d euros" % (coci,bi500))
    if(rest >= bi200):
        coci = rest / bi200
        rest = num % bi200
        print("%d billetes de %d euros" % (coci,bi200))
    if(rest >=  bi100):
        coci = rest / bi100
        rest = num % bi100
        print("%d billetes de %d euros" % (coci,bi100))
    if(rest >= bi50):
        coci = rest / bi50
        rest = num % bi50
        print("%d billetes de %d euros" % (coci,bi50))
    if(rest >= bi20):
        coci = rest / bi20
        rest = num % bi20
        print("%d billetes de %d euros" % (coci,bi20))
    if(rest >= bi10):
        coci = rest / bi10
        rest = num % bi10
        print("%d billetes de %d euros" % (coci,bi10))
    if(rest >= bi5):
        coci = rest / bi5
        rest = num % bi5
        print("%d billetes de %d euros" % (coci,bi5))
    if(rest >= mon2):
        coci = rest / mon2
        rest = num % mon2
        print("%d monedas de %d euros" % (coci,mon2))
    if(rest >= mon1):
        coci = rest / mon1
        rest = num % mon1
        print("%d monedas de %d euros" % (coci,mon1))

    if(num >= bi200 and num < bi500):
        coci = num / bi200
        rest = num % bi200
        print("%d billetes de %d euros" % (coci,bi200))
    if(rest >= bi100):
        coci = rest / bi100
        rest = num % bi100
        print("%d billetes de %d euros" % (coci,bi100))
    if(rest >= bi50):
        coci = rest / bi50
        rest = num % bi50
        print("%d billetes de %d euros" % (coci,bi50))
    if(rest >= bi20):
        coci = rest / bi20
        rest = num % bi20
        print("%d billetes de %d euros" % (coci,bi20))
    if(rest >= bi10):
        coci = rest / bi10
        rest = num % bi10
        print("%d billetes de %d euros" % (coci,bi10))
    if(rest >= bi5):
        coci = rest / bi5
        rest = num % bi5
        print("%d billetes de %d euros" % (coci,bi5))
    if(rest >= mon2):
        coci = rest / mon2
        rest = num % mon2
        print("%d monedas de %d euros" % (coci,mon2))
    if(rest >= mon1):
        coci = rest / mon1
        rest = num % mon1
        print("%d monedas de %d euros" % (coci,mon1))

    if(num >= bi100 and num < bi200):
        coci = num / bi100
        rest = num % bi100
        print("%d billetes de %d euros" % (coci,bi100))
    if(rest >= bi50):
        coci = rest / bi50
        rest = num % bi50
        print("%d billetes de %d euros" % (coci,bi50))
    if(rest >= bi20):
        coci = rest / bi20
        rest = num % bi20
        print("%d billetes de %d euros" % (coci,bi20))
    if(rest >= bi10):
        coci = rest / bi10
        rest = num % bi10
        print("%d billetes de %d euros" % (coci,bi10))
    if(rest >= bi5):
        coci = rest / bi5
        rest = num % bi5
        print("%d billetes de %d euros" % (coci,bi5))
    if(rest >= mon2):
        coci = rest / mon2
        rest = num % mon2
        print("%d monedas de %d euros" % (coci,mon2))
    if(rest >= mon1):
        coci = rest / mon1
        rest = num % mon1
        print("%d monedas de %d euros" % (coci,mon1))


    if(num >= bi50 and num < bi100):
        coci = num / bi50
        rest = num % bi50
        print("%d billetes de %d euros" % (coci,bi50))
    if(rest >= bi20):
        coci = rest / bi20
        rest = num % bi20
        print("%d billetes de %d euros" % (coci,bi20))
    if(rest >= bi10):
        coci = rest / bi10
        rest = num % bi10
        print("%d billetes de %d euros" % (coci,bi10))
    if(rest >= bi5):
        coci = rest / bi5
        rest = num % bi5
        print("%d billetes de %d euros" % (coci,bi5))
    if(rest >= mon2):
        coci = rest / mon2
        rest = num % mon2
        print("%d monedas de %d euros" % (coci,mon2))
    if(rest >= mon1):
        coci = rest / mon1
        rest = num % mon1
        print("%d monedas de %d euros" % (coci,mon1))


    if(num >= bi20 and num < bi50):
        coci = num / bi20
        rest = num % bi20
        print("%d billetes de %d euros" % (coci,bi20))
    if(rest >= bi10):
        coci = rest / bi10
        rest = num % bi10
        print("%d billetes de %d euros" % (coci,bi10))
    if(rest >= bi5):
        coci = rest / bi5
        rest = num % bi5
        print("%d billetes de %d euros" % (coci,bi5))
    if(rest >= mon2):
        coci = rest / mon2
        rest = num % mon2
        print("%d monedas de %d euros" % (coci,mon2))
    if(rest >= mon1):
        coci = rest / mon1
        rest = num % mon1
        print("%d monedas de %d euros" % (coci,mon1))


    if(num >= bi10 and num < bi20):
        coci = num / bi10
        rest = num % bi10
        print("%d billetes de %d euros" % (coci,bi10))
    if(rest >= bi5):
        coci = rest / bi5
        rest = num % bi5
        print("%d billetes de %d euros" % (coci,bi5))
    if(rest >= mon2):
        coci = rest / mon2
        rest = num % mon2
        print("%d monedas de %d euros" % (coci,mon2))
    if(rest >= mon1):
        coci = rest / mon1
        rest = num % mon1
        print("%d monedas de %d euros" % (coci,mon1))


    if(num >= bi5 and num < bi10):
        coci = num / bi5
        rest = num % bi5
        print("%d billetes de %d euros" % (coci,bi50))
    if(rest >= mon2):
        coci = rest / mon2
        rest = num % mon2
        print("%d monedas de %d euros" % (coci,mon2))
    if(rest >= mon1):
        coci = rest / mon1
        rest = num % mon1
        print("%d monedas de %d euros" % (coci,mon1))


    if(num >= bi2 and num < bi5):
        coci = num / bi2
        rest = num % bi2
        print("%d billetes de %d euros" % (coci,bi2))
    if(rest >= mon1):
        coci = rest / mon1
        rest = num % mon1
        print("%d monedas de %d euros" % (coci,mon1))


    if(num >= bi1 and num < bi2):
        coci = num / bi1
        rest = num % bi1
        print("%d billetes de %d euros" % (coci,bi1))

main()
            


            

