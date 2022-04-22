from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from random import randint

if __name__ == "__main__":
	#Contains RGB values fo valid colours
	#0,100,0 - Green
	#0,0,100 - Blue
	colours = [(0,100,0), (0,0,100)]

	root = tk.Tk()
	canvas = tk.Canvas(root, height = 200, width = 200)

	img = Image.new("RGB", (128, 128))
	draw = ImageDraw.Draw(img)

	for x in range(64):
		for y in range(64):
			draw.rectangle([4*x,4*y,4*(x+1),4*(y+1)], fill = colours[randint(0,1)])
	
	image = ImageTk.PhotoImage(img)
	imagesprite = canvas.create_image(100, 100, image=image)
	canvas.pack()

	root.mainloop()