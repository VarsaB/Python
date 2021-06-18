# Draw polygon as per requirements

import turtle             

def draw_poly(num_sides,side_lenght): # draws polygon as per users choice
        angle = 360.0 / num_sides
        polygon = turtle.Turtle()
        for i in range(num_sides):
           polygon.forward(side_length)           
           polygon.left(angle) 
        turtle.done()
def draw_circle(): # Draws circle
        size = int(input("Enter radius of circle"))
        turtle.Turtle()
        turtle.circle(size)
        turtle.done()

#reads data from user as number of sides and lenght of it
print("What type of shape you want to draw ? \n Enter 1- Circle 2 - Polygon ")
choice = int(input())
if choice ==1 or choice ==2:
     if choice ==1:
             draw_circle()
     else:
             num_sides = int(input("Enter number of sides for polygon"))
             side_length = int(input("Enter lenght of side"))
             draw_poly(num_sides,side_length)
else:
        print("Invalid option!!")