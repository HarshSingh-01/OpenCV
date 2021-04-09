import cv2
import numpy as np

img = cv2.imread('Basics\images\CityParks.jpg')
cv2.imshow('Image', img)

# Translation 
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimesions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(src=img, M=transMat, dsize=dimesions) # The function warpAffine transforms the source image using the specified matrix

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translate = translate(img , -100, 100)
cv2.imshow('Translated', translate)

# Rotation
def rotate(img, angle=0, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(src=img, M=rotMat, dsize=dimensions)

rotated = rotate(img, angle=-90)
cv2.imshow('Rotated', rotated)

# Resizing
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resize', resized)

# Cropping
cropped = img[200:300, 300:400]
cv2.imshow('Cropped', cropped)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()