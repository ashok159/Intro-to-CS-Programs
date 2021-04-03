#Name:Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: February 16, 2021
#This program runs: Turtle Color

import turtle

word = input("Hexidecimal:")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("#" + word)

for i in range(5):
    alex.stamp()
    alex.penup()
    alex.forward(50)
    alex.pendown()
