# Variables to edit
w, h = 50, 50
N = 3

# Imports
from cmath import pi
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from random import randint, choice, choices
import math

# Defines the colours
# 1: Blue
# 2: Green
# 3: Red
# 4: Mystery colour
colours = {
    1: (0, 0, 100),
    2: (0, 100, 0),
    3: (100, 0, 0),
    4: (100, 100, 0)
}
weights = {
    1: 120,
    2: 120,
    3: 40,
    4: 110
}

# Defines the rules
# 0: Up
# 1: Down
# 2: Left
# 3: Right
rules = {
    1: [[1, 3], [1, 3], [1, 3], [1, 3]],
    2: [[2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]],
    3: [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]],
    4: [[4, 2], [4, 2], [4, 2], [4, 2]]
}

# Defines the wave
wave = [[1, 2, 3, 4] for x in range(w * h)]

# Colours designated pixel
def colourPixel(x, y, col):
    global colours

    draw.rectangle([4*x, 4*y, 4*(x+0.75), 4*(y+0.75)], fill = colours[col], width = 0)

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
        entropy = len(wave[i])
        if lowestEntropy > entropy > 1:
            lowest.clear
            lowest.append(i)
            lowestEntropy = entropy
        elif entropy == lowestEntropy:
            lowest.append(i)
    
    if len(lowest) != 0:
        return choice(lowest)
    else:
        return False

# Make selection of colour of pixel
def updatePixel(id):
    global wave

    wave[id] = [choices(wave[id], k=1, weights = tuple(weights[i] for i in wave[id]))[0]]

    return True

# Update entropy of surrounding pixels
def updateEntropy(id):
    global wave

    # Find ID of various pixels
    ePixelCoord = pixelCoord(id)
    leftPixel = pixelID(ePixelCoord[0] - 1, ePixelCoord[1])
    rightPixel = pixelID(ePixelCoord[0] + 1, ePixelCoord[1])
    topPixel = pixelID(ePixelCoord[0], ePixelCoord[1] - 1)
    bottomPixel = pixelID(ePixelCoord[0], ePixelCoord[1] + 1)

    # Update left pixel
    if ePixelCoord[0] != 0:
        if len(wave[leftPixel]) != 1:
            for i in wave[leftPixel]:
                if wave[id][0] not in rules[i][3]:
                    wave[leftPixel].remove(i)

            # Update entropy if set to 0                    
            if len(wave[leftPixel]) == 1:
                wave = updateEntropy(leftPixel)
    
    # Update right pixel
    if ePixelCoord[0] != w - 1:
        if len(wave[rightPixel]) != 1:
            for i in wave[rightPixel]:
                if wave[id][0] not in rules[i][2]:
                    wave[rightPixel].remove(i)
            
            # Update entropy if set to 0                    
            if len(wave[rightPixel]) == 1:
                wave = updateEntropy(rightPixel)
    
    # Update top pixel
    if ePixelCoord[1] != 0:
        if len(wave[topPixel]) != 1:
            for i in wave[topPixel]:
                if wave[id][0] not in rules[i][1]:
                    wave[topPixel].remove(i)
            
            # Update entropy if set to 0                    
            if len(wave[topPixel]) == 1:
                wave = updateEntropy(topPixel)
    
    # Update bottom pixel
    if ePixelCoord[1] != h - 1:
        if len(wave[bottomPixel]) != 1:
            for i in wave[bottomPixel]:
                if wave[id][0] not in rules[i][0]:
                    wave[bottomPixel].remove(i)
            
            # Update entropy if set to 0                    
            if len(wave[bottomPixel]) == 1:
                wave = updateEntropy(bottomPixel)
    
    # Update image
    colourPixel(pixelCoord(id)[0], pixelCoord(id)[1], wave[id][0])
    
    return wave

# Determines if the code should continue running
def continueRunning():
    global wave

    lowestEntropy = math.inf
    lowest = []

    for i in range(len(wave)):
        entropy = len(wave[i])
        if lowestEntropy > entropy > 1:
            lowest.clear
            lowest.append(i)
            lowestEntropy = entropy
        elif entropy == lowestEntropy:
            lowest.append(i)
    
    if len(lowest) != 0:
        return True
    else:
        return False

# Updates the image to match the wave function
# Uncollapsed pixels are left blank
def updateImage():
    global wave, img, draw

    for i in range(len(wave)):
        if len(wave[i]) == 1:
            colourPixel(pixelCoord(i), wave[i][0])
    
    return True

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, height = h * 4 + 20, width = w * 4 + 20)
	
    # Sets up image
    img = Image.new("RGB", (w * 4, h * 4))
    draw = ImageDraw.Draw(img)

    # Displays the image
    image = ImageTk.PhotoImage(img)
    imagesprite = canvas.create_image(w * 2+ 10, h * 2 + 10, image=image)
    canvas.pack()

    # Main loop
    while continueRunning():
        i = getLowestEntropy()
        updatePixel(i)
        updateEntropy(i)

        # Display updated image
        image = ImageTk.PhotoImage(img)
        canvas.itemconfig(imagesprite, image = image)
        canvas.pack()
        root.update_idletasks()
        root.update()

    root.mainloop()