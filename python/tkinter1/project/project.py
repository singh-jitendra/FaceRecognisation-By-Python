


from tkinter import *
from tkinter import messagebox
import database

import cv2
#import os module for reading training data directories and paths
import os
#import numpy to convert python lists to numpy arrays as 
#it is needed by OpenCV face recognizers
import numpy as np

def enter(name):
    database.insert1(name)


def detect_face(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5);
    

    if (len(faces) == 0):
        return None, None
    

    (x, y, w, h) = faces[0]


    return  gray[y:y+w, x:x+h],faces[0]



def prepare_training_data(data_folder_path):
    


    dirs = os.listdir(data_folder_path)

    faces = []

    labels = []
    

    for dir_name in dirs:
        

        if not dir_name.startswith("s"):
            continue;
            

        label = int(dir_name.replace("s", ""))

        subject_dir_path = data_folder_path + "/" + dir_name
        

        subject_images_names = os.listdir(subject_dir_path)
        

        for image_name in subject_images_names:
            

            if image_name.startswith("."):
                continue;

            image_path = subject_dir_path + "/" + image_name


            image = cv2.imread(image_path)

            face, rect = detect_face(image)
            

            if not face is  None:

                faces.append(face)

                labels.append(label)
          
            
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return faces, labels


def data():
    
    #print("Preparing data...")
    faces, labels = prepare_training_data("training_data")
    #print("Data prepared")


#print total faces and labels
    #print("Total faces: ", len(faces))
    #print("Total labels: ", len(labels))

    face_recognizer =cv2.face.LBPHFaceRecognizer_create()

    face_recognizer.train(faces,np.array(labels))
    return face_recognizer


def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


def predict(test_img,face_recognizer):
    d = database.view2()
    e = d[0]
    subjects = ["unknown",e[0]]
    
    img = test_img.copy()

    face, rect = detect_face(img)
    try:
        label2, confidence = face_recognizer.predict(face)

    except:
        a = messagebox.showerror("Warning", "It does not predict the face pls restart your camera")
        if a == "ok":
            cv2.destroyAllWindows()
            return


    if confidence > 60:
        label2 = 0

    label_text = subjects[label2]
    # print(label_text)


    draw_rectangle(img, rect)

    draw_text(img, label_text, rect[0], rect[1] - 5)

    return img ,label_text


def main():

    face_recognizer=data()
    #print("Predicting faces...")

    vedio=cv2.VideoCapture(0)
    while True:
        check,images=vedio.read()
        if check is None:
            break
        try:

            predicted_img,face_name = predict(images,face_recognizer)
        except:
            face_name="unknown"


        try:

            cv2.imshow("predicted face ", cv2.resize(predicted_img, (400, 500)))
        except:
            return

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    enter(face_name)
    vedio.release()
    cv2.destroyAllWindows()

