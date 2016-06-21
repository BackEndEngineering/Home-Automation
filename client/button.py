import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(18, GPIO.OUT)


last_state = None

while True:
    current_state = GPIO.input(25)
    if current_state == last_state:
        continue
    
    if current_state == GPIO.LOW:
        print("Turn ON")
       
    else:
        print("Turn OFF")

    last_state = current_state





   
