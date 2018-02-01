import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
video = cv2.VideoWriter('output.avi', fourcc, 20, (640,480))

# Set Range of color to be tracked in this case blue
lowerColor = np.array([100,100,100])
upperColor = np.array([140,255,255])

while True:
    # Take each frame
    _, frame = cap.read()
    
    # Convert RGB to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    # Threshold the HSV image to get only color wanted
    mask = cv2.inRange(hsv, lowerColor, upperColor)
        
    #Apply Median Blur to mask
    medianMask = cv2.medianBlur(mask,15)
        
    #Find object to be tracked
    kernal = np.ones((5,5), 'uint8')
    temp = cv2.dilate(medianMask,kernal)
    _, contours, hierarchy = cv2.findContours(temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask = mask)
        
    #Make frame tracking object
    result = cv2.drawContours(frame, contours, -1, (0,0,0), 3)
        
    #Gaussian Blurring to deal with Noise
    blurRes = cv2.GaussianBlur(res,(9,9),0)
    medianRes = cv2.medianBlur(res,15)
        
    #Display live video frame
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('Median Blur Mask', medianMask)
    cv2.imshow('res',res)
    cv2.imshow('Gaussian Blurring',blurRes)
    cv2.imshow('Median Blur Res', medianRes)
    cv2.imshow('Result',result)
        
    # Write frame to file
    #frame = cv2.flip(frame,0)
    video.write(result)
    if cv2.waitKey(5) == 27:
        break

cap.release()
video.release()
cv2.destroyAllWindows()