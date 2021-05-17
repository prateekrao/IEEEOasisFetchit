import cv2
import numpy as np

# BGR values of all colors
RED = (0, 255, 0)
GREEN = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 128, 0)
ORANGE = (0, 255, 165)
GREY = (128, 128, 128)
TURQUOISE = (208, 64, 224)

#TODO: These colors should be given from readQR.py
start = 'red'
stop = 'blue'
path = 'green'

colorMatch = ['red':RED, 'blue':BLUE, 'green':GREEN]

start = colorMatch[start]
stop = colorMatch[stop]
path = colorMatch[path]

#TODO: create a lower and upper limit for the colors +-30

cv2.namedWindow('Original vid')

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    #image = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((3, 3), np.uint8)

    mask_start = cv2.inRange(hsv, lwr_start, upper_start)
    mask_start = cv2.dilate(mask_start, kernel, iterations=33)

    mask_stop = cv2.inRange(hsv, lwr_stop, upper_stop)
    mask_stop = cv2.dilate(mask_stop, kernel, iterations=33)

    mask_path = cv2.inRange(hsv, lwr_path, upper_path)
    mask_path = cv2.dilate(mask_path, kernel, iterations=33)

    #TODO: show all masks and test with the colors

    cv2.imshow('image', frame)

    key = cv2.waitKey(100)
    if key == 27:
        break
