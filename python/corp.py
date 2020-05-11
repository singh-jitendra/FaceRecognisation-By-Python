import cv2
import numpy as np
import matplotlib
img =cv2.imread("opencv_frame_1.png")
corp=img[263:426,374:537]
cv2.imshow("test",corp)
basehsv = cv2.cvtColor(corp,cv2.COLOR_BGR2HSV)
cv2.imshow("tes1t",basehsv)
