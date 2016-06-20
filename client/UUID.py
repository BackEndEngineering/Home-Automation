from config import CONFIG, TOKEN
import requests
import sys

try:
    uid_file = open('UID', encoding='utf-8')
    print(uid_file.read())
    sys.exit()
except FileNotFoundError:
    pass

headers = {'Authorization': 'Token '+ TOKEN}
controller = {}
response = requests.post('http://guitron.herokuapp.com/api/Controller/', json=CONFIG, headers=headers)
print(response.status_code)
print(response.json())
