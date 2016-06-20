import requests

#events = requests.get('http://guitron.herokuapp.com/api/Controller/')
#print(events.status_code)
#print(events.headers)
#print(events.text[0:100])
#print(events.json()[0])
controller = {'name': '5', 'user': 'superman', 'location': '16 Crestborn bedroom 10'}
headers = {'Authorization': 'Token cb7431488e267a9283732ac9e867c4aac9eb8b40'}
response = requests.post('http://guitron.herokuapp.com/api/Controller/', json=controller, headers=headers)
print(response.status_code)
print(response.text[0:100])
