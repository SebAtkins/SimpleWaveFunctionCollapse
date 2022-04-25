# Variables to edit
w, h = 100, 100
N = 3

# Imports
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from random import randint, choice
import math

# Defines the colours
# 1: Blue
# 2: Green
# 3: Red
colours = {
    1: (0, 0, 100),
    2: (0, 100, 0),
    3: (100, 0, 0)
}

# Defines the rules
# 1: Up
# 2: Down
# 3: Left
# 4: Right
rules = {
    1: [[1, 3], [1], [1, 3], [1, 3]],
    2: [[2], [2, 3], [2, 3], [2, 3]],
    3: [[2, 3], [1, 3], [1, 2, 3], [1, 2, 3]]
}

# Defines the wave
wave = [[1, 2, 3] for x in range(w * h)]

# Colours designated pixel
def colourPixel(x, y, col):
    global colours

    draw.rectangle([4*x, 4*y, 4*(x+1), 4*(y+1)], fill = colours[col])

    return True

# Returns ID of pixel
def pixelID(x, y):
    global w, h

    return x + w * y

# Returns coordinates from ID
def pixelCoord(id):
    global w, h

    return id % w, id // w

# Select pixel with low entropy
# Returns ID of said pixel
def getLowestEntropy():
    global wave

    lowestEntropy = math.inf
    lowest = []

    for i in range(len(wave)):
        entropy = wave[i]
        if lowestEntropy > entropy > 1:
            lowest.clear
            lowest.append(i)
        elif entropy == lowestEntropy:
            lowest.append(i)
    
    return choice(lowest)

# Make selection of colour of pixel
def updatePixel(id):
    global wave

    

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, height = h * 4 + 20, width = w * 4 + 20)
	
    # Sets up image
    img = Image.new("RGB", (w * 4, h * 4))
    draw = ImageDraw.Draw(img)

    # Main loop

    # Displays the image
    image = ImageTk.PhotoImage(img)
    imagesprite = canvas.create_image(w * 2+ 10, h * 2 + 10, image=image)
    canvas.pack()
    root.mainloop()