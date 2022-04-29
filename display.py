import tkinter as tk
from PIL import ImageTk

class display:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height = self.y * 16, width = self.x * 16)
        self.image = ImageTk.PhotoImage(img)
        self.imagesprite = self.canvas.create_image(0, 0, anchor = tk.NW, image = self.image)
        self.canvas.pack()
    
    def update(self, img):
        self.image = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.imagesprite, image = self.image)
        self.canvas.pack()
        self.root.update_idletasks()
        self.root.update()
    
    def main(self):
        self.canvas.pack()
        self.root.mainloop()