
# Collecting Weather data from OpenWeather.

import requests
from bs4 import BeautifulSoup

# parameters
latitude = 6.6018
longitude = 3.3515
API_KEY = "f79c259d7bda321529418abd05c217ce"

weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"

request = requests.get(url= weather_api)

req = requests.get(url = 'https://google.com')

# check the response
print(requests.status_codes)

# body
response = request.content
print(response)

# make a requests
request = requests.get(url= weather_api).json()

# data collection

data ={
    'country': request['sys']['country'],
    'city': request['name'],
    'longitude' : request['coord']['lon'],
    'latitude' : request['coord']['lat'],
    'temp' : request['main']['temp'],
    'temp_min' : request['main']['temp_min'],
    'temp_max ' : request['main']['temp_max'],
    'pressure' :request['main']['humidity'],
    'humidity' :request ['main']['humidity'],
    'sea_level': request['main']['sea_level'],
    'ground_level': request['main']['grnd_level'],
    'wind_speed' : request['wind']['speed'],
    'wind_degree' :request['wind']['deg'],
    'sunrise' : request['sys']['sunrise'],
    'sunset' : request['sys']['sunset'],
    'description': request['weather'][0]['description']

}




print(data)