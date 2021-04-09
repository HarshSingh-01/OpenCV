import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Basics\images\Cats.jpg')
img = cv2.resize(img, (600,450))
cv2.imshow('Kittens', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

mask = cv2.circle(blank, (img.shape[1]//2 + 120,img.shape[0]//2 - 80), 100, 255, -1)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Masked Image', masked)

# Grayscale histogram
gray_hist = cv2.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Colour Histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv2.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv2.waitKey(0)