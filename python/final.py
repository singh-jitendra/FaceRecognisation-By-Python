import cv2
import sys
import numpy as np



def image_capture():
    cam=cv2.VideoCapture(0)
    #cv2.nameWindows("capturing_image")
    global img_counter
    while True:
        ret,frame = cam.read()
        cv2.imshow("capturing_image",frame)
        if not ret:
            break
        
        k=cv2.waitKey(1)
        
        if k%256 == 27:
        # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "test{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter+=1
          
            break
    return img_name

    cam.release()

    cv2.destroyAllWindows()


def face_detect(img_test):
    
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

      
    img=cv2.imread(img_test)
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
    return p,q,r,s

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def corp(img_test,p,q,r,s):
    img = cv2.imread(img_test)
    crop_img = img[q:s,p:r]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    
def masking(img_test,p,q,r,s):
    img = cv2.imread(img_test,0)
    mask=np.zeros(img.shape[:2],np.uint8)
    mask[q:s,p:r]=255#mask[y:y+h , x:x+w]
    masked_img=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("masked",masked_img)
    cv2.imwrite(img_test,0)
    print("complete")
    return img_test
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    
def compare_histogram(img_test1,img_test2):
    #reading the images and convert them to HSV
    base = cv2.imread(img_test1)
    test1 = cv2.imread(img_test2)
    basehsv = cv2.cvtColor(base,cv2.COLOR_BGR2HSV)
    test1hsv = cv2.cvtColor(test1,cv2.COLOR_BGR2HSV)

    # Calculate the Hist for each images
    histbase = cv2.calcHist(basehsv,[0],None,[256],[0,256])
    cv2.normalize(histbase,histbase,0,255,cv2.NORM_MINMAX)
    histtest1 = cv2.calcHist(test1hsv,[0],None,[256],[0,256])
    cv2.normalize(histtest1,histtest1,0,255,cv2.NORM_MINMAX)

    # Compare two Hist. and find out the correlation value
    base_test1 = cv2.compareHist(histbase,histtest1,0)
    print (base_test1)

img_counter=0  
img_test=image_capture()
p,q,r,s=face_detect(img_test)
#img_test1=masking(img_test,p,q,r,s)
img_test1=corp(img_test,p,q,r,s)
img_test=image_capture()
p,q,r,s=face_detect(img_test)
#img_test2=masking(img_test,p,q,r,s)
img_test2=corp(img_test,p,q,r,s)
compare_histogram(img_test1,img_test2)


    
        


        
