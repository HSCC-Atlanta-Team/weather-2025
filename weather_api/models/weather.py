from django.db import models
from .base import BaseModel
import json

class Weather(BaseModel):
    coord = models.JSONField()
    weather = models.JSONField()
    base = models.CharField()
    main = models.JSONField()
    visibility = models.CharField()
    wind = models.JSONField()
    clouds = models.JSONField()
    dt = models.IntegerField()
    sys = models.JSONField()
    timezone = models.CharField()
    name = models.CharField()
    cod = models.IntegerField()

    def getTemp(self):
        temp = self.main.get('temp')
        return f"{temp}°F" if temp is not None else "N/A"