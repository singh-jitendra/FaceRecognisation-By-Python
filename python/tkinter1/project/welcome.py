from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from delete import del_account
from PIL import ImageTk, Image
from  instruct import inst
from database import view2
def hi():
    print("it work")
def update():
    b=messagebox.askquestion("update","Are you want to update face")
    if b=='yes':
        inst()
        messagebox.showinfo("sucess","Your face updated successfully ")


def wel():
    root = Toplevel()
    root.geometry("300x300")
    img = Image.open("download.png")
    img = img.resize((50, 50))
    img = ImageTk.PhotoImage(img)
    topframe = Frame(root, borderwidth=10, relief=RAISED)
    topframe.pack(expand=1)

    label1 = Label(topframe, text="FACE RECOGNITION SYSTEM")
    label1.pack(anchor="center")
    label2 = Label(topframe, image=img)
    label2.pack()
    def del_acc():
        a=del_account()
        if a=='yes':
            exit(-1)

    menu = Menu(root)
    root.config(menu=menu)
    subMenu = Menu(menu)
    menu.add_cascade(label="Update", menu=subMenu)
    subMenu.add_command(label="Delete Account",command=del_acc)
    subMenu.add_command(label="Update Face", command=update)
    log=Menu(menu)

    menu.add_cascade(label="Log out",menu=log)
    log.add_command(label="log out",command=root.destroy)
    bottomframe=Frame(root, borderwidth=10)
    bottomframe.pack()


    label=Label(bottomframe,text="WELCOME......@@ ##")
    label.pack(anchor=CENTER)
    a=view2()
    b=a[0]
    labe2 = Label(bottomframe, text=b[0])
    labe2.pack(anchor=CENTER)
    Status = Label(root, text="welcome....", bd=1)
    Status.pack(anchor=SW, side=BOTTOM)
    root.mainloop()
