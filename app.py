# app.py
from flask import Flask, render_template, jsonify, request
from utils.weather_api import WeatherAPI
from utils.alerts import AlertManager
from config.config import Config
import threading
import time

app = Flask(__name__)
weather_api = WeatherAPI()
alert_manager = AlertManager()
weather_data = {}

def update_weather():
    while True:
        try:
            for city in Config.CITIES:
                data = weather_api.get_weather_data(city)
                if data:
                    weather_data[city] = data
                    alert_manager.check_alerts(data)
            time.sleep(Config.UPDATE_INTERVAL)
        except Exception as e:
            print(f"Error in update_weather: {str(e)}")
            time.sleep(60)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/weather')
def get_weather():
    return jsonify({
        'weather_data': weather_data,
        'alerts': alert_manager.alerts
    })

@app.route('/api/weather/city/<city>')
def get_city_weather(city):
    try:
        data = weather_api.get_weather_data_by_name(city)
        if data:
            return jsonify({'success': True, 'data': data})
        return jsonify({'success': False, 'error': 'City not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    update_thread = threading.Thread(target=update_weather)
    update_thread.daemon = True
    update_thread.start()
    app.run(debug=True)