from django.db import models
import json

# Create your models here.
class CurrentWeather(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    currentUnits = models.CharField()
    currentValues = models.CharField()
    timestamp = models.DateTimeField(auto_now=True)

    def getTemp(self):
        currentValues = json.loads(self.currentValues)
        currentUnits = json.loads(self.currentUnits)

        return str(currentValues.get('temperature_2m')) + ' ' + currentUnits.get('temperature_2m');
