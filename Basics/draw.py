import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # Creating a blank image of shape 500x500 with 3 color channels
cv2.imshow('Blank', blank)

# 1. Paint the image a certain colour 
blank[200:300, 300:400] = 0,255,0
cv2.imshow('Green', blank)

# 2. Draw a Rectangle
# cv2.rectangle(image, start_point, end_point, colour, thickness)
cv2.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) # If thickness is -1, it will the shape completely
cv2.imshow('Rectangle', blank)

# 3. Draw a circle
# cv2.circle(image, cordiantes, radius, colour, thickness)
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv2.imshow('Circle', blank)

# 4. Draw a line
# cv2.line(image, start_point , end_point, colour, thickness)
cv2.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv2.imshow('Line', blank)

# 5. Write text
# cv2.putText(image, text, org, fontFace, fontScale, color, thickness)
cv2.putText(blank, 'Hello, My name is Harsh', (0,255), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv2.imshow('Text', blank)

cv2.waitKey(0)
