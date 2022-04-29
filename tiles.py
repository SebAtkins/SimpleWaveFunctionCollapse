from PIL import Image
from tileReader import *

# Generates the textures that will be used in other documents
def getTextures():
    """Generates textures, returns a dictionary"""
    textures = {}
    defSockets = genSockets()

    for i in range(3):
        for r in range(4):
            sockets = defSockets[i]
            img = Image.open(f"tilemap/tilemap{i}.png")
            for rotations in range(r):
                sockets = rotateSocketsAntiClockwise(sockets)
                img = img.rotate(90)
            textures[f"{i}{r}"] = [sockets, img]
    
    textures["30"] = [defSockets[3], Image.open("tilemap/tilemap3.png")]
    textures["31"] = [rotateSocketsAntiClockwise(defSockets[3]), Image.open("tilemap/tilemap3.png").rotate(90)]

    textures["40"] = [defSockets[4], Image.open("tilemap/tilemap4.png")]
    textures["50"] = [defSockets[5], Image.open("tilemap/tilemap5.png")]

    return textures