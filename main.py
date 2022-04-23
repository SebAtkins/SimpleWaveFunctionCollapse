from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from random import randint

from matplotlib.pyplot import getp

#Coord system:
# (0,3) (1,3) (2,3) (3,3)
# (0,2) (1,2) (2,2) (3,2)
# (0,1) (1,1) (2,1) (3,1)
# (0,0) (1,0) (2,0) (3,0)

def getPixelID(x, y):
	global outputXScale

	return int(x + outputXScale / 2 * y)

if __name__ == "__main__":
	#Defines scale of output image
	outputXScale = 512
	outputYScale = 512

	#Contains RGB values for valid colours
	#0,100,0 - Green
	#0,0,100 - Blue
	colours = [(0,100,0), (0,0,100)]

	#Defines cardinal directions
	UP = (0, 1)
	DOWN = (0, -1)
	LEFT = (-1, 0)
	RIGHT = (1, 0)

	#Defines random colour for each coord
	coords = [randint(0, len(colours) - 1) for x in range(outputXScale*outputYScale)]

	#Sets up tkinter
	root = tk.Tk()
	canvas = tk.Canvas(root, height = outputYScale + 10, width = outputXScale + 10)
	
	#Sets up image
	img = Image.new("RGB", (outputXScale, outputYScale))
	draw = ImageDraw.Draw(img)

	#Currently just adds random colours to all squares
	for x in range(int(outputXScale / 2)):
		for y in range(int(outputYScale / 2)):
			draw.rectangle([4*x,4*y,4*(x+1),4*(y+1)], fill = colours[coords[getPixelID(x,y)]])

	#Displays the image
	image = ImageTk.PhotoImage(img)
	imagesprite = canvas.create_image((outputXScale + 10) / 2, (outputYScale + 10) / 2, image=image)
	canvas.pack()
	root.mainloop()