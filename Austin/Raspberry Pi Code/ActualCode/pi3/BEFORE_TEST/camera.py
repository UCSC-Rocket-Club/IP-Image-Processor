from picamera.array import PiRGBArray
from picamera import PiCamera
from adxl345 import ADXL345
import math
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
    frames_record_time  = time.time()
    frame_count = 0
    adxl = ADXL345()
    
    while True:
        axes = adxl.getAxes(True)
        xyforce = math.sqrt(axes['x'] ** 2 + axes['y'] ** 2)
        netforce = math.sqrt(xyforce ** 2 + axes['z'] ** 2)

        if(netforce >= 2):
            print('LAUNCH LAUNCH LAUNCH LAUNCH LAUNCH')
            break

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        timeStamp = str(time.time())
        cv2.imwrite(folder + timeStamp + ".jpg", image)
        frame_count += 1
        clock = time.clock() - startTime
        print('time: ' + str(clock))
        print('the ' + timeStamp + '.jpg frame has been taken and recorded \n')
        rawCapture.truncate(0)
        if clock > 10:
            print('Camera Done ' + str(clock) +'s\n')
            rawCapture.close()
            camera.close()
            break

    frames_record_time = time.time() - frames_record_time
    print(str(frame_count) + ' frames done in ' + str(frames_record_time) + ' seconds for the camera recording')     
