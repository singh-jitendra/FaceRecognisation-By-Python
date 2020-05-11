import os
import shutil
from tkinter import messagebox
import database
def del_fol():
       trains="training_data"
       #train="training_data\s1"

       if  os.path.exists(trains):

              try:
                shutil.rmtree(trains)
                database.delete1()
              except:
                  pass
       else:
           a=messagebox.showwarning("warning","there is no account created ")
           if a=='ok':
               pass


def del_account():
    trains = "training_data"
    # train="training_data\s1"
    a = messagebox.askquestion("delete", "Are you want to delete your account ")
    if a == 'yes':
        shutil.rmtree(trains)
        database.delete1()
        return a



