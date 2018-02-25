from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import shutil
import os
import cv2

def record():
            
    shutil.rmtree('/home/pi/images/')
    os.mkdir('/home/pi/images')
    folder = '/home/pi/images/'
    timeStamp = str(time.time())    
    clock = 0
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))
    startTime = time.clock()
    
    for frame in camera.capture(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imwrite( folder + timeStamp + ".jpg", image)
        clock = time.clock() - startTime
        rawCapture.truncate(0)
        if clock > 30:
           break
        