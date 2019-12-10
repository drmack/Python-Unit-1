"""
This program will draw two lines across the canvas in an X formation.
"""

from tkinter import *

root = Tk()

# Create canvas
screen = Canvas(root, width = 300, height = 200)
screen.pack()

# Draw black lines
screen.create_line(0, 0, 300, 200)
screen.create_line(0, 200, 300, 0)

# Add shapes to canvas
mainloop()