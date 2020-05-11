import cv2
import numpy as np
#from PIL import Image

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "jitu{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter=img_counter+1

cam.release()

cv2.destroyAllWindows()
i=0
while i<img_counter:
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

      
    img=cv2.imread("jitu{}.png".format(i))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    print(type(faces))
    print(faces)
    p=(x)
    q=(y)
    r=(x+w)
    s=(y+h)
    resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
    cv2.imshow("detect",resized)
    #imageobject=Image.open("jitu{}.png".format(i))
    #cropped -imageobject.corp((p,q,r,s))
    #cropped.show()



    img = cv2.imread("jitu{}.png".format(i),0)
    mask=np.zeros(img.shape[:2],np.uint8)
    mask[q:s,p:r]=255#mask[y:y+h , x:x+w]
    masked_img=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("masked",masked_img)
    i+=1
cv2.waitKey(0)
cv2.destroyAllWindows()


