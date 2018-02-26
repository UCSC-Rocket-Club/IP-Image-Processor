import camera
import detect_color as dc
from multiprocessing import Process, Queue, Lock

def thread():
    p1 = Process(target=camera.record)
    p2 = Process(target=dc.anal_video)

    print('Buckle up, butter cup. You just flipped my bitch switch\n')

    p1.start()
    p2.start()
