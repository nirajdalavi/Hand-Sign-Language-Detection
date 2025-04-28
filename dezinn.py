import cv2 as cv
from test import func1 
cv2=cv

root_wind='main'
cv.namedWindow(root_wind)

def startScan():
    func1()

cv.createButton('scan', startScan)