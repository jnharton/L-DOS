'''
graphics

'''

import os
import time
import turtle

def pg(text, length, size, mod):
    turtle.screensize(250,250)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.ht()
    turtle.title("Graphical Interface")
    turtle.clear()
    turtle.write(text, align = "center", font = ("Arial", size, mod))
    turtle.pu
    time.sleep(length)


def pgui(text, fon):
    turtle.screensize(250,250)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.ht()
    turtle.title("Graphical Interface")
    turtle.clear()
    turtle.write(text, align = "center", font = (fon, 10, "bold"))
    turtle.pu
    time.sleep(10)

def ttext():
    turtle.screensize(250, 250)
    turtle.penup()
    turtle.goto(0,225)
    turtle.pendown()
    turtle.ht()
    turtle.title("Graphical Interface")
    turtle.write("Graphical Interface", align = "center", font = ("Arial", 10, "bold"))
    turtle.pu()
    turtle.goto(0, -150)
    turtle.pd()
    path = os.getcwd()
    turtle.write(path, align="center", font=("Arial", 8, "bold"))
    turtle.pu()
    turtle.goto(0, -255)
    turtle.pd()

def square():
    #import turtle
    turtle.clear()
    turtle.pu()
    turtle.begin_fill()
    turtle.goto(400,400)
    turtle.pd()
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)


def moveturtle(x, y):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()