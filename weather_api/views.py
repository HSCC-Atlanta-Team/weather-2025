from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from var_dump import var_dump
from weather_api.models import CurrentWeather
import json

# Create your views here.
def index(request):
    return render(request, 'hello_world.html', {'name': 'jamie'})

def weather(request):
    uri = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
    response = requests.get(uri)
    data = response.json()    
    validData = {
        'longitude': data.get('longitude'),
        'latitude': data.get('latitude'),
        'currentValues': json.dumps(data.get('current')),
        'currentUnits': json.dumps(data.get('current_units')),
    }

    new_record = CurrentWeather(**validData)
    new_record.save()

    return render(request, 'current_weather.html', {'weather': new_record})