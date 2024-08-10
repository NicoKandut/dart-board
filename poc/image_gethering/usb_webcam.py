import cv2
from datetime import datetime

PATH = "data/webcam/board-{}.png".format(datetime.now().strftime("%d%m%y%H%M%S"))

cam = cv2.VideoCapture(4) #can mby change on other devices

result, image = cam.read() 

if result: 
    cv2.imwrite(PATH, image) 
 