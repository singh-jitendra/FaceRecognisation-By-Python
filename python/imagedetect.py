import cv2


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

  
img=cv2.imread("opencv_frame_1.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
print(type(faces))
print(faces)
print(x)
print(y)
print(x+w)
print(y+w)
resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("detect",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
