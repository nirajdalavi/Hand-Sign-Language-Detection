import cv2 
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
from tkinter import *
from PIL import Image, ImageTk

cap=cv2.VideoCapture(0)
width, height = 1000, 1000
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
detector=HandDetector(maxHands=1)
offset=20
imgSize=300
labels=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
app = Tk() 
app.bind('<Escape>', lambda e: app.quit())
label_widget = Label(app)
label_widget.pack()

def asl(): 
    classifier=Classifier("Model/keras_model.h5","Model/labels.txt")
    open_camera(classifier)

def open_camera(classifier):

    success,img=cap.read()
    global imgOutput 
    imgOutput=img.copy()
    hands,img=detector.findHands(img)
    if hands:
        hand=hands[0]
        x,y,w,h=hand['bbox']
        imgWhite=np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop=img[y-offset:y+h+offset,x-offset:x+w+offset]
        imgCropShape= imgCrop.shape

        aspectRatio=h/w

        if aspectRatio>1:
            k=imgSize/h
            wCal=math.ceil(k*w)
            try:
                imgResize=cv2.resize(imgCrop,(wCal,imgSize))
            except:
                open_camera(classifier)       
            imgResizeShape= imgResize.shape
            wGap=math.ceil((300-wCal)/2)
            imgWhite[:,wGap:wCal+wGap]=imgResize
            prediction,index=classifier.getPrediction(imgWhite,draw=False)
            print(prediction,index)
        else:
            k=imgSize/w
            hCal=math.ceil(k*h)
            try:
                imgResize=cv2.resize(imgCrop,(imgSize,hCal))
            except:
                open_camera(classifier)      
            imgResizeShape= imgResize.shape
            hGap=math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:hCal+hGap,:]=imgResize    
            prediction,index=classifier.getPrediction(imgWhite,draw=False)
        cv2.rectangle(imgOutput,(x-offset,y-offset-50),(x-offset+90,y-offset),(255,0,255),cv2.FILLED)
        cv2.putText(imgOutput,labels[index],(x,y-26),cv2.FONT_HERSHEY_COMPLEX,1.7,(255,255,255),2)
        cv2.rectangle(imgOutput,(x-offset,y-offset),(x+w+offset,y+h+offset),(255,0,255),4)

    opencv_image = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(opencv_image)
    photo_image = ImageTk.PhotoImage(image=captured_image)
    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)
    label_widget.after(10, open_camera,classifier)


def hold():
    label_widget.destroy()

button1 = Button(app, text="Start detecting!", command=asl)
button1.pack()



button3= Button(app,text="stop",command=hold)
button3.pack()
app.mainloop()