import requests
import json
url = 'https://static-maps.yandex.ru/'
token='85291902-221d-4193-b8aa-e1da0cc2697f'
info = requests.get(f'{url}?ll=37.620070,55.753630')
print(info.text)