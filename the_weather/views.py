from django.shortcuts import render
import requests
from .forms import CityForm
from the_weather.models import City

# Create your views here.


def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=090ffecfae05341a427634840e247205'
    err_message = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                response = requests.get(url.format(new_city)).json()    
                if response['cod'] == 200:
                    msg = 'City Added Successfully'
                    form.save()
                else:
                    err_message = 'City weather record not available at moment'
            else:
                err_message = 'City Already Exist'

        if err_message:
            message = err_message
            message_class = 'is-danger'
        else:
            message = msg
            message_class = 'is-success'

    form = CityForm()
    weather_data = []

    cities = City.objects.all()
    for city in cities:
        response = requests.get(url.format(city)).json()


        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
            'humidity': response['main']['humidity'],
            'pressure': response['main']['pressure'],
            'wind': response['wind']['speed']
        }

        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class,

    }
    return render(request, 'the_weather/index.html', context)
