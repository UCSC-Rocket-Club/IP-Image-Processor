import RPi.GPIO as GPIO
import time
import signal
import sys
import os
import run


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10,GPIO.OUT)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


def signal_handler(signal, frame):
	GPIO.output(10,GPIO.LOW)
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for i in range(0,30):
	GPIO.output(10,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(10,GPIO.LOW)
	time.sleep(0.1)



while GPIO.input(4) == 1:
	pass





while True:
	status = GPIO.input(4)
	if status == 1:
		GPIO.output(10,GPIO.HIGH)
	        	
                print('fuck wiht me you know i got it') 
                run.thread()              
                GPIO.output(10,GPIO.LOW)
		#except:
		#	GPIO.output(10,GPIO.LOW)
		#	exit(0)
	else:
		GPIO.output(10,GPIO.LOW)


