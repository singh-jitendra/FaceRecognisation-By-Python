from tkinter import *

def about():
    r=Toplevel()
    r.geometry("250x150")
    ro=Frame(r,borderwidth=10)
    ro.pack()

    label=Label(ro,text="ABOUT US")
    label.pack()
    label1=Label(ro,text="ITM GOI")
    label1.pack()
    label2=Label(ro,text="JITENDRA SINGH  \n 0905cs151066 \n COMPUTER SCIENCE DEPARTMENT \n B.E. 3rd YEAR ")
    label2.pack()

    def close():
        r.destroy()

    b1=Button(ro,text="close",command=close)
    b1.pack(side=RIGHT)
    r.mainloop()