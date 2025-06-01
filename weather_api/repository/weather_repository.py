import os
from weather_api.models import Weather
from var_dump import var_dump
from .repository import Repository

class WeatherRepository(Repository):
    def get_current_weather(self, options=None):
        data = self.send('/weather', 'get', options)
        
        return Weather.fromApi(data)
