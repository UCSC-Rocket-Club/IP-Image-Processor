#import picamera
import time
import shutil
import os
import detect_color as dc
import cv2

def record():
            
    #shutil.rmtree('/home/pi/images/')
    #os.mkdir('/home/pi/images')
    #folder = '/home/pi/images/'
    #shutil.rmtree('/home/arlamb/pi/images/')
    #os.mkdir('/home/arlamb/pi/images/')
    #folder = '/home/arlamb/pi/images/'
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc('X','2','6','4')
    #with picamera.PiCamera() as camera:
        #camera.resolution = (1280,720)
        #camera.exposure_mode = 'sports'
    
    while True:
        clock = 0
        timeStamp = str(time.time())
        video = cv2.VideoWriter(timeStamp + '.h264', fourcc, 20, (640,480))
        
        while clock < 2:
            _, frame = cap.read()
            startTime = time.clock()
            frame = dc.process(frame)
            #cv2.imshow('Video',frame)
            print(clock)
            clock += time.clock() - startTime
            video.write(frame)
            if cv2.waitKey(5) == 27:
                break
        video.release()
        if cv2.waitKey(5) == 27:
                break

    cap.release()
    cv2.destroyAllWindows()