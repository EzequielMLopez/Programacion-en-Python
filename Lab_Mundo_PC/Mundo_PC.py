#Programa: Mundo_PC.py
#Proposito: Simulación de ordenes de venta.
#Autor: Ezequiel Lopez
#Fecha: 31/08/2022

from Monitor import *
from Ratón import *
from Teclado import *
from Computadora import *
from Orden import *

raton = Raton("Bluethoot", "Fedora")
teclado = Teclado("Digital", "Vemos")
monitor = Monitor("HP", "25PX")
raton2 = Raton("Alcachofa", "Pepino")
comboHP = Computadora("Intento", monitor, teclado, raton)
comboACER = Computadora("Factible", monitor, teclado, raton2)
comboCASET = Computadora("Santis", monitor, teclado, raton)

venta = Orden(comboHP)    
venta.agregarComputadora(comboCASET)
venta.agregarComputadora(comboACER)

print(venta)