import tkinter as tk
from gs import screen

class GS(tk.Tk):

    def __init__(self, height = 800, width = 800, mode = "g 50", *args, **kwargs):

        self.height = height
        self.width = width
        self.mode = mode

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        frame = screen.Screen(container, self, self.height, self.width, self.mode)

        self.frames[screen.Screen] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(screen.Screen)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()





        

    