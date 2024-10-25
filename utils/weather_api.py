# utils/weather_api.py
import requests
from datetime import datetime
from config.config import Config

class WeatherAPI:
    def __init__(self):
        self.api_key = Config.OPENWEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def kelvin_to_celsius(self, kelvin):
        return round(kelvin - 273.15, 2)
    
    def get_weather_data(self, city_name):
        coords = Config.CITIES[city_name]
        params = {
            'lat': coords['lat'],
            'lon': coords['lon'],
            'appid': self.api_key
        }
        return self._fetch_weather_data(params)
    
    def get_weather_data_by_name(self, city_name):
        params = {
            'q': city_name,
            'appid': self.api_key
        }
        return self._fetch_weather_data(params)
    
    def _fetch_weather_data(self, params):
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            
            return {
                'city': data['name'],
                'condition': data['weather'][0]['main'],
                'icon': data['weather'][0]['icon'],
                'temp': self.kelvin_to_celsius(data['main']['temp']),
                'feels_like': self.kelvin_to_celsius(data['main']['feels_like']),
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'dt': datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {str(e)}")
            return None