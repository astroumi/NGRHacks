from tkinter import *

root = Tk() # Creates graphical window

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!") # Defines widget
myLabel2 = Label(root, text="Hello World!") # Defines widget
# Shoving it onto screen

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

root.mainloop() # Allows the program to continue looping and taking in inputs
