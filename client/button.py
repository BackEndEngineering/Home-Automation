import RPi.GPIO as GPIO
from config import TOKEN, BASE_URL
import requests
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(18, GPIO.OUT)



URL = BASE_URL
Token = TOKEN

try:
    uid_file = open('UID', encoding='utf-8')
    uid = uid_file.read()
    uid_file.close()

except FileNotFoundError:
    pass

headers = {'Authorization': 'Token '+ TOKEN}

last_state = None

while True:
    current_state = GPIO.input(25)
    if current_state == last_state:
        continue

    if current_state == GPIO.LOW:
        print("Turn ON")

        event_data = {
                        'uuid': uid,
                        'name':'Master Bedroom ',
                        'area': 'Bedroom 1',
                        'kind': 'fan',
                        'pin': '1',
                        'value': 'on'
                        }

        response = requests.post('http://guitron.herokuapp.com/' + 'guitron/create_event/', json=event_data, headers=headers)
        print(response.status_code)

    else:
        print("Turn OFF")
    time.sleep(5)

    response = requests.get('http://guitron.herokuapp.com/' + 'guitron/get_action/', headers=headers)
    print(response.status_code)

    actions = response.json()["actions"]

    for action in actions:
        print(action)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13, GPIO.IN)
        lights = None
        current_state = GPIO.input(13)
        current_state = lights

        if lights == GPIO.LOW:

        #    GPIO.setmode(GPIO.BCM)
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, GPIO.HIGH)
            print('Lights are Turn ON')

            action = {
                        'name':'Lights',
                        'area': 'Game Room',
                        'kind': 'ceiling fan',
                        'pin': '17',
                        'value': 'on'
                        }

        if lights == GPIO.HIGH:
#            GPIO.setmode(GPIO.BCM)
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, GPIO.LOW)
            GPIO.cleanup()
            print('Lights are Turn OFF')


        time.sleep( 5 )
        last_state = current_state
