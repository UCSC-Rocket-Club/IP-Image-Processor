import camera
import detect_color as dc
import time
from multiprocessing import Process, Queue, Lock

def thread():
    p1 = Process(target=camera.record)
    p2 = Process(target=dc.anal_video)

    print('Buckle up, butter cup. You just flipped my bitch switch\n')

    p1.start()
    time.sleep(20)
    p2.start()
    
