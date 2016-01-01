
from PIL import Image
import sys
import glob

files = glob.glob("img/*.jpg")
count = 0

for i in files:
    im = Image.open(i)
    pixdata = im.load()

    width = im.size[0]
    height = im.size[1]

    newIm = Image.new("RGB", (width, height))
    newData = newIm.load()

    count += 1
    strCount = str(count)

    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if 180 < pixdata[x, y][0]:
                pixdata[x, y] = (0, 255, 0)
            elif 180 < pixdata[x, y][1]:
                pixdata[x, y] = (255, 0, 0)
            elif 180 < pixdata[x, y][2]:
                pixdata[x, y] = (0, 0, 255)
            elif pixdata[x, y][0] >= 180 and 100 < pixdata[x, y][0]:
                pixdata[x, y] = (200, 20, 100)
            elif pixdata[x, y][1] >= 180 and 100 < pixdata[x, y][1]:
                pixdata[x, y] = (200, 0, 200)
            elif pixdata[x, y][2] >= 180 and 100 < pixdata[x, y][2]:
                pixdata[x, y] = (0, 220, 0)
            elif pixdata[x, y][0] >= 100:
                pixdata[x, y] = (0, 10, 215)
            elif pixdata[x, y][1] >= 100:
                pixdata[x, y] = (0, 200, 0)
            else:
                pixdata[x, y] = (202, 0, 100)

    im.convert('RGB')
    im.save('out/color/' + strCount + '.jpg', "JPEG")