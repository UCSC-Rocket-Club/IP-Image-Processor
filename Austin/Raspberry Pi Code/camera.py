#import picamera
import time
#import shutil
#import os
import detect_color as dc
import cv2

def record():

    #shutil.rmtree('/home/pi/images/')
    #os.mkdir('/home/pi/images')
    #with picamera.PiCamera() as camera:
    	#camera.resolution = (1280,720)
        #camera.exposure_mode = 'sports'
        #folder = '/home/pi/images/'
        #while(True):
            #time_stamp = str(time.time())
            #fn = time_stamp
            #camera.start_preview()
            #camera.start_recording(folder + fn + '.h264')
            #time.sleep(2)
            #camera.stop_recording()
            #camera.stop_preview()
            #camera.capture(folder + fn + '.jpg', format='jpeg')
            #dc.process(folder+fn + '.jpg')
            
    
    cap = cv2.VideoCapture(0)
    clock = 0
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    while True:
        timeStamp = str(time.time())
        video = cv2.VideoWriter(timeStamp + '.avi', fourcc, 20, (640,480))
        
        while clock < 2000:
            _, frame = cap.read()
            startTime = time.clock()
            frame = dc.process(frame)
            clock += time.clock() - startTime
            video.write(frame)
            print clock
            if cv2.waitKey(5) == 27:
                break
        video.release()
        if cv2.waitKey(5) == 27:
                break

    cap.release()