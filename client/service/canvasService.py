import tkinter

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

    tk = None
    canvas = None

    def on_canvas_click(event):
        print(event)

    def __init__(self):

        # What the fuck is this?
        self.tk = tkinter.Tk()
        self.canvas = tk.Canvas(tk, width=400, heigh = 400, bg='white')
        self.canvas.pack
        self.tk.mainloop()