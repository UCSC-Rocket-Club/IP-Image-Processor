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
    clock = 0
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))
    startTime = time.clock()
    timeStamp = str(time.time())
    fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
    video = cv2.VideoWriter(folder + timeStamp.replace('.','') + '.avi',fourcc, 30,(480, 360))
    frame_count = 0
    time_to_record = time.time()
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        video.write(image)
        frame_count += 1
        clock = time.clock() - startTime
        print('Camera: '+ str(clock) + 's\n')
        rawCapture.truncate(0)
        if clock > 10:
            print('Camera Done ' + str(clock) +'s\n')
            video.release()
            camera.close()
            rawCapture.close()
            break
    
    time_to_record = time.time() - time_to_record
    print('after ' + str(frame_count) + ' frames done in ' + str(time_to_record) + ' seconds CAMERA DONE HOPEFULLY EXITED\n')
