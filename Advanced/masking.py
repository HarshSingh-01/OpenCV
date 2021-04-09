import cv2
import numpy as np

img = cv2.imread('Basics\images\Kittens.jpg')
img = cv2.resize(img, (600,450))
cv2.imshow('Kittens', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('Blank Image', blank)

circle = cv2.circle(blank.copy(), (img.shape[1]//2 + 20 , img.shape[0]//2 + 20), 80, 255, -1)
rectangle = cv2.rectangle(blank.copy(), (50,50), (350,350), 255, -1)

cv2.imshow('Circle', circle)
cv2.imshow('Rectangle', rectangle)

weird_shape = cv2.bitwise_and(circle, rectangle)
cv2.imshow('Weird Shape', weird_shape)

masked = cv2.bitwise_and(img,img,mask=weird_shape) # mask can be circle or rectangle
cv2.imshow('Weird Shaped Masked Image', masked)

cv2.waitKey(0)