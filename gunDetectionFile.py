import numpy as np 
import imutils 
import cv2 


dataSheet = cv2.CascadeClassifier('dataSheet.xml') 
camera = cv2.VideoCapture(0) 


firstFrame = None
gun_exist = False

while True: 
        
     ret, frame = camera.read() 

     frame = imutils.resize(frame, width = 500) 
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        
     gun = cascadeSheet.detectMultiScale(gray, 1.3, 5, minSize = (100, 100)) 
        
     if len(gun) > 0: 
          gun_exist = True
              
        for (x, y, w, h) in gun: 
                
             frame = cv2.rectangle(frame, (x, y), (x + w, y + h),(255, 0, 0), 2) 
             roi_gray = gray[y:y + h, x:x + w] 
             roi_color = frame[y:y + h, x:x + w]         


        if firstFrame is None: 
             firstFrame = gray 
             continue
 
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'): 
             break

camera.release() 
cv2.destroyAllWindows()