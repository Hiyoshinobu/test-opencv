import cv2
import time

img = cv2.imread("venv/Ressources/Image1.jpg")

scale_percent = 50

width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dsize = (width, height)
img = cv2.resize(img, dsize)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ksize = (7,7)
imgBlur = cv2.GaussianBlur(imgGray, ksize,0)

imgCanny = cv2.Canny(img, 100, 100)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("jaaj", imgGray - imgBlur)

cv2.waitKey(0)




