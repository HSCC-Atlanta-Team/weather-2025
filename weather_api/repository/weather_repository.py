import requests
import os
from weather_api.models import Weather
from var_dump import var_dump
from .repository import Repository

class WeatherRepository(Repository):
    def get_current_weather(self, options=None):
        url = f"{self.base_url}/weather"
        self.setOptions(options)

        try:
            response = requests.get(url, params=self.options)
            response.raise_for_status()

            data = response.json()
            return Weather.fromApi(data)

        except requests.RequestException as e:
            print(f"Weather API error: {e}")
            return None

    def create_forecast(self, forcast):
        requests.request('get')
