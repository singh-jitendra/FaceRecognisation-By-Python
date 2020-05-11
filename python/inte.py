import cv2
import sys
import numpy as np
#face_cascade=sys.argv[0]
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
img_counter=1

while True:
    check,frame=video.read()
#img=cv2.imread("jitu.jpg")
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    print(type(faces))
    print(faces)
#resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
    cv2.imshow("detect",frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        img_name = "jitu{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        break

video.release()
cv2.destroyAllWindows()
for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
img = cv2.imread(img_name,0)
mask=np.zeros(img.shape[:2],np.uint8)
mask[x:x+w,y:y+h]=255
masked_img=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("masked",masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

