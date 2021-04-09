import cv2
import numpy as np

blank = np.zeros(shape=(400,400),dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('Circle',circle)

# bitwise AND --> intersecting regions
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('Bitwise AND', bitwise_and)

# bitwise OR --> non-interesting and interesting regions
bitwise_or = cv2.bitwise_or(rectangle,circle)
cv2.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR --> non-interesting regions
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('Bitwise XOR', bitwise_xor)

cv2.waitKey(0)