from django.db import models
from .base import BaseModel
import json

class CurrentWeather(BaseModel):
    latitude = models.FloatField()
    longitude = models.FloatField()
    current_units = models.CharField()
    current = models.CharField()
    timestamp = models.DateTimeField(auto_now=True)

    def getTemp(self):
        currentValues = json.loads(self.current)
        currentUnits = json.loads(self.current_units)

        return str(currentValues.get('temperature_2m')) + ' ' + currentUnits.get('temperature_2m');