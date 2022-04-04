from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=090ffecfae05341a427634840e247205'

    response = requests.get(format(url)).json()
