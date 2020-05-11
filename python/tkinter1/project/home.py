from tkinter import *

from PIL import ImageTk, Image

from login import log
from regis import regist
from about import about
from delete import del_fol
from help import help
from contact import cont

win=Tk()
win.title("F.R.S")
win.geometry("400x400")

img=Image.open("download.png")
img=img.resize((50,50))
img =ImageTk.PhotoImage(img)

win.wm_iconphoto(win,img)

topframe=Frame(win,borderwidth=10,relief=RAISED)
topframe.pack(expand=1)

label1=Label(topframe,text="FACE RECOGNITION SYSTEM")
label1.pack(anchor="center")




label2=Label(topframe,image=img)
label2.pack()

bottomframe=Frame(win,borderwidth=10)
bottomframe.pack(side=BOTTOM,expand=1)

b1=Button(bottomframe,text="Log In",command=log)
b1.pack(side=LEFT)

b2=Button(bottomframe,text="Registration" ,command=regist)
b2.pack(side=LEFT)

b3=Button(bottomframe,text="Help",command=help)
b3.pack(side=LEFT)


b4=Button(bottomframe,text="Contact",command=cont)
b4.pack(side=LEFT)

b5=Button(bottomframe,text="About Us",command=about)
b5.pack(anchor=CENTER,side=LEFT)

b6=Button(bottomframe,text="Deletet Account",command=del_fol)
b6.pack(anchor=CENTER,side=BOTTOM)


win.mainloop()
