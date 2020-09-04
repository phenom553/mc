#!/usr/bin/env python3


import turtle

#main window settings
window = turtle.Screen()
window.title("Pong by @phenom553")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer()


#Paddle A

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350, 0)
paddleA.shapesize(stretch_wid=5, stretch_len=1)


#Paddle B

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.penup()
paddleB.goto(350, 0)
paddleB.shapesize(stretch_wid=5, stretch_len=1)


#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#Move func
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)
    
def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)
    
    
def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)
    
def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)
    
#Keyboard

window.listen()
window.onkeypress(paddleA_up, "w")

window.listen()
window.onkeypress(paddleA_down, "s")


window.listen()
window.onkeypress(paddleB_up, "Up")
                  
window.listen()
window.onkeypress(paddleB_down, "Down")                 

#main game loop
while True:
    window.update()

