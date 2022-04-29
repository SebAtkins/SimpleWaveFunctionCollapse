import tiles
from math import inf
from random import choice

class wave:
    def __init__(self, w: int = 50, h: int = 50):
        """Takes w (width) and h (height)"""
        self.w = w
        self.h = h

    # Returns ID of pixel
    def pixelID(self, x: int, y: int):
        """Finds ID of pixel, returns ints"""
        return x + self.w * y

    # Returns coordinates from ID
    def pixelCoord(self, id: int):
        """Finds coords of pixel, returns (w, h)"""
        return id % self.w, id // self.w

    # Finds pixel with lowest entropy, returns ID of said pixel
    def getLowestEntropy(self):
        """
        Finds pixel with lowest entropy and returns ID (int) / False

        Returns the ID of the pixel with lowest entropy.
        If all pixels collapsed returns False
        """

        lowestEntropy = inf
        lowest = []

        for i in range(len(self.wave)):
            entropy = len(self.wave[i])
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
    def updatePixel(self, id: int):
        """Updates pixel to a random possible option, returns Bool"""
        try:
            self.wave[id] = [choice(self.wave[id])]

            return True
        except:
            return False

    def generate(self):
        """Runs the generation, returns True"""
        # Generate textures and sockets
        self.textures = tiles.getTextures()

        # Define initial wave
        self.wave = [[j for j in self.textures] for i in range(self.w * self.h)]

        return True

if __name__==("__main__"):
    wave = wave(50, 50)
    wave.generate()