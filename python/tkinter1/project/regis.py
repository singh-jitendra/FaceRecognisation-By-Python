from tkinter import *

import cv2
from PIL import ImageTk, Image
from instruct import inst
import database
import dir



def regist():
       rooot=Toplevel()
       rooot.geometry("400x400")

       topframe=Frame(rooot,borderwidth=10,relief=RAISED)
       topframe.pack(expand=1)

       bottomframe=Frame(rooot,borderwidth=10)
       bottomframe.pack(expand=1,side=BOTTOM)


       label0=Label(topframe,text="FACE RECOGNITION SYSTEM")
       label0.pack(anchor="center")

       img1=Image.open("download.png")
       img2=img1.resize((50,50))
       img3 =ImageTk.PhotoImage(img2)

       labe=Label(topframe,image=img3)
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

       b2=Button(bottomframe,text="Start Camera !",command=inst)
       b2.grid(row=6,column=1)
       def entry():
           database.insert(titletext.get(),titletext1.get(), titletext2.get(), titletext4.get(), titletext5.get())
           database.insert2(titletext.get())
           rooot.destroy()
       b3=Button(bottomframe,text="SUMBIT",justify=LEFT,command=entry)
       b3.grid(row=7,column=2)

       b4 = Button(bottomframe, text="CLOSE", justify=LEFT, command=rooot.destroy)
       b4.grid(row=7, column=3)

       a=dir.check_fol()
       if a=="ok":
           rooot.destroy()

       rooot.mainloop()


