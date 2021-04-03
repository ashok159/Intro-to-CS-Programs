#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 16, 2021
#This program runs: Turtle String

import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     
commands = input("Please enter a command string: ")

for ch in commands:
    if ch == 'F':            
        tess.forward(50)
    elif ch == 'L':          
        tess.left(90)
    elif ch == 'R':          
        tess.right(90)
    elif ch == '^':         
        tess.penup()
    elif ch == 'v':          
        tess.pendown()
    elif ch == 'r':          
        tess.color("red")
    elif ch == 'g':          
        tess.color("green")
    elif ch == 'b':
        tess.color("blue")
    elif ch == 'c':
        tess.color("cyan")
    elif ch == 'T':
        tess.shape("turtle")
        tess.stamp()
    elif ch == 'S':
        for i in range(4):
            tess.forward(50)
            tess.left(90)
    else:                    
        print("Error: do not know the command:", ch)

print("See graphics window for your image")
myWin.exitonclick()         
