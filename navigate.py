import cv2
import numpy as np

def detect(video):

    capture = cv2.VideoCapture(video)

    while True:
        frame, image = capture.read()

        gauss_image = cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)

        hsvimage = cv2.cvtColor(gauss_image, cv2.COLOR_BGR2HSV)

        ly = np.array([14, 47, 53], dtype = 'uint8')
        uy = np.array([27, 253, 255], dtype= 'uint8')

        mask = cv2.inRange(hsvimage, ly, uy)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
        for _, c in enumerate(contours):
            x,y,w,h= cv2.boundingRect(c)
                
            x0, y0 = ((x * 1.75 + w) / 2, (y * 1.75 + h) / 2)
            x= 0
            y= 0

            if (x-x0) != 0:
                m = (y-y0)/(x-x0)
            
            if m > 0.1:
                cv2.putText(image,"Move LEFT", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,255))

            elif m < -0.1:
                cv2.putText(image, "Move RIGHT", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255))

            else:
                cv2.putText(image, "Move STRAIGHT", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1 ,(255,255,0))

        cv2.imshow('navigate', image)    
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

