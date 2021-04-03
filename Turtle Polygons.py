#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 23, 2021
#This program runs: Turtle Polygons

import turtle
def setUp(t, dist, col):
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)

def nestedPolygon(t, length, sides):
    if length > 10:
        for i in range(sides):
            t.forward(length)
            t.left(360/sides)
        nestedPolygon(t, length/2, sides)

def fractalPolygon(t, length, sides):
    if length > 10:
        for i in range(sides):
            t.forward(length)
            t.left(360/sides)
            fractalPolygon(t, length/2, sides)

def main():
    l = int(input('Enter length: '))
    s = int(input('Enter number of sides: '))
    if s < 3:
        print("A polygon must have at least 3 sides.")
    else:
        tom = turtle.Turtle()
        setUp(tom, -100, "darkgreen")
        nestedPolygon(tom, l, s)

        tess = turtle.Turtle()
        setUp(tess, 100, "steelblue")
        fractalPolygon(tess, l, s)

if __name__ == "__main__":
    main()
    
