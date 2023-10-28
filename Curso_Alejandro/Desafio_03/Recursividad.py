#------------------------------------------------------------------------------#
#HACER LA SERIE DE FIGGONACCI CON METODO DE RECURSIVIDAD Y CON EL DE ITERACIÓN
#HACER EL INTERCAMBIO DE LOS VALORES DE UNA LISTA POR EL METODO DE RECURSIVIDAD
#------------------------------------------------------------------------------#

# RECURSIVIDAD

def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)

print(factorial(5))

# SERIE DE FIGONACCI #
def fibonacci(termino):
    if termino > 1:
        return fibonacci(termino - 1) + fibonacci(termino - 2)
    return termino

print(fibonacci(8))

def suma(numero):
    if numero == 0:
        return 0
    return numero + suma(numero-1)

print(suma(11))