from tkinter import Tk, Canvas
import os

"""
This is the class we will use to dictate where things are
"""
class Coordinates():
    x = None
    y = None

    def __init__ (self, x, y):
        self.x = x
        self.y = y

class CanvasService():

    window = None
    canvas = None
    parent_close_function = None

    def on_canvas_click(event):
        print(event)

    def on_close(self):
        self.parent_close_function()

    def __init__(self, parent_close_function):

        print(f'Creating Window...')
        self.window = Tk()
        self.window.title('Hello Stinky')
        self.window.geometry("800x600")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.canvas = Canvas(self.window, bg='white')
        self.parent_close_function = parent_close_function
        self.window.mainloop()