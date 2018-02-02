import picamera
import time
import shutil
import os
import detect_color as dc


def record():

    shutil.rmtree('/home/pi/images/')
    os.mkdir('/home/pi/images')
    with picamera.PiCamera() as camera:
    	camera.resolution = (1280,720)
        camera.exposure_mode = 'sports'
        folder = '/home/pi/images/'
        while(True):
            time_stamp = str(time.time())
            fn = time_stamp
            camera.start_preview()
            camera.start_recording(folder + fn + '.h264')
            time.sleep(2)
            camera.stop_recording()
            camera.stop_preview()
            camera.capture(folder + fn + '.jpg', format='jpeg')
            dc.process(folder+fn + '.jpg')
