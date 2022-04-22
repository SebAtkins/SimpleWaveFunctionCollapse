from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from random import randint

if __name__ == "__main__":
	#Defines scale of output image
	outputXScale = 512
	outputYScale = 512

	#Contains RGB values fo valid colours
	#0,100,0 - Green
	#0,0,100 - Blue
	colours = [(0,100,0), (0,0,100)]
	coords = [randint(0,1) for x in range(outputXScale*outputYScale)]

	#Sets up tkinter and image
	root = tk.Tk()
	canvas = tk.Canvas(root, height = outputYScale + 10, width = outputXScale + 10)
	
	img = Image.new("RGB", (outputXScale, outputYScale))
	draw = ImageDraw.Draw(img)

	#Currently just adds random colours to all squares
	for x in range(int(outputXScale / 2)):
		for y in range(int(outputYScale / 2)):
			draw.rectangle([4*x,4*y,4*(x+1),4*(y+1)], fill = colours[coords[x + outputXScale * y]])
	
	#Displays the image
	image = ImageTk.PhotoImage(img)
	imagesprite = canvas.create_image((outputXScale + 10) / 2, (outputYScale + 10) / 2, image=image)
	canvas.pack()
	root.mainloop()