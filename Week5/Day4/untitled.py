import requests
import time

response = requests.get('https://api.chucknorris.io/jokes/random')

print(response.json()['value'])
