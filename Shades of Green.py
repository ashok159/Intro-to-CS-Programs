#Name: Ashok Surujdeo
#Date: February 16, 2021
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#This program prints: Shades of Green

import turtle

turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)

for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(0,i,0)

tess.penup()
tess.forward(300)
tess.pendown()
for i in range(255,0,-10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(0,i,0)
