import requests

pyynto = requests.get('https://api.chucknorris.io/jokes/random')
vitsi = pyynto.json()

print(vitsi["value"])