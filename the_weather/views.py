from django.shortcuts import render
import requests

from the_weather.models import City

# Create your views here.
def index(request):
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=090ffecfae05341a427634840e247205'

    cities = City.objects.all()
    weather_data = []
    for city in cities:
        response = requests.get(format(city)).json()

    city_weather = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'humidity': response['main']['humidity'],
        'pressure': response['main']['pressure'],
        'wind': response['wind']['speed']
    }

    weather_data.append(city_weather)