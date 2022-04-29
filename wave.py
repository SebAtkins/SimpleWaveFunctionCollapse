import tiles, display
from math import inf
from random import choice
from PIL import Image

class wave:
    """
    Class used for generation of images via wavefront collapse

    Functions:
    - generate()
    - new = wave(width, height)    
    """

    # Constructor
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

    # Updates entropy of surrounding pixels, wraps around
    def updateEntropy(self, id: int):
        """Update entropy of pixels, wraps around screen, returns True"""
        coords = self.pixelCoord(id)

        # Update left pixel's entropy
        leftPixel = self.pixelID((coords[0] - 1) % self.w, (coords[1]) % self.h)
        if len(self.wave[leftPixel]) != 1:
            for i in self.wave[leftPixel]:
                if self.textures[i][0][3] != self.textures[self.wave[id][0]][0][2]:
                    self.wave[leftPixel].remove(i)
            if len(self.wave[leftPixel]) == 1:
                self.updateEntropy(leftPixel)
        
        # Update right pixel's entropy
        rightPixel = self.pixelID((coords[0] + 1) % self.w, (coords[1]) % self.h)
        if len(self.wave[rightPixel]) != 1:
            for i in self.wave[rightPixel]:
                if self.textures[i][0][2] != self.textures[self.wave[id][0]][0][3]:
                    self.wave[rightPixel].remove(i)
            if len(self.wave[rightPixel]) == 1:
                self.updateEntropy(rightPixel)
        
        # Update top pixel's entropy
        topPixel = self.pixelID((coords[0]) % self.w, (coords[1] + 1) % self.h)
        if len(self.wave[topPixel]) != 1:
            for i in self.wave[topPixel]:
                if self.textures[i][0][1] != self.textures[self.wave[id][0]][0][0]:
                    self.wave[topPixel].remove(i)
            if len(self.wave[topPixel]) == 1:
                self.updateEntropy(topPixel)
        
        # Update bottom pixel's entropy
        bottomPixel = self.pixelID((coords[0]) % self.w, (coords[1] - 1) % self.h)
        if len(self.wave[bottomPixel]) != 1:
            for i in self.wave[bottomPixel]:
                if self.textures[i][0][0] != self.textures[self.wave[id][0]][0][1]:
                    self.wave[bottomPixel].remove(i)
            if len(self.wave[bottomPixel]) == 1:
                self.updateEntropy(bottomPixel)
        
        self.updatePixel(id)

        return True
    
    # Updates the image to show the collapsed pixel
    def updatePixel(self, id: int):
        """Updates image to collapsed value, returns True"""

        coords = self.pixelCoord(id)

        self.img.paste(self.textures[self.wave[id][0]][1], (coords[0] * 16, coords[1] * 16))

        return True

    def generate(self):
        """Runs the generation, returns True"""
        # Generate textures and sockets
        self.textures = tiles.getTextures()

        # Define initial wave
        self.wave = [[j for j in self.textures] for i in range(self.w * self.h)]

        # Create image
        self.img = Image.new("RGB", [self.w * 16, self.h * 16], "black")

        # Create screen
        self.screen = display.display(self.w, self.h, self.img)

        self.screen.update(self.img)

        # Main loop
        while i:=self.getLowestEntropy():
            self.updatePixel(i)
            self.updateEntropy(i)
            self.screen.update(self.img)

        print("swag")

        self.screen.main()

        return True

if __name__==("__main__"):
    wave = wave(32, 32)
    wave.generate()