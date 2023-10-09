from PIL import Image
from PIL import ImageOps
from PIL import ImageColor
from PIL import ImageEnhance
import PIL

import random

inputImage = PIL.Image.open(input("Název vstupního souboru: "))

sharpnessTreshold = float(input("Hranice ostrosti (0-999+) [Doporučení 25]: ")) 
resFactor = float(input("Zmenšení rozlišení: (2 = 2x menší) [Doporučení 1]: "))
tresholdMult = float(input("Světlost (1-1) [Doporučení 0.8]: "))

enhancer = ImageEnhance.Sharpness(inputImage)
inputImage = enhancer.enhance(sharpnessTreshold)

resizedInput = inputImage.resize(tuple(round(ti/resFactor) for ti in inputImage.size))
grayscale = PIL.ImageOps.grayscale(resizedInput)
maxX, maxY = grayscale.size
output = PIL.Image.new("RGB", grayscale.size)

for X in range(maxX):
    for Y in range(maxY):
        pixelBrightness = grayscale.getpixel((X,Y))
        if(((pixelBrightness/255)>(random.random())*tresholdMult)):
            output.putpixel((X, Y), (255, 255, 255))

output.save("out.jpg")
