import os
import requests

class Repository:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv("API_BASE_URL", default="")

        self.options = {
            'APPID': os.getenv("API_KEY", default=""),
            'units': os.getenv("API_UNITS", default=""),
        }

    def send(self, url, method, params=None):
        params = params or {}

        # merge our passed params with defautl options
        self.options.update(params)
        
        # prepend our base_url   
        url = f"{self.base_url}/{url}"

        try:
            response = requests.request(method, url, params=self.options)
            response.raise_for_status()

            data = response.json()
        except requests.RequestException as e:
            print(f"API error: {e}")
            return None

        return data