from tkinter import *
import database
from PIL import ImageTk, Image
from project import main
from tkinter import messagebox
import welcome
import os



def check_folder():
    if not os.path.exists("training_data/s1"):
        c=messagebox.showwarning("warning","pls register first")
        return c
def log():


    root =Toplevel()

    root.geometry("350x300")


    topframe=Frame(root,relief= RAISED,borderwidth=10)
    topframe.pack(expand=1)
    bottomframe=Frame(root, borderwidth=10)
    bottomframe.pack(side=BOTTOM,expand=1)


    label1=Label(topframe,text="Face Recogniation System")
    label1.pack(anchor="center")

    img=Image.open("download.png")
    img=img.resize((50,50))
    img =ImageTk.PhotoImage(img)

    label2=Label(topframe,image=img)
    label2.pack()

    l1=Label(topframe,text="LOG IN")
    l1.pack(anchor="center")

    l2=Label(bottomframe,text="USER ID")
    l2.grid(row=0,column=1)
    titletext=StringVar()

    e2=Entry(bottomframe,textvariable=titletext)
    e2.grid(row=0,column=2)

    l3=Label(bottomframe,text="PASSWORD")
    l3.grid(row=1,column=1)
    titletext1=StringVar()
    e3=Entry(bottomframe,textvariable=titletext1,show="*")
    e3.grid(row=1,column=2)
    l4 = Label(bottomframe, text="OR")
    l4.grid(row=2, column=1)
    def user():
       try:
           b=database.search(titletext.get())
           c=b[0]
           #print(c)
           d=database.view1()
           e=d[0]
           #print(e)
           database.delete()
           if c[0]==titletext1.get() or c[1]==e[0]:
               root.destroy()
               welcome.wel()
           else:
               messagebox.askretrycancel("login  error", "pls check your user id and password")
       except:
           b=messagebox.showwarning("warning", "pls confirm your face , user id and password")
           if b=="ok":
               root.destroy()


   

    l4=Label(bottomframe,text="DETECT FACE *" )
    l4.grid(row=3,column=1)

    b2=Button(bottomframe, text="Start Camera !", command=main)
    b2.grid(row=3,column=2)

    b1=Button(bottomframe,text="Sign In",command = user)
    b1.grid(row=4,column=3)

    b3 = Button(bottomframe, text="close", command=root.destroy)
    b3.grid(row=4, column=4)
    d = check_folder()
    if d == "ok":
        root.destroy()

    root.mainloop()


