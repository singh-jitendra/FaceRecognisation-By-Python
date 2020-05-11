import cv2


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)

while True:
    check,frame=video.read()
#img=cv2.imread("jitu.jpg")
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #print(type(faces))
    #print(faces)
#resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
    cv2.imshow("detect",frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break

video.release()
cv2.destroyAllWindows()
