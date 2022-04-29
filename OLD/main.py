from turtle import update
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from random import randint, choice

#Coord system:
# (0,3) (1,3) (2,3) (3,3)
# (0,2) (1,2) (2,2) (3,2)
# (0,1) (1,1) (2,1) (3,1)
# (0,0) (1,0) (2,0) (3,0)

#Function to get ID of a given pixel
def getPixelID(x, y):
	global outputXScale

	return int(x + outputXScale / 2 * y)

#Function to get pixel from given ID
def getPixelFromID(id):
	global outputXScale

	y = int(id // (outputXScale / 2))
	x = int(id % (outputXScale / 2))

	return x, y

#Function to find a random pixel ID with the lowest entropy
def getLowestEntropy(possibleColours):
	#List to store lowest entropy elements for random selection
	shortest = []

	#Gets the length of the shortest list
	shortestLength = len(min(possibleColours, key=len))

	#Find all elements with the lowest entropy
	for x in range(len(possibleColours)):
		if len(possibleColours[x]) == shortestLength:
			shortest.append(x)
	
	#Return random element from shortest
	toReturn = choice(shortest)
	while NONE in possibleColours[toReturn]:
		toReturn = choice(shortest)
	return toReturn

def updatePossibleColours(possibleColours, finalColour, updatedPixelID):
	global RULES, outputXScale, outputYScale

	#Pixels that should be edited next
	updatedPixels = []

	#Get coords of updated pixel
	updatedPixel = getPixelFromID(updatedPixelID)
	
	#Update entropy of left pixel
	if updatedPixel[0] != 0:
		leftPixel = getPixelID(updatedPixel[0] - 1, updatedPixel[1])
		updatedPixels.append(leftPixel)
		toTest = possibleColours[leftPixel]

		for x in toTest:
			validColours = RULES[x][3]
			if x not in validColours:
				if x != validColours:
					possibleColours[leftPixel].remove(x)
				

	#Update entropy of right pixel
	if updatedPixel[0] != outputXScale / 2:
		rightPixel = getPixelID(updatedPixel[0] + 1, updatedPixel[1])
		updatedPixels.append(rightPixel)
		toTest = possibleColours[rightPixel]

		for x in toTest:
			validColours = RULES[x][1]
			if x not in validColours:
				if x != validColours:
					possibleColours[rightPixel].remove(x)
		
	
	#Update entropy of above pixel
	if updatedPixel[0] != outputXScale / 2:
		abovePixel = getPixelID(updatedPixel[0], updatedPixel[1] + 1)
		updatedPixels.append(abovePixel)
		toTest = possibleColours[abovePixel]

		for x in toTest:
			validColours = RULES[x][2]
			if x not in validColours:
				if x != validColours:
					possibleColours[abovePixel].remove(x)

	
	#Update entropy of below pixel
	if updatedPixel[0] != outputXScale / 2:
		belowPixel = getPixelID(updatedPixel[0], updatedPixel[1] - 1)
		updatedPixels.append(belowPixel)
		toTest = possibleColours[belowPixel]
		
		for x in toTest:
			validColours = RULES[x][0]
			if x not in validColours:
				if x != validColours:
					possibleColours[belowPixel].remove(x)
	
	possibleColours[updatedPixelID] = [finalColour[updatedPixelID] for x in range(3)]
	
	return possibleColours
	return possibleColours, updatedPixels

if __name__ == "__main__":
	#Defines scale of output image
	outputXScale = 128
	outputYScale = 128

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
	finalColour = [NONE for x in range(int(outputXScale / 2 * outputYScale / 2))]
	possibleColours = [[GREEN, BLUE] for x in range(int(outputXScale / 2 * outputYScale / 2))]

	#Defines random colour for each coord
	coords = [randint(0, len(COLOURS) - 1) for x in range(outputXScale * outputYScale)]

	#Sets up tkinter
	root = tk.Tk()
	canvas = tk.Canvas(root, height = outputYScale + 10, width = outputXScale + 10)
	
	#Sets up image
	img = Image.new("RGB", (outputXScale, outputYScale))
	draw = ImageDraw.Draw(img)

	#Main loop
	while NONE in finalColour:
		pixelToEdit = getLowestEntropy(possibleColours)
		print(f"Editing {getPixelFromID(pixelToEdit)}, ID:{pixelToEdit}")
		colours = possibleColours[pixelToEdit]
		finalColour[pixelToEdit] = choice(colours)
		possibleColours = updatePossibleColours(possibleColours, finalColour, pixelToEdit)

	#Currently just adds random colours to all squares
	for x in range(int(outputXScale / 2)):
		for y in range(int(outputYScale / 2)):
			#draw.rectangle([4*x,4*y,4*(x+1),4*(y+1)], fill = COLOURS[coords[getPixelID(x,y)]])
			draw.rectangle([4*x,4*y,4*(x+1),4*(y+1)], fill = finalColour[getPixelID(x,y)])

	#Displays the image
	image = ImageTk.PhotoImage(img)
	imagesprite = canvas.create_image((outputXScale + 10) / 2, (outputYScale + 10) / 2, image=image)
	canvas.pack()
	root.mainloop()