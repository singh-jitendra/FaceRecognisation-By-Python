import cv2,time
video=cv2.VideoCapture(0)
while True:
    
    check,frame =video.read()

    print(check)

    print(frame)

    #time.sleep(5)

    cv2.imshow("capturing",frame)

    key=cv2.waitKey(1)
    if key==ord("q"):
        break
     

video.release()

cv2.destroyAllWindows()
