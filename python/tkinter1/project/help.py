from tkinter import *
from PIL import ImageTk, Image
def help():
    root=Toplevel()
    root.geometry("400x200")
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
    frame.pack(fill='both',expand="yes")
    labelframe=LabelFrame(frame,text="F.A.Q's")
    labelframe.pack(fill='both',expand="yes")
    label=Label(labelframe,text="Read the instruction carefully for registering the face.\n If you don't able toregister as well as log in pls delete account first ")
    label.pack()
    root.mainloop()
