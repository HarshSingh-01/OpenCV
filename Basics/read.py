import cv2

# Reading Images
img = cv2.imread('Basics\images/download.jpg') 
cv2.imshow('Dog', img) # Dog is the window name and variable img that stores the reded image in it.

cv2.waitKey(0)

# Reading Videos
capture = cv2.VideoCapture('G:\\TV Series\Anime\Full Metal Alchemist Brotherhood/Full Metal Alchemist - 01 To Challenge the Sun (engdub).avi')

while True:
    isTrue, frame = capture.read()

    cv2.imshow('Video', frame) # Video is the window name and variable frame is the capture frames

    if cv2.waitKey(40) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()