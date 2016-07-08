import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)
try:
	time.sleep(2)
	print "Ready"
	while True:
		if (GPIO.input(2)==1):
			print "Motion detected"
			time.sleep(1)
		else:
			print "No motion"
			time.sleep(1)
except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()

