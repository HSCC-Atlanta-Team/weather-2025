from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from var_dump import var_dump
from weather_api.models import CurrentWeather
import json
import sys

# Create your views here.
def weather(request):
    uri = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    response = requests.get(uri)
    data = response.json()    

    new_record = CurrentWeather()
    new_record.hydrate(data);
    new_record.save()

    return render(request, 'current_weather.html', {'weather': new_record})