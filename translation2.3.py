
from PIL import Image
import sys
import glob

files = glob.glob("img/1.jpg")
count = 0

for i in files:
    im = Image.open(i)
    pixdata = im.load()

    count += 1
    strCount = str(count)

    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if 185 < pixdata[x, y][0] or 185 < pixdata[x, y][1] or 185 < pixdata[x, y][2]:
                pixdata[x, y] = (0, 0, 0)
            else:
                pixdata[x, y] = (255, 255, 255)
    

    for y in xrange(1, im.size[1]-1):
        for x in xrange(1, im.size[0]-1):
            if pixdata[x, y] == (0,0,0) and (pixdata[x + 1, y] == (255, 255, 255) or pixdata[x + 1, y + 1] == (255, 255, 255) or pixdata[x, y + 1] == (255, 255, 255)):
                pixdata[x, y] = (0, 0, 255)
            elif pixdata[x, y] == (0,0,0) and (pixdata[x - 1, y] == (255, 255, 255) or pixdata[x - 1, y - 1] == (255, 255, 255) or pixdata[x, y - 1] == (255, 255, 255)): 
                pixdata[x, y] = (0, 0, 0)
            else:
                pixdata[x, y] = (255, 255, 255)

    im.convert('RGB')
    im.save('out/translation2.3/' + strCount + '.4.jpg', "JPEG")