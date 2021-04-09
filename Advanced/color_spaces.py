import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Basics\images\CityParks.jpg')
img = cv2.resize(img, (600,450))
cv2.imshow("City Park", img)

# BGR to Grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# BGR to HSV
hsv = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# BGR to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

# BGR to RGB
bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('BGR --> RGB', bgr_to_rgb) 

# HSV to BGR
lab_to_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('LAB --> BGR', lab_to_bgr)

# HSV to BGR
hsv_to_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV --> BGR', hsv_to_bgr)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()
