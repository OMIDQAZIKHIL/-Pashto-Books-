from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def input_soil_data(request):
    return render(request, 'input_soil_data.html')

def login_page(request):
    return render(request, 'login_page.html')

def weather_climate(request):
    return render(request, 'weather_climate.html')
