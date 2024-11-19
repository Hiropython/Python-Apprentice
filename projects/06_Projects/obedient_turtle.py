"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
from tkinter import messagebox, simpledialog, Tk


# TODO)
import turtle
turtle.setup(width=600, height=600)
t=turtle.Turtle()
t.shape('turtle')
#t.speed(0)
def square(size):
    for i in range (4):
        t.forward(size)
        t.right(90)


def triangle(size):
    for i in range (3):
        t.forward(size)
        t.left(120)



def circle(size):
    t.speed(0)
    for i in range (130):
        t.forward(size)
        t.right(3)

request = True
while request:
    answer=simpledialog.askstring("Shape","What shape should I draw?")
    if answer=="square":
        square(100)
        request = False
    elif answer=="triangle":
        triangle(100)
        request=False
    elif answer=="circle":
        circle(2)
        request=False
    else:
         messagebox.showinfo('Error',"Choose square, triangle, or circle" )



#   1. Create a turtle.
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
pass
turtle.exitonclick()