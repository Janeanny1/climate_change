from django.shortcuts import render
import urllib.request
import json

def index(request):
    weather_data = {}

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            try:
                source = urllib.request.urlopen(
                    f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=830fa36612df55b135fa8b63ba140d5b&units=metric'
                ).read()
                current_data = json.loads(source)

                forecast_source = urllib.request.urlopen(
                    f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=830fa36612df55b135fa8b63ba140d5b&units=metric'
                ).read()
                forecast_data = json.loads(forecast_source)

                weather_data = {
                    'city': current_data['name'],
                    'country': current_data['sys']['country'],
                    'coordinates': current_data['coord'],
                    'temperature': current_data['main']['temp'],
                    'pressure': current_data['main']['pressure'],
                    'humidity': current_data['main']['humidity'],
                    'wind': current_data['wind'],
                    'forecast': forecast_data['list'][:5],
                }

            except urllib.error.URLError as e:
                weather_data['error'] = f'Network error: {str(e)}'
            except json.JSONDecodeError:
                weather_data['error'] = 'Error parsing weather data'
            except KeyError:
                weather_data['error'] = 'Invalid data received from weather service'
            except Exception as e:
                weather_data['error'] = f'An error occurred: {str(e)}'

    return render(request, "index.html", {"weather_data": weather_data})
