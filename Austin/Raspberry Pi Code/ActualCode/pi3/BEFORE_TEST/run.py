import camera
import detect_color as dc
import time
import math
from multiprocessing import Process, Queue, Lock
from adxl345 import ADXL345

def thread():
    p1 = Process(target=camera.record)
    p2 = Process(target=dc.anal_video)

    print('Buckle up, butter cup. You just flipped my bitch switch\n')

    p1.start()
    adxl = ADXL345()

    while True:
        axes = adxl.getAxes(True)
        xyforce = math.sqrt(axes['x'] ** 2 + axes['y'] ** 2)
        netforce = math.sqrt(xyforce ** 2 + axes['z'] ** 2)

        if(netforce >= 2):
            print('LAUNCH LAUNCH LAUNCH LAUNCH LAUNCH')
            break


    time.sleep(2)
    p2.start()
    
