import requests

API_KEY = '93746a98d57a67a21efa064b49cecea4'

CITY = input('Enter a city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(url)

# This Python code above asks the user for a city name, then uses that name 
# to check the weather using an online service called OpenWeatherMap. 
# It gets the weather information by sending a API KEY along with the city name, 
# and stores the results in the response variable.

# This code below, If the weather data request was successful (status code 200), 
# the code extracts temperature, feels-like temperature, weather description, 
# and wind speed from the received data and prints them. 
# Otherwise, it prints an error message indicating 
# that the specific city couldn't be found.
if response.status_code == 200:
    data = response.json()
    current_temperature_kelvin = data['main']['temp']
    current_temperature_celsius = current_temperature_kelvin - 273.15
    feels_like_temperature_kelvin = data['main']['feels_like']
    feels_like_temperature_celsius = feels_like_temperature_kelvin - 273.15
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    print(f'Current Temperature: {current_temperature_celsius:.0f} °C')
    print(f'Feels Like: {feels_like_temperature_celsius:.0f} °C')
    print(f'Weather Type: {weather_description}')
    print(f'Wind Speed: {wind_speed:.1f} m/s')
else:
    print('Cannot find the specific city')
