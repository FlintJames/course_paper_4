import requests
import json

url = 'https://api.hh.ru/vacancies'

response = requests.get(url, params={'text': 'vacancy'})
print(response.text)
j = response.json()
print(j)
print(type(j))
print(j['items'][2:3])


