import cv2

# Rescale Function for saved videos and images
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (height, width)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

# For live video feeds
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


# Reading Image
img = cv2.imread('Basics\images/download.jpg')
resized_img = rescaleFrame(img)

cv2.imshow('Image', img) # Normal image
cv2.imshow('Resized_img', resized_img) # Resized_image

cv2.waitKey(0)

# Reading video
capture = cv2.VideoCapture('G:\\TV Series\Anime\Full Metal Alchemist Brotherhood/Full Metal Alchemist - 01 To Challenge the Sun (engdub).avi')

while True:
    isTrue, frame = capture.read()

    resized_frame = rescaleFrame(frame)

    cv2.imshow('Video', frame) # Normal Video
    cv2.imshow('Resized_video', resized_frame) # Resized_video

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
