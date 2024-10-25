from config.config import Config
from datetime import datetime

class AlertManager:
    def __init__(self):
        self.previous_readings = {}
        self.alert_count = {}
        self.alerts = []  # Store alerts with timestamps
        self.max_alerts = 10  # Maximum number of alerts to keep
    
    def add_alert(self, alert_text, city):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.alerts.insert(0, {
            'text': alert_text,
            'city': city,
            'timestamp': timestamp,
            'id': len(self.alerts)
        })
        # Keep only the latest alerts
        self.alerts = self.alerts[:self.max_alerts]
    
    def check_alerts(self, weather_data):
        city = weather_data['city']
        
        # Temperature alert
        if weather_data['temp'] > Config.ALERT_THRESHOLDS['temperature']:
            if city not in self.alert_count:
                self.alert_count[city] = 1
            else:
                self.alert_count[city] += 1
            
            if self.alert_count[city] >= Config.ALERT_THRESHOLDS['consecutive_alerts']:
                self.add_alert(
                    f"High temperature in {city}: {weather_data['temp']}°C",
                    city
                )
        else:
            self.alert_count[city] = 0
        
       
        
        return self.alerts
