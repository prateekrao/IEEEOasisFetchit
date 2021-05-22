import cv2
import numpy as np

def detect(video):

    capture = cv2.VideoCapture(video)

    while True:
        frame, image = capture.read()

        shape = image.shape
        h = shape[0]
        w = shape[1]

        gauss_image = cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)

        hsvimage = cv2.cvtColor(gauss_image, cv2.COLOR_BGR2HSV)

        ly = np.array([14, 47, 53], dtype = 'uint8')
        uy = np.array([27, 253, 255], dtype= 'uint8')

        mask = cv2.inRange(hsvimage, ly, uy)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        cv2.imshow('cont', mask)
        cv2.waitKey(0)
