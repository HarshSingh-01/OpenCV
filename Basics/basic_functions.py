import cv2
import numpy as np

img = cv2.imread('Basics\images/CityParks.jpg')
cv2.imshow('Image', img)

# GrayScale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # or you can use '0' for graycale
cv2.imshow('Gray', gray)

# Blur
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

# Edge Cascade
canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Edge Cascade', canny)

# Dilating the image
dilated = cv2.dilate(canny, (7,7), iterations=3)
cv2.imshow('Dilated', dilated)

# Resize
resize = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized',resize)

# Cropping
cropped = img[50:200, 200:400]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)