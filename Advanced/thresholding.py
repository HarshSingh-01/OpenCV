import cv2

img = cv2.imread('Basics\images\Kittens.jpg')
img = cv2.resize(img, (600,400))
cv2.imshow("Cats", img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv2.threshold(src=gray, thresh=150, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow("Simple Threshold", thresh)

threshold, thresh_inv = cv2.threshold(src=gray, thresh=150, maxval=255, type=cv2.THRESH_BINARY_INV)
cv2.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        thresholdType=cv2.THRESH_BINARY_INV, blockSize=11,C=9)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)

cv2.waitKey(0)
