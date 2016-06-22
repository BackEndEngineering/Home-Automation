import RPi.GPIO as GPIO
from config import TOKEN, BASE_URL

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

        response = requests.post('http://guitron.herokuapp.com/' + 'guitron/create/', json=event_data, headers=headers)
        print(response.status_code)
# Get URL, token, and uuid
#  URL: from config import BASE_URL
#  token: from config import TOKEN
#  uuid: something like "with open(UID) as uid_file: uuid = uid_file.read()
# Create Event dictionary
#       # event_data = {
        #             'uuid': '1', # from UID file
        #             'name':'Master Bedroom ', # hard code
        #             'area': 'Bedroom 1', # hard code
        #             'kind': 'fan', # hard code
        #             'pin': '1', # hard code
        #             'value': 'on'
        #             }
# Create headers dictionary
#       # headers = {'Authorization': 'Token '+ TOKEN}
# response = requests.post()
#  Three arguments:
#   url: base_url + "/guitron/create/"
#   json=event_data,
#   headers=headers
# Look at the response
#  response.status_code # print it out for now

    else:
        print("Turn OFF")

    last_state = current_state
