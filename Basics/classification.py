import cv2
import numpy as np

def draw_on_img(image):
    img = cv2.imread(image)
    tl = round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = [np.random.randint(0, 255) for _ in range(3)]
    h, w, c = img.shape
    label = "Weapon: 99%"
    
    x, y, x1, y1 = 0, 0, int(w*0.10), int(h*0.035)
    c1, c2 = (x, y), (x1, y1)
    tf = max(tl - 1, 1)
    t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
    c2 = c1[0] + t_size[0], c1[1] + t_size[1] + int(3.5*tl)
    
    cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
    cv2.putText(img, label, (c1[0], y1), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
    
    
    cv2.imshow("Image", img)
    if cv2.waitKey(0) & 0xFF==ord('q'):
        cv2.destroyAllWindows()



draw_on_img("/Users/harsh/Desktop/ML Ops/Computer Vision/opencv/OpenCV/Basics/images/CityParks.jpg")