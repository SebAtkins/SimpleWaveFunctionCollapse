from cgitb import text
from PIL import Image
import tiles

textures = tiles.getTextures()

for x in textures:
    print(x)