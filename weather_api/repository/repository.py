import os
import requests

class Repository:
    def __init__(self, base_url=None):
        # We initialize an instance of this class by setting some class properties
        # These are all common parameters that will be sent with EVERY request

        # Our base URL for the api
        self.base_url = base_url or os.getenv("API_BASE_URL", default="")

        # Our API key and "units" setting- both get sent as GET query string parameters,
        # so we create a dict to hold them
        self.options = {
            'APPID': os.getenv("API_KEY", default=""),
            'units': os.getenv("API_UNITS", default=""),
        }

    """
    Send an API request

    Args:
        url: (str) the endpoint URL for the request
        method: (str) the HTTP request method to use (GET, POST, PUT, DELETE, etc.)
        params: (dict) request parameters

    Returns:
        A dict representing the response JSON
    """
    def send(self, url, method, params=None):
        # ensure params is a  dict
        params = params or {}

        # merge our passed params with default options
        self.options.update(params)
        
        # prepend our base_url   
        url = f"{self.base_url}/{url}"

        try:
            # Send the request using the "request" method of the requests module
            # (instead of the get() or post() type methods in the module)
            response = requests.request(method, url, params=self.options)

            # This will raise an error if the request response status is NOT 200 (ok)
            response.raise_for_status()

            # Convert the reponse JSON to a dict
            data = response.json()

        # Error handling
        except requests.RequestException as e:
            print(f"API error: {e}")
            return None

        return data