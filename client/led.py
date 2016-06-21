import RPi.GPIO as GPIO


lights = input( 'Turn Lights ON or OFF? ')
if lights == "ON":

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    print('Lights are Turn ON')
  

if lights == "OFF":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()
    print('Lights are Turn OFF')

 
