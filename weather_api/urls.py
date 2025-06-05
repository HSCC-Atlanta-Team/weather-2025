from django.urls import path

from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('weather-card', views.weather_card, name='weather-card'),
    path('weather-icon', views.weather_icon, name='weather-icon'),
]