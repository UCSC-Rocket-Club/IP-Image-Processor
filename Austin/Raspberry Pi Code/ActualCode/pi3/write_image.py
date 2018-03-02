import cv2
import time

folder = '/home/pi/images/'
startTime = time.clock()

def process(frame):
    image = frame.array
    timeStamp = str(time.time())
    cv2.imwrite(folder + timeStamp + ".jpg", image)
    
