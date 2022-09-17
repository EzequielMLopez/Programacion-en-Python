import turtle
import time
import random

screen = turtle.Screen()
snake = turtle.Turtle()
comida = snake.clone()
cuerpo = []

screen.setup(430, 430)
screen.title("EL JUEGO DE LA SERPIENTE EN TU COMPU PARA SIEMPRE")

snake.shape("square")
snake.direction = "stop"
snake.penup()

comida.shape("circle")
comida.color("orange")
comida.penup()
comida.hideturtle()
comida.goto(random.randrange(-200, 200), random.randrange(-200, 200))
comida.showturtle()

def up():
    snake.direction = "up"
def down():
    snake.direction = "down"
def left():
    snake.direction = "left"
def right():
    snake.direction = "right"

def movimiento():
    if(snake.direction == "up"):snake.sety(snake.ycor() + 20)
    elif(snake.direction == "down"):snake.sety(snake.ycor() - 20)  
    elif(snake.direction == "left"):snake.setx(snake.xcor() - 20)
    elif(snake.direction == "right"):snake.setx(snake.xcor() + 20) 

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

while(True):
    screen.update()

    if(snake.distance(comida) < 20):
        comida.hideturtle()        
        comida.goto(random.randrange(-200, 200), random.randrange(-200, 200))
        comida.showturtle()
        cuerpo.append(snake.clone())

    for i in range(len(cuerpo)-1,0,-1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto( x, y)
    if(len(cuerpo) > 0):
        x = snake.xcor()
        y = snake.ycor()
        cuerpo[0].goto(x, y)

    movimiento()
    time.sleep(0.04)