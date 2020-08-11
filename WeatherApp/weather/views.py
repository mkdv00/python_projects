import requests
from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):
    app_id = 'c4646362a19e75184ddc7b4d95cf11cd'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id

    if(request.method) == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        # Отправляю запрос на сервер
        response = requests.get(url.format(city.name)).json()
        # Создаю словарь
        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
