from tkinter import *
import cv2
from PIL import ImageTk, Image

def camroll():
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            # print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # spaced

            cv2.imwrite(r"training_data\s1\train_image{}.png".format(img_counter),frame)

            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()

def inst():
    root=Toplevel()
    root.geometry("300x400")
    img = Image.open("download.png")
    img = img.resize((50, 50))
    img = ImageTk.PhotoImage(img)

    topframe = Frame(root, borderwidth=10, relief=RAISED)
    topframe.pack(expand=1)

    label1 = Label(topframe, text="FACE RECOGNITION SYSTEM")
    label1.pack(anchor="center")

    label2 = Label(topframe, image=img)
    label2.pack()
    frame=Frame(root,borderwidth=10)
    frame.pack(fill="both",expand="yes")
    labelframe=LabelFrame(frame,text="INSTRUCTION FOR REGISTER FACE")
    labelframe.pack(fill="both",expand="yes")
    left = Label(labelframe, text="Please read the instruction carefully !!")
    left.pack()
    label1=Label(labelframe,text="1. Click your image in all gesture one by one \n i.e. happy, sad ,angry ,and any expression")
    label1.pack(anchor=W)
    label2=Label(labelframe,text="2.Pls provide one person face .")
    label2.pack(anchor=W)
    label3=Label(labelframe,text="3.For click image pls press SPACE .")
    label3.pack(anchor=W)
    label4=Label(labelframe,text="4.For exit from camera prompt press ESC.")
    label4.pack(anchor=W)
    label5 = Label(labelframe, text="5.pls click atleast 10 images of your face.")
    label5.pack(anchor=W)
    label6 = Label(labelframe, text="6.At last close the prompt your image save \nsuceessfully")
    label6.pack(anchor=W)

    b1=Button(frame,text="Start!!",command=camroll)
    b1.pack(side=RIGHT)
    b2=Button(frame,text="Sumbit face!!",command=root.destroy)
    b2.pack(side=LEFT)


    root.mainloop()
