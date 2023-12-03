import requests

API_KEY = '93746a98d57a67a21efa064b49cecea4'

CITY = input('Enter a city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(url)

# This Python code checks if an API request is successful (status code 200), 
# extracts temperature, weather description, and prints the information. 
# If the request is unsuccessful, it prints an error message 
# indicating the city could not be found.

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    desc = data['weather'][0]['description']
    wind = data['wind']['speed']
    
    print(f'Temperature: {temperature} K')
    print(f'Weather: {desc}')
    print(f'Wind Speed: {wind} m/s')
else:
    print('Cannot find the specific city')
    