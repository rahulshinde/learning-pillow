
from PIL import Image
import sys
import glob

files = glob.glob("img/1.jpg")
count = 0

for i in files:
    im = Image.open(i)
    pixdata = im.load()

    width, height = im.size()

    newIm = Image.new("RGB", (width, height))
    newData = newIm.load()

    count += 1
    strCount = str(count)

    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if 100 < pixdata[x, y][0] or 100 < pixdata[x, y][1] or 100 < pixdata[x, y][2]:
                pixdata[x, y] = (0, 0, 0)
            else:
                pixdata[x, y] = (255, 255, 255)

    for y in xrange(1, im.size[1]-1):
        for x in xrange(1, im.size[0]-1):
            if pixdata[x, y] == (0,0,0) and (pixdata[x + 1, y] == (255, 255, 255) or pixdata[x + 1, y + 1] == (255, 255, 255) or pixdata[x, y + 1] == (255, 255, 255) or pixdata[x - 1, y] == (255, 255, 255) or pixdata[x - 1, y - 1] == (255, 255, 255) or pixdata[x, y + 1] == (255, 255, 255) or pixdata[x - 1, y + 1] == (255, 255, 255) or pixdata[x + 1, y - 1] == (255, 255, 255)):
                newData[x, y] = (0, 0, 0)
            else:
                newData[x, y] = (255, 255, 255)

    newIm.convert('RGB')
    newIm.save('out/outliner/' + strCount + '.jpg', "JPEG")