from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import shutil
import os
import detect_color as dc
import cv2

def record():
            
    #shutil.rmtree('/home/pi/images/')
    #os.mkdir('/home/pi/images')
    #folder = '/home/pi/images/'
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))
    
    timeStamp = str(time.time())
    fourcc = cv2.VideoWriter_fourcc('H','2','6','4')
    video = cv2.VideoWriter(timeStamp + '.h264', fourcc, 20, (640,480))
    
    clock = 0
        
    for frame in camera.capture(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        startTime = time.clock()
        image = dc.process(image)
        cv2.imshow('Video',image)
        #print(clock)
        clock += time.clock() - startTime
        video.write(image)
        rawCapture.truncate(0)
        if clock > 30:
           break
        
    video.release()
    rawCapture.release()
    cv2.destroyAllWindows()