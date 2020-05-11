from tkinter import *
from PIL import ImageTk, Image

root =Tk()

root.title("FACE RECOG. SYSTEM")

root.geometry("300x300")
topframe=Frame(root,relief= RAISED, borderwidth=5)
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

l4=Label(bottomframe,text="DETECT FACE *")
l4.grid(row=3,column=1)

b2=Button(bottomframe,text="Start Camera !" )
b2.grid(row=3,column=2)

b1=Button(bottomframe,text="Sign In")
b1.grid(row=4,column=3)



root.mainloop()
