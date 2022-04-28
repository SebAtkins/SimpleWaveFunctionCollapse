from PIL import Image
import sys

def genSockets():
    """
    genSockets() and returns a dictionary

    Generates the sockets from images
    Does not calculate rotations 
    Returns {n: [topSocket, bottomSocket, leftSocket, rightSocket]}
    """
    sockets = {}

    for i in range(6):
        img = Image.open(f"tilemap/tilemap{i}.png")

        sockets[i] = [0, 0, 0, 0]

        px = img.load()
        
        # Define top socket
        if px[7,0] == px[8,0] == px[9,0] == px[6,0] == (128, 128, 128, 255):
            sockets[i][0] = 1

        # Define bottom socket
        if px[7,15] == px[8,15] == px[9,15] == px[6,15] == (128, 128, 128, 255):
            sockets[i][1] = 1
        
        # Define left socket
        if px[0,6] == px[0,7] == px[0,8] == px[0,9] == (128, 128, 128, 255):
            sockets[i][2] = 1
        
        # Define right socket
        if px[15,6] == px[15,7] == px[15,8] == px[15,9] == (128, 128, 128, 255):
            sockets[i][3] = 1

    return sockets

def rotateSocketsClockwise(list):
    """
    rotateSocketsClockwise(list) and return a list

    Rotates the passed list clockwise by 90 degrees
    """
    list[0], list[1], list[2], list[3] = list[2], list[3], list[1], list[0]

    return list

def rotateSocketsAntiClockwise(list):
    """
    rotateSocketsAntiClockwise(list) and return a list

    Rotates the passed list anti-clockwise by 90 degrees
    """
    list[0], list[1], list[2], list[3] = list[3], list[2], list[0], list[1]

    return list