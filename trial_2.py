import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


images = [cv2.imread(file) for file in glob.glob("C:/Users/nada/Desktop/ROV Competition/task 3 - subway car/*.png")]
resized = []
X_long = 290*2
X_short = 290
Y = 290
for im in images:
    y, x = im.shape[0],im.shape[1]
    if x>=500 & y<250:
        resized.append(cv2.resize(im, (X_long, Y), interpolation = cv2.INTER_CUBIC))
    else:
        resized.append(cv2.resize(im, (X_short, Y), interpolation = cv2.INTER_CUBIC))
i=0
for img in resized:
    cv2.imwrite("res"+str(i)+".jpg", resized[i])
    i = i+1
    
# Vertically added: 
I1 = Image.open("res1.jpg")
I2 = Image.open("res4.jpg")
im = Image.new('RGB', (X_long, (I1.height + I2.height)),(255,255,255)).save("out.jpg")
out = Image.open("out.jpg")

out.paste(I2,(0,0))
out.save("out.jpg")
out = Image.open("out.jpg")
out.paste(I1,(0,I2.height))
out.save("out.jpg")
out = cv2.imread("out.jpg")
#
# Horizontally added:
#I1 = Image.open("res0.jpg")
#I2 = Image.open("out1.jpg")

#im = Image.new('RGB', ((I1.width+I2.width),(I2.height+10)),(255,255,255)).save("out1.jpg")
#out = Image.open("out1.jpg")
#out.paste(I2,(I1.width,0))
#out.save("out1.jpg")

#out = Image.open("out1.jpg")
#out.paste(I1,(0,I2.height))
#out.save("out1.jpg")

# Horizontally added - stage 2:
#I1 = Image.open("out1.jpg")
#I2 = Image.open("res2.jpg")

#im = Image.new('RGB', ((I1.width+I2.width), I1.height,),(255,255,255)).save("out1.jpg")
#out = Image.open("out1.jpg")
#out.paste(I1,(0,0))
#out.save("out1.jpg")

#out = Image.open("out1.jpg")
#out.paste(I2,(I1.width,0))
#out.save("out1.jpg")
out = cv2.imread("out.jpg")

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
