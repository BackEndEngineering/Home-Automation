import RPi.GPIO as GPIO
import time

lights = input( 'Turn Lights ON or OFF? '))
if lights == "yes":

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, 1)
blink = GPIO.PWM(18, 1)
try:
    blink.start(50)
    while True:
        pass
except KeyboardInterrupt:
    blink.stop()
GPIO.cleanup()
