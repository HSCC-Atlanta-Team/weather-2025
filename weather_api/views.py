from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from var_dump import var_dump
from weather_api.models import CurrentWeather
import json
import sys
from .repository.weather_repository import WeatherRepository

# Create your views here.
def weather_old(request):
    uri = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    response = requests.get(uri)
    data = response.json()    

    new_record = CurrentWeather.fromApi(data)

    return render(request, 'current_weather.html', {'weather': new_record})

def weather(request):
    repo = WeatherRepository()
    
    # parse query parameters: ?city=atlanta
    options = request.GET.dict()
    if 'q' not in options:
        options['q'] = 'Atlanta,US'

    current_weather = repo.get_current_weather(options=options)

    if current_weather is None:
        return HttpResponse("Failed to fetch weather data.", status=500)

    var_dump(current_weather)
    current_weather.save()

    return render(request, 'weather.html', {'weather': current_weather})