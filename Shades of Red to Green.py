#Name: Ashok Surujdeo
#Date: February 16, 2021
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#This program prints: Shades of Red to Green

import turtle

turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)

for i in range(0,255,10):
    tess.forward(25)
    tess.pensize(i)
    tess.color(255-i,i,0)
    
