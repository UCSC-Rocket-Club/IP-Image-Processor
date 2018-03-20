from picamera.array import PiRGBArray
from picamera import PiCamera
from multiprocessing import Process
import detect_color
import write_image
import math
import time
import shutil
import os
import cv2

def record():
            
    shutil.rmtree('/home/pi/images/')
    os.mkdir('/home/pi/images')
    clock = 0
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))
    startTime = time.clock()

    frames_record_time  = time.time()
    frame_count = 0
        
    #start of multi-thread code

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        writing_process = Process(target=write_image.process, args=(frame, ))
        writing_process.start()

        frame_count += 1
        clock = time.clock() - startTime
        print('time: ' + str(clock))
        rawCapture.truncate(0)

        if clock > 20:
            print('Camera Done ' + str(clock) +'s\n')
            rawCapture.close()
            camera.close()
            break

    frames_record_time = time.time() - frames_record_time
    print(str(frame_count) + ' frames done in ' + str(frames_record_time) + ' seconds for the camera recording')     

    detect_color.anal_video()
    
    # old code that used to work, but wrote slowly

#    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#        image = frame.array
#        timeStamp = str(time.time())
#        cv2.imwrite(folder + timeStamp + ".jpg", image)
#        frame_count += 1
#        clock = time.clock() - startTime
#        print('time: ' + str(clock))
#        print('the ' + timeStamp + '.jpg frame has been taken and recorded \n')
#        rawCapture.truncate(0)
#        if clock > 10:
#            print('Camera Done ' + str(clock) +'s\n')
#            rawCapture.close()
#            camera.close()
#            break
#
#    frames_record_time = time.time() - frames_record_time
#    print(str(frame_count) + ' frames done in ' + str(frames_record_time) + ' seconds for the camera recording')     
#    
