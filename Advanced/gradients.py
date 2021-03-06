import cv2
import numpy as np

img = cv2.imread('Basics\images\CityParks.jpg')
img = cv2.resize(img, (600,400))
cv2.imshow('Park', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian', lap)

# Sobel
sobel_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combined_sobel = cv2.bitwise_or(sobel_x, sobel_y)

cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Combined Sobel', combined_sobel)

canny = cv2.Canny(gray, 150, 175)
cv2.imshow('Canny', canny)
 
cv2.waitKey(0)