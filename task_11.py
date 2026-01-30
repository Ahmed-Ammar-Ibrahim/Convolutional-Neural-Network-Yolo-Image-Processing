import cv2
from skimage.measure import compare_ssim
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imgs
import imutils

original = cv2.imread('origin_2.jpg')
changed = cv2.imread('aligned.jpg')

# changed = cv2.resize(changed, (original.shape[1], original.shape[0]), interpolation=cv2.INTER_CUBIC)
original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
changed_gray = cv2.cvtColor(changed, cv2.COLOR_BGR2GRAY)

lower_gray = np.array([25, 25, 25])
upper_gray = np.array([151, 151, 151])
upper_gray_2 = np.array([185, 185, 185])

mask_1 = cv2.inRange(original, lower_gray, upper_gray)
mask_2 = cv2.inRange(changed, lower_gray, upper_gray_2)

# remove the background from the image

masked_image_1 = np.copy(original)
masked_image_2 = np.copy(changed)
masked_image_1[mask_1 != 0] = [0, 0, 0]
masked_image_2[mask_2 != 0] = [0, 0, 0]


green = cv2.subtract(masked_image_1, masked_image_2)

# convert the color to grayscale kont bgrab 7aga :D
original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
changed_gray = cv2.cvtColor(changed, cv2.COLOR_BGR2GRAY)

green_gray = cv2.cvtColor(green, cv2.COLOR_RGB2GRAY)
# threshold byen mask1 wa mask2
h1, thresh1 = cv2.threshold(green_gray, 0, 255, cv2.THRESH_BINARY)

h, thresh = cv2.threshold(cv2.subtract(mask_1, mask_2), 200, 255, cv2.THRESH_BINARY)

cnts_1 = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_1 = imutils.grab_contours(cnts_1)

cnts_1 = sorted(cnts_1, key=cv2.contourArea, reverse=True)[:1]

cnts_2 = cv2.findContours(thresh1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts_2 = imutils.grab_contours(cnts_2)
cnts_2 = sorted(cnts_2, key=cv2.contourArea, reverse=True)[:2]

for c in cnts_1:
    # compute the bounding box of the contour and then draw
    # bounding box on both input images to represent where the two

    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(original, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(changed, (x, y), (x + w, y + h), (0, 0, 255), 2)

for c in cnts_2:
    # compute the bounding box of the contour and then draw
    # bounding box on both input images to represent where the two

    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(original, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(changed, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("original", np.hstack([original, changed]))

cv2.waitKey(0)