import cv2 

img = cv2.imread('Basics\images\Kittens.jpg')
img = cv2.resize(img, (600,450))
cv2.imshow("Cats",img)

# Averaging 
average = cv2.blur(img, (3,3))
cv2.imshow("Average", average)

# Gaussian Blur
gauss = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv2.medianBlur(img, 3)
cv2.imshow('Median Blur', median)

# Bilateral
bilateral = cv2.bilateralFilter(img, 10, 35, 25)
cv2.imshow('Bilateral', bilateral)


cv2.waitKey(0)