import tkinter as tk
from tkinter import messagebox
LARGE_FONT= ("Verdana", 12)


class GS(tk.Tk):

    def __init__(self, height = 800, width = 800, lines = 50, *args, **kwargs):
        self.height = height
        self.width = width
        self.lines = lines
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        frame = Grid(container, self, self.height, self.width, self.lines)

        self.frames[Grid] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Grid)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Grid(tk.Frame):

    def __init__(self, parent, controller, height, width, lines):
        tk.Frame.__init__(self, parent)
        self.height = height
        self.width = width
        self.lines= lines
        self.clicks = []
        label = tk.Label(self, text="Graphics Simulator", font=LARGE_FONT)
        label.pack(pady =10, padx=10)
        self.canvas = tk.Canvas(height=self.height, width=self.width, bg='white')
        self.canvas.create_line(0, self.height/2, self.width, self.height/2)
        self.canvas.create_line(self.width/2, 0, self.width/2, self.height)
        #self.make_axes()
        self.canvas.bind('<Configure>', self.create_grid)
        self.canvas.pack(fill=tk.BOTH, expand=True)


    def create_grid(self, event = None):
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        lines = self.lines
        self.canvas.delete('grid_line')
    
        for i in range(0, w, lines):
            self.canvas.create_line([(i, 0), (i, h)], tag='grid_line')
    
        for i in range(0, h, lines):
            self.canvas.create_line([(0, i), (w, i)], tag='grid_line')

    def create_axes(self):
        for i in range(0, self.width//2, 50):
            #Negative X-axis
            self.canvas.create_line(i, self.height//2, i, self.height//2+3)
            self.canvas.create_text(i, self.height/2+10,fill="black",font="Times 10", text=str(-(self.width//2 - i)))

            #Positive X-axis
            self.canvas.create_line(i+self.width//2, self.height//2, i+self.width//2, self.height//2+3)
            self.canvas.create_text(i+self.width//2, self.height/2+10,fill="black",font="Times 10", text=str((i)))

        for i in range(50, self.height//2, 50):
            #Positive Y-axis
            self.canvas.create_line(self.width//2, i, self.width//2-5, i)
            self.canvas.create_text(self.width//2-17, i, fill="black",font="Times 10", text=str((self.height//2 - i)))

            #Negative Y-axis
            self.canvas.create_line(self.width//2, i+self.height//2, self.width//2-5, i+self.height//2)        
            self.canvas.create_text(self.width//2-17, i+self.height//2, fill="black",font="Times 10", text=str(-(self.height//2 - i)))    



        

    