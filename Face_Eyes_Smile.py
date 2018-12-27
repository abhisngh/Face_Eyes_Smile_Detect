# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 01:25:34 2018

@author: Abhishek Kumar Singh
"""

# Face Recognition

# Importing the libraries
import cv2

# We load the cascade for the face.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# We load the cascade for the eyes.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# We load the cascade for the smiles.
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
 
 # We create a function that takes as input the image in black and white (gray) and the original image (frame),
 #and that will return the same image with the detector rectangles. 
def detect(gray, frame):
    
    #faces are the tuple containing x,y(co-ordinates) and w,h widht and height respectively'''
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # For each detected face:
    for (x, y, w, h) in faces:
        
        # We paint a rectangle around the face.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # We get the region of interest in the black and white image.
        roi_gray = gray[y:y+h, x:x+w]
        
        # We get the region of interest in the colored image.
        roi_color = frame[y:y+h, x:x+w]
        
        # We apply the detectMultiScale method to locate one or several eyes in the image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        
        
         # For each detected eye:
        for (ex, ey, ew, eh) in eyes:
            # We paint a rectangle around the eyes, but inside the referential of the face.
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
           
        # We apply the detectMultiScale method to locate smile in the image.
        smile = smile_cascade.detectMultiScale(roi_gray,1.7, 22)
        
        # For each detected eye:
        for(sx,sy,sw,sh) in smile:
            # We paint a rectangle around the smile, but inside the referential of the face.
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0,0,2500), 2)
    return frame

# Doing some Face Recognition with the webcam
# We turn the webcam on.
#0 value for internal webcam and 1 for external webcam'''
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    
    # We do some colour transformations.
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # We get the output of our detect function.
        canvas = detect(gray, frame)
    
    # We display the outputs.
        cv2.imshow('Video', canvas)
    
    # If we type q on the keyboard:
        if cv2.waitKey(1) & 0xFF == ord('q'):
         # We stop the loop.
            break

# We turn the webcam off.    
video_capture.release()

# We destroy all the windows inside which the images were displayed.
cv2.destroyAllWindows()
