import record
import detect_color as dc
import time
from multiprocessing import Process, Queue, Lock

p1 = Process(target=record.record)
p2 = Process(target=dc.anal_video)

p1.start()
p2.start()
