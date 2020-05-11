import cv2
from tkinter import *

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
           if k%256 == 27:
               # ESC pressed
               #print("Escape hit, closing...")
               break
           elif k%256 == 32:
               # SPACE pressed
               img_name = "train_image{}.png".format(img_counter)
               cv2.imwrite(img_name, frame)
               #print("{} written!".format(img_name))
               img_counter += 1
       cam.release()
       cv2.destroyAllWindows()

rooot=Tk()

topframe=Frame(rooot,borderwidth=10,relief=RAISED)
topframe.pack(expand=1)

bottomframe=Frame(rooot,borderwidth=10)
bottomframe.pack(expand=1,side=BOTTOM)


label0=Label(topframe,text="FACE RECOGNITION SYSTEM")
label0.pack(anchor="center")

img=Image.open("download.png")
img=img.resize((50,50))
img =ImageTk.PhotoImage(img)

labe=Label(topframe,image=img)
labe.pack()

label1=Label(topframe,text="REGISTRATION")
label1.pack(anchor="center")

label2=Label(bottomframe,text="NAME")
label2.grid(row=0,column=0)

titletext=StringVar()

e2=Entry(bottomframe,textvariable=titletext)
e2.grid(row=0,column=1)

label3=Label(bottomframe,text="USER NAME")
label3.grid(row=1,column=0)

titletext1=StringVar()

e3=Entry(bottomframe,textvariable=titletext1)
e3.grid(row=1,column=1)

label4=Label(bottomframe,text="PASSWORD")
label4.grid(row=2,column=0)

titletext2=StringVar()

e4=Entry(bottomframe,textvariable=titletext2,show="*")
e4.grid(row=2,column=1)

label5=Label(bottomframe,text="CONFIRM PASSWORD")
label5.grid(row=3,column=0)

titletext3=StringVar()

e5=Entry(bottomframe,textvariable=titletext3)
e5.grid(row=3,column=1)

label6=Label(bottomframe,text="DATE OF BIRTH")
label6.grid(row=4,column=0)

titletext4=StringVar()

e6=Entry(bottomframe,textvariable=titletext4)
e6.grid(row=4,column=1)

label7=Label(bottomframe,text="GENDER")
label7.grid(row=5,column=0)

titletext5=StringVar()

e7=Entry(bottomframe,textvariable=titletext5)
e7.grid(row=5,column=1)

label8=Label(bottomframe,text="REGISTER FACE")
label8.grid(row=6,column=0)

b2=Button(bottomframe,text="Start Camera !",command=camroll)
b2.grid(row=6,column=1)

b3=Button(bottomframe,text="SUMBIT",justify=LEFT)
b3.grid(row=7,column=2)

root.mainloop()
