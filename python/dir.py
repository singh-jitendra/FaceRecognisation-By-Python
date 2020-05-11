import os
import shutil
training_data="training"
train="training\s1"
if not os.path.exists(training_data):
       os.mkdir(training_data)
       print("its make")
else:
       print("it already exists")
if not os.path.exists(train):
       os.mkdir(train)
       print("its make")
else:
       print("it already exists")
#shutil.rmtree(training_data)


       
