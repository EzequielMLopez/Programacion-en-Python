#Programa: Juego_Tortugas.py
#Proposito: Simular la carrera de dos tortugas.
#Autor: Ezequiel Lopez
#Fecha: 22/08/2022

import random
import turtle

def iniciot1():
    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.pencolor("red")
    return t1

def iniciot2():
    t2 = turtle.Turtle()
    t2.penup()
    t2.sety(-70)
    t2.shape("turtle")
    t2.pencolor("green")
    t2.pendown()
    return t2

def meta1():
    t3 = turtle.Turtle()
    t3.penup()
    t3.hideturtle()
    t3.sety(-30)
    t3.forward(200)
    t3.pendown()
    t3.pencolor("red")
    t3.circle(30)

def meta2():
    t3 = turtle.Turtle()
    t3.penup()
    t3.hideturtle()
    t3.sety(-100)
    t3.forward(200)
    t3.pendown()
    t3.pencolor("green")
    t3.circle(30)

screen = turtle.Screen()
screen.title("UN MUNDO SE CREA CON IMAGINACIÓN Y PERSEVERANCIA")
choice = "Yes"
while(choice == "Yes"):
    t1 = iniciot1()
    t2 = iniciot2()
    meta1()
    meta2()
    verdad = True
    while(t1.xcor() < 185 and t2.xcor() < 185 and verdad == True):
        t1.forward(random.randrange(1, 6) * 7)
        t2.forward(random.randrange(1, 6) * 7)
        if(t1.xcor() > 185):
            t1.penup()
            t1.backward(t1.xcor() - 200)
            t1.write("Gane, soy la tortuga más rojaaa SIUUUU", False, align="right")
            verdad = False
            break        
        if(t2.xcor() > 185):
            t2.penup()
            t2.backward(t2.xcor() - 200)
            t2.write("Alguna vez viste algo tan verde como LLOO?", False, align="right")
            verdad = False
            break
    choice = input("Quieres seguir jugando? Yes/Not: ")
    if(choice == "Yes"):screen.clear()
    else:
        print("Espero que lo hayas disfrutado, no te olvides de cerrar la ventana antes de irte :)")
        break

turtle.done()