import qrcode
import cv2

img = cv2.imread('qrcode.png')
qr = cv2.QRCodeDetector()
