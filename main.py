from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from random import randint

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
	BLUE = (0, 0, 100)
	GREEN = (0, 100, 0)
	NONE = (0, 0, 0)
	COLOURS = [GREEN, BLUE]

	#Defines cardinal directions
	UP = (0, 1)
	DOWN = (0, -1)
	LEFT = (-1, 0)
	RIGHT = (1, 0)

	#Defines rules
	#Index 0: UP
	#Index 1: LEFT
	#Index 2: DOWN
	#Index 3: RIGHT
	RULES = {BLUE: ((BLUE, GREEN), (BLUE),  (BLUE), (BLUE, GREEN)),
			 GREEN: ((GREEN), (GREEN, BLUE), (GREEN, BLUE), (GREEN))}

	#Stores final colour and possible colours
	finalColour = [NONE for x in range(outputXScale * outputYScale)]
	possibleColours = [(GREEN, BLUE) for x in range(outputXScale * outputYScale)]

	#Defines random colour for each coord
	coords = [randint(0, len(COLOURS) - 1) for x in range(outputXScale * outputYScale)]

	#Sets up tkinter
	root = tk.Tk()
	canvas = tk.Canvas(root, height = outputYScale + 10, width = outputXScale + 10)
	
	#Sets up image
	img = Image.new("RGB", (outputXScale, outputYScale))
	draw = ImageDraw.Draw(img)

	#Currently just adds random colours to all squares
	for x in range(int(outputXScale / 2)):
		for y in range(int(outputYScale / 2)):
			draw.rectangle([4*x,4*y,4*(x+1),4*(y+1)], fill = COLOURS[coords[getPixelID(x,y)]])

	#Displays the image
	image = ImageTk.PhotoImage(img)
	imagesprite = canvas.create_image((outputXScale + 10) / 2, (outputYScale + 10) / 2, image=image)
	canvas.pack()
	root.mainloop()