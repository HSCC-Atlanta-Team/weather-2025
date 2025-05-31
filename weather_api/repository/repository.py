import os

class Repository:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv("API_BASE_URL", default="")

        self.options = {
            'APPID': os.getenv("API_KEY", default=""),
            'units': os.getenv("API_UNITS", default=""),
        }

    def setOptions(self, options=None):
        options = options or {}
        self.options.update(options)