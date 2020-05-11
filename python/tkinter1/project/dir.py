import os
from tkinter import messagebox
import database

def check_fol():
       trains="training_data"
       train="training_data\s1"

       if not os.path.exists(trains):
              os.mkdir(trains)
              os.mkdir(train)
              try:
                  d = database.view2()
                  e = d[0]
                  database.delete1(e)
              except:
                  pass
       else:
              d=messagebox.showwarning("warning","you have already registered ")
       return d



       
