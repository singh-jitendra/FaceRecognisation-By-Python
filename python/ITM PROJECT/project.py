

# Face Recognition with OpenCV


# ### Import Required Modules

# Before starting the actual coding we need to import the required modules for coding. So let's import them first. 
# 
# - **cv2:** is _OpenCV_ module for Python which we will use for face detection and face recognition.
# - **os:** We will use this Python module to read our training directories and file names.
# - **numpy:** We will use this module to convert Python lists to numpy arrays as OpenCV face recognizers accept numpy arrays.

#import OpenCV module
import cv2
#import os module for reading training data directories and paths
import os
#import numpy to convert python lists to numpy arrays as 
#it is needed by OpenCV face recognizers
import numpy as np



 
subjects = ["unknown","jitendra", "nancy","kavita"]



#function to detect face using OpenCV"""
def detect_face(img):
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]

    #return only the face part of the image
    return  gray[y:y+w, x:x+h],faces[0]


def prepare_training_data(data_folder_path):
    
    #------STEP-1--------
    #get the directories (one directory for each subject) in data folder
    dirs = os.listdir(data_folder_path)
    
    #list to hold all subject faces
    faces = []
    #list to hold labels for all subjects
    labels = []
    
    #let's go through each directory and read images within it
    for dir_name in dirs:
        
        #our subject directories start with letter 's' so
        #ignore any non-relevant directories if any
        if not dir_name.startswith("s"):
            continue;
            
        #------STEP-2--------
        #extract label number of subject from dir_name
        #format of dir name = slabel
        #, so removing letter 's' from dir_name will give us label
        label = int(dir_name.replace("s", ""))
        #print(label)
        #build path of directory containin images for current subject subject
        #sample subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name
        
        #get the images names that are inside the given subject directory
        subject_images_names = os.listdir(subject_dir_path)
        
        #------STEP-3--------
        #go through each image name, read image, 
        #detect face and add face to list of faces
        for image_name in subject_images_names:
            
            #ignore system files like .DS_Store
            if image_name.startswith("."):
                continue;
            
            #build image path
            #sample image path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + image_name

            #read image
            image = cv2.imread(image_path)
            #print(image_path)
            #display an image window to show the image 
            #cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)
            
            #detect face
            face, rect = detect_face(image)
            
            #------STEP-4--------
            #for the purpose of this tutorial
            #we will ignore faces that are not detected
            if not face is  None:
                #add face to list of faces
                faces.append(face)
                #add label for this face
                labels.append(label)
          
            
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return faces, labels


# function to draw rectangle on image
# according to given (x, y) coordinates and
# given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


# function to draw text on give image starting from
# passed (x, y) coordinates.
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

def predict(test_img):
    img = test_img.copy()
        # detect face from the image
    face, rect = detect_face(img)

        # predict the image using our face recognizer
    label2, confidence = face_recognizer.predict(face)

        # print(label2,confidence)
    if confidence > 60:
        label2 = 0
        # get name of respective label returned by face recognizer
    label_text = subjects[label2]
        # print(label_text)

        # draw a rectangle around face detected
    draw_rectangle(img, rect)
        # draw name of predicted person
    draw_text(img, label_text, rect[0], rect[1] - 5)

    return img



print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")


#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))




#create our LBPH face recognizer
face_recognizer =cv2.face.LBPHFaceRecognizer_create()

#or use EigenFaceRecognizer by replacing above line with
#face_recognizer = cv2.face.EigenFaceRecognizer_create()

#or use FisherFaceRecognizer by replacing above line with
#face_recognizer = cv2.face.FisherFaceRecognizer_create()



#train our face recognizer of our training faces
face_recognizer.train(faces,np.array(labels))








#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the 
#subject


print("Predicting faces...")

vedio=cv2.VideoCapture(0)
while True:
    check,images=vedio.read()
    if check is None:
        break
    predicted_img1 = predict(images)

        #display both images

    cv2.imshow("predicted face ", cv2.resize(predicted_img1, (400, 500)))

    key=cv2.waitKey(1)
    if key==ord("q"):
        break
vedio.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()