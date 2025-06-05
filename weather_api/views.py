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
def weather(request):
    return render(request, 'weather_grid.html')

def weather_card(request):
    repo = WeatherRepository()
    # parse query parameters: ?q=atlanta
    options = request.GET.dict()
    if 'q' not in options:
        options['q'] = 'Atlanta'

    current_weather = repo.get_current_weather(options=options)

    if current_weather is None:
        return HttpResponse("Failed to fetch weather data.", status=500)

    city = request.GET.get('city')
    weather_icon = 'clear-day'
    return render(request, 'weather_card.html', {'city': options['q'], 'current_weather': current_weather, 'weather_icon': weather_icon})

def weather_icon(request):
    return HttpResponse('this is an icon')
