"""
This program will draw a snowman on the screen.
"""

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 400
bottom_diameter = canvas_height/2
middle_diameter = bottom_diameter/2
top_diameter = middle_diameter/2

# Create canvas
screen = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
screen.pack()

# Add shapes here!



# Add shapes to canvas
mainloop()
