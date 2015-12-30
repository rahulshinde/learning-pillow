
from PIL import Image
import sys

imageFileName = raw_input("enter the name of the image file: ")

im = Image.open("img/" + imageFileName)

pixdata = im.load()


for y in xrange(im.size[1]):
    for x in xrange(im.size[0]):
        if 200 < pixdata[x, y][0] or 100 < pixdata[x, y][1] or 50 < pixdata[x, y][2]:
            pixdata[x, y] = (0, 0, 0)
        else:
            pixdata[x, y] = (255, 255, 255)

im.convert('RGB')
im.save('img/out1.1.jpg', "JPEG")

for y in xrange(1, im.size[1]-1):
    for x in xrange(1, im.size[0]-1):
        if pixdata[x, y] == (0,0,0) and (pixdata[x + 1, y] == (255, 255, 255) or pixdata[x + 1, y + 1] == (255, 255, 255)):
            pixdata[x, y] = (0, 0, 0)
        else:
            pixdata[x, y] = (255, 255, 255)

im.convert('RGB')
im.save('img/out1.2.jpg', "JPEG")