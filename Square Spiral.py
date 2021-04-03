#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 2, 2021
#This program runs: Square Spiral

import turtle

alex = turtle.Turtle()

length = 25

for i in range(100):
    alex.right(5)
    length = length*1.02
    for i in range(4):
        alex.forward(length)
        alex.right(90)
