#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: February 23, 2021
#This program runs: Turtle Spiral

stamps = int(input("Enter number of stamps the turtle will print: "))

import turtle
alex = turtle.Turtle()
alex.shape('arrow')
alex.color('cyan')

alex.penup()
steps = 10

for i in range (0, stamps):
    alex.stamp()
    if (i % 2 == 0):
        steps += 3
    alex.forward(steps)
    alex.right(24)
