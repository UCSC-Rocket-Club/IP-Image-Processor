import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
video = cv2.VideoWriter('output.avi', fourcc, 20, (640,480))

# Set Range of color to be tracked in this case blue
lowerBlue = np.array([100,100,100])
upperBlue = np.array([140,255,255])

# Set Range of color to be tracked in this case red
lowerRed = np.array([0,100,100])
upperRed = np.array([10,255,255])

#Set Colors
#red = [0,0,255]
#blue = [255,0,0]

while True:
    # Take each frame
    _, frame = cap.read()
    
    # Convert RGB to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    # Threshold the HSV image to get only color wanted
    maskBlue = cv2.inRange(hsv, lowerBlue, upperBlue)
    maskRed = cv2.inRange(hsv, lowerRed, upperRed)
    
    #maskBlue = cv2.inRange(lab, blue)
    #maskRed = cv2.inRange(lab, red)
    
    #Apply Median Blur to mask
    medianMaskBlue = cv2.medianBlur(maskBlue,15)
    medianMaskRed = cv2.medianBlur(maskRed,15)
        
    #Find Blue object to be tracked
    kernal = np.ones((5,5), 'uint8')
    
    blue = cv2.dilate(medianMaskBlue,kernal)
    _, contoursBlue, hierarchy = cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    red =cv2.dilate(medianMaskRed,kernal)
    _, contoursRed, _ = cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    # Write Box for Blue
    for pic, contour in enumerate(contoursBlue):
        area = cv2.contourArea(contour)
        if area > 300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame, 'BLUE',(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            
    # Write Box for Red
    for pic, contour in enumerate(contoursRed):
        area = cv2.contourArea(contour)
        if area > 300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame, 'RED',(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
        
    #Make frame tracking object
    #result = cv2.drawContours(frame, contours, -1, (0,0,0), 3)
        
    #Display live video frame
    cv2.imshow('frame',frame)
    cv2.imshow('mask',maskBlue)
    cv2.imshow('Blue Median Blur Mask', medianMaskBlue)
    #cv2.imshow('Result',result)
        
    # Write frame to file
    #frame = cv2.flip(frame,0)
    video.write(frame)
    if cv2.waitKey(5) == 27:
        break

cap.release()
video.release()
cv2.destroyAllWindows()