import cv2
import numpy as np

#reading the images and convert them to HSV
base = cv2.imread('151.jpg')
test1 = cv2.imread('152.jpg')
basehsv = cv2.cvtColor(base,cv2.COLOR_BGR2HSV)
test1hsv = cv2.cvtColor(test1,cv2.COLOR_BGR2HSV)

# Calculate the Hist for each images
histbase = cv2.calcHist(basehsv,[0],None,[256],[0,256])
cv2.normalize(histbase,histbase,0,255,cv2.NORM_MINMAX)
histtest1 = cv2.calcHist(test1hsv,[0],None,[256],[0,256])
cv2.normalize(histtest1,histtest1,0,255,cv2.NORM_MINMAX)
cv2.imshow("haa",basehsv)
cv2.imshow("haa1",test1hsv)

# Compare two Hist. and find out the correlation value
base_test1 = cv2.compareHist(histbase,histtest1,0)
print (base_test1)
