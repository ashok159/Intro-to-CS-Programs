#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: February 2, 2021
#This program generates a star-flower.

import turtle
wn = turtle.Screen()
wn.bgcolor("cyan")

turtle = turtle.Turtle()
turtle.fillcolor('yellow')
turtle.pencolor('red')
turtle.pensize(1)
turtle.shape('turtle')

for i in range(18):
    turtle.forward(200)
    turtle.left(140)
    turtle.stamp()


