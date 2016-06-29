import RPi.GPIO as GPIO
from config import TOKEN, BASE_URL
import requests
import time
import smtplib

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(18, GPIO.HIGH)



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

def text():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("myguitron@gmail.com", "Myguitron10")

    msg = "YOUR MESSAGE!"
    server.sendmail("MyGuiTron@gmail.com", "2108874112@messaging.sprintpcs.com", msg)
    server.quit()

def handle_events():
    global last_state
    current_state = GPIO.input(25)
    if current_state == last_state:
        return

    if current_state == GPIO.LOW:
        print("Turn ON")
        text()
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
    last_state = current_state

while True:
    handle_events()
    response = requests.get('http://guitron.herokuapp.com/' + 'guitron/get_action/', headers=headers)
    print(response.status_code)

    actions = response.json()["actions"]

    for action in actions:
        print(action)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13, GPIO.IN)

        if action['value'] == 'ON':
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, GPIO.HIGH)

        if action['value'] == 'OFF':
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, GPIO.LOW)

        time.sleep( 5 )
