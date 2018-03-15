import camera
import detect_color as dc
import time
import math
from multiprocessing import Process, Queue, Lock
from adxl345 import ADXL345
import RPi.GPIO as GPIO

def thread():
    #p1 = Process(target=camera.record)

    print('\nBuckle up, butter cup. You just flipped my bitch switch\n')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(10, GPIO.LOW)
    print('Set-up Pin 10\n')
    GPIO.setup(21, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    print('Set-up Pin 21\n')
	
    adxl = ADXL345()
    print('Set-up ADXL345\n')

    GPIO.output(10, GPIO.HIGH)
        
    while True:
        axes = adxl.getAxes(True)
        xyforce = math.sqrt(axes['x'] ** 2 + axes['y'] ** 2)
        netforce = math.sqrt(xyforce ** 2 + axes['z'] ** 2)

        if(netforce >= 5):
            GPIO.output(10, GPIO.LOW)
            print('LAUNCH LAUNCH LAUNCH LAUNCH LAUNCH')
            break
    camera.record()
    #p1.start()

    # commented out to experiment with several threads writing images to the sd card at once

    #    p1.start()
    #    adxl = ADXL345()
    #
    #    while True:
    #        axes = adxl.getAxes(True)
    #        xyforce = math.sqrt(axes['x'] ** 2 + axes['y'] ** 2)
    #        netforce = math.sqrt(xyforce ** 2 + axes['z'] ** 2)
    #
    #        if(netforce >= 2):
    #            print('LAUNCH LAUNCH LAUNCH LAUNCH LAUNCH')
    #            break
    #
    #
    #    time.sleep(2)
    #    p2.start()

    
thread()
