#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: April 6, 2021
#This program runs: Fixed Errors

import turtle
import random


print("This program draws concentric circles of many different colors")

# prompt for the input
fig_num = int(input("Enter the number of circles to draw: "))
radius = int(input("Enter the radius of the largest circle: "))

#set the decrement for each concentric radius
decrement = (radius / fig_num)

#initialize turtle
tina = turtle.Turtle()

# draw fig_num filled concentric circles, randomly changing colors
for j in range(fig_num):
    #move the turtle to the -radius y coordinate
    tina.goto(0,-radius)

    #set a random color
    (r,g,b) = (random.random(), random.random(), random.random())
    tina.pencolor(r,g,b)
    tina.fillcolor(r,g,b)

    #draw the circle
    tina.down()
    tina.begin_fill()
    tina.circle(radius)
    tina.end_fill()

    #decrement the radius for the next concentric circle
    radius -= decrement

turtle.Screen().exitonclick()
