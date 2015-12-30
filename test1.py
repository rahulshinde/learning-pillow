
from PIL import Image
import sys

im = Image.open("img/1.jpg")

pixdata = im.load()



for y in xrange(im.size[1]):
    for x in xrange(im.size[0]):
        if 252 < pixdata[x, y][0] or 252 < pixdata[x, y][1] or 252 < pixdata[x, y][2]:
            pixdata[x, y] = (0, 0, 0)
        else:
            pixdata[x, y] = (0, 0, 0)

im.show()