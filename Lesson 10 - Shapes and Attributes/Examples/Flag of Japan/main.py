"""
This program will draw the Japanese flag.
"""

from tkinter import *

root = Tk()

# Create canvas
screen = Canvas(root, width = 400, height = 300, bg="white")
screen.pack()

# Draw red circle
screen.create_oval(100, 50, 300, 250, fill="red", outline="")

# Add shapes to canvas
mainloop()