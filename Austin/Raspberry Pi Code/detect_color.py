# USAGE
# python detect_color.py --image example_shapes.png

# import the necessary packages
#from pyimagesearch.shapedetector import ShapeDetector
#from pyimagesearch.colorlabeler import ColorLabeler
#import argparse
#import imutils
import cv2
import numpy as np
# from __future__ import print_function



def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)



def process(frame):

    # Set Range of blue to be tracked
    lowerBlue = np.array([100,100,100])
    upperBlue = np.array([140,255,255])

    # Set Range of pink to be tracked
    lowerRed = np.array([125, 100, 30])
    upperRed = np.array([255, 255, 255])

    # Set Range of yellow to be tracked
    lowerYellow = np.array([0, 204, 204])
    upperYellow = np.array([153, 255, 255])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    # Threshold the HSV image to get only color wanted
    maskBlue = cv2.inRange(hsv, lowerBlue, upperBlue)
    maskRed = cv2.inRange(hsv, lowerRed, upperRed)
    maskYellow = cv2.inRange(hsv, lowerYellow, upperYellow)
    
    #maskBlue = cv2.inRange(lab, blue)
    #maskRed = cv2.inRange(lab, red)
    
    #Apply Median Blur to mask
    medianMaskBlue = cv2.medianBlur(maskBlue,15)
    medianMaskRed = cv2.medianBlur(maskRed,15)
    medianMaskYellow = cv2.medianBlur(maskYellow,15)
        
    #Find Blue object to be tracked
    kernal = np.ones((5,5), 'uint8')
    
    blue = cv2.dilate(medianMaskBlue,kernal)
    _, contoursBlue, hierarchy = cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    red =cv2.dilate(medianMaskRed,kernal)
    _, contoursRed, _ = cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    yellow =cv2.dilate(medianMaskYellow,kernal)
    _, contoursYellow, _ = cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
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
     
    # Write Box for Yellow
    for pic, contour in enumerate(contoursYellow):
        area = cv2.contourArea(contour)
        if area > 300:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame, 'YELLOW',(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0))
            
    return frame

