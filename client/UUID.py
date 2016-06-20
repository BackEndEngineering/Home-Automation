from config import CONFIG, TOKEN
import requests
import sys

try:
    uid_file = open('UID', encoding='utf-8')
    print(uid_file.read())
    uid_file.close()
    sys.exit()
except FileNotFoundError:
    pass

headers = {'Authorization': 'Token '+ TOKEN}
controller = {}
response = requests.post('http://guitron.herokuapp.com/api/Controller/', json=CONFIG, headers=headers)
print(response.status_code)
#print(response.json())
controller = response.json()


try:
    with open('UID', mode='w', encoding='utf-8') as uid_file:
        uid_file.write(controller['uuid'])

except FileNotFoundError:
    pass
