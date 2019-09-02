import tkinter as tk
LARGE_FONT= ("Verdana", 12)

class Screen(tk.Frame):

    def __init__(self, parent, controller, height, width, mode = "g 100"):
        tk.Frame.__init__(self, parent)
        self.height = height
        self.width = width
        self.mode = mode
        if(self.mode[0] == "g"):
            self.lines = int(mode[2:])

        #Window label
        label = tk.Label(self, text="Graphics Simulator", font=LARGE_FONT)
        label.pack(pady =10, padx=10)

        #Canvas creation
        self.canvas = tk.Canvas(height=self.height, width=self.width, bg='white')
        self.canvas.create_line(0, self.height/2, self.width, self.height/2)
        self.canvas.create_line(self.width/2, 0, self.width/2, self.height)

        if(self.mode[0] == "g"):
            self.canvas.bind('<Configure>', self.create_grid)
        elif(self.mode[0] == "c"):
            self.canvas.bind('<Configure>', self.create_axes)


        self.canvas.pack(fill=tk.BOTH, expand=True)


    def create_grid(self, event = None):
        """Create a grid of pixels to simulate pixels on your screen."""
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        lines = self.lines
        self.canvas.delete('grid_line')
    
        for i in range(0, w, lines):
            self.canvas.create_line([(i, 0), (i, h)], tag='grid_line')
    
        for i in range(0, h, lines):
            self.canvas.create_line([(0, i), (w, i)], tag='grid_line')


    def create_axes(self, event = None):
        """Create cartesian co-ordinate axes."""
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
