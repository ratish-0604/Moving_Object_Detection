# Moving Object Detection

import cv2
import time
import imutils

#captures the video
cam = cv2.VideoCapture(0)
time.sleep(1)

#assigning the first frame as none
first_frame = None
area=500

#running the loop for capturing images in it

while True:
    
    #takes each frame from the video 
    _,img = cam.read()
    text = "Normal" #to show when no object is detected
    
    img = imutils.resize(img,width=500)
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussimg = cv2.GaussianBlur(grayimg,(21,21),0)
    
    #passing the first frame with none
    if first_frame is None:
        first_frame = gaussimg
        continue
    
    #getting the difference between gaussian blur image and normal image
    img_diff=cv2.absdiff(first_frame,gaussimg)
    thres = cv2.threshold(img_diff,30,255,cv2.THRESH_BINARY)[1]
    thres = cv2.dilate(thres, None, iterations=2)
    
    #finding the borders for the objects in the image
    cnts = cv2.findContours(thres.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    #traversing the loop to find there is a moving object
    for c in cnts:
        if cv2.contourArea(c)<area:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        
        #highlights the moving object in green
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
        #change the text from normal to moving object detected if a object is detected
        text = "Moving Object Detected"
    
    #shows the image
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("camfeed",img)
    key = cv2.waitKey(1)&0xFF
    
    #if 'q' is pressed the cam is exited
    if key==ord('q'):
        break

#turns off the camera and closes the whole project
cam.release()
cv2.destroyAllWindows()
