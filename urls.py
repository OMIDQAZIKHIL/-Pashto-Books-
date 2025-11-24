from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('input-soil-data/', views.input_soil_data, name='input_soil_data'),  # Input Soil Data page
    path('login-page/', views.login_page, name='login_page'),  # Login page
    path('weather_climate/', views.weather_climate, name='weather_climate'),  # Weather Climate page
]
