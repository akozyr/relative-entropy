'''
from PIL import Image
import numpy as np

im = Image.open('5.png')
im = im.convert('L')
imArr = np.asarray(im)
invertedArr = np.linalg.inv(imArr)

print(invertedArr)
'''
# np.savetxt('matrix.txt', invertedArr)

'''
processedImage = Image.fromarray(invertedArr)
processedImage.convert('RGB').save('processedIm.png')
processedImage.show()
'''
import math
from PIL import Image

imageFile = 'lena.bmp'
print(imageFile)
im = Image.open(imageFile)
rgbHistogram = im.histogram()
print('Snannon Entropy for Red, Green, Blue:')
for rgb in range(3):
     totalPixels = sum(rgbHistogram[rgb * 256 : (rgb + 1) * 256])
     ent = 0.0
     for col in range(rgb * 256, (rgb + 1) * 256):
         freq = float(rgbHistogram[col]) / totalPixels
         if freq > 0:
             ent = ent + freq * math.log(freq, 2)
     ent = -ent
     print(ent)

