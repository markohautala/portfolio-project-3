import requests

API_KEY = '93746a98d57a67a21efa064b49cecea4'

CITY = input('Enter a city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    desc = data['weather'][0]['description']
    desc = data['weather'][0]['wind']
    print(f'Temperature: {temperature} K')
    print(f'Weather: {desc}')
    print(f'Wind: {wind}')
else:
    print('Cannot find the specific city')
    