import requests
import os
from weather_api.models import Weather
from var_dump import var_dump

class WeatherRepository:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv("API_BASE_URL", default="")

    def get_current_weather(self, options=None):
        url = f"{self.base_url}/weather"
        options = options or {}

        try:
            # Inject our API key here
            options['APPID'] = os.getenv("API_KEY", default="")
            # Apply our units setting
            options['units'] = os.getenv("API_UNITS", default="")

            response = requests.get(url, params=options or {})
            response.raise_for_status()

            data = response.json()
            return Weather.fromApi(data)

        except requests.RequestException as e:
            print(f"Weather API error: {e}")
            return None
