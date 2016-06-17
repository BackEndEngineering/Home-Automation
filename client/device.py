import requests
action = {'name': '1', 'location': '321 Crestview bedroom 1', 'user': 'David'}
response = requests.post('http://guitron.herokuapp.com/api/Controller/', auth=('raspberrypi','compaq10'),json=action)
print(response.status_code)
print(response.json())
