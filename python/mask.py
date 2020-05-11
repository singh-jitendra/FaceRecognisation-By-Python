import cv2
import numpy as np

img = cv2.imread("15.jpg",0)
mask=np.zeros(img.shape[:2],np.uint8)
mask[72:202,69:199]=255
masked_img=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("masked",masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
