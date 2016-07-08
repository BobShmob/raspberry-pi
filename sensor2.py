import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
	print “b”

print “PIR Module Test)”
time.sleep(2)
print “Ready”

try:
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
	while 1:
		time.sleep(100)
except KeyboardInterrupt:
	print “ Quit”
	GPIO.cleanup()
