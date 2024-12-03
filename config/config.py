class Config:
    OPENWEATHER_API_KEY = "c85482eb18cfead5d7ad88036a34e328"
    CITIES = {
        
        'Delhi': {'lat': 28.6139, 'lon': 77.2090},
        'Mumbai': {'lat': 19.0760, 'lon': 72.8777},
        'Chennai': {'lat': 13.0827, 'lon': 80.2707},
        'Bangalore': {'lat': 12.9716, 'lon': 77.5946},
        'Kolkata': {'lat': 22.5726, 'lon': 88.3639},
        'Hyderabad': {'lat': 17.3850, 'lon': 78.4867}
    }
    UPDATE_INTERVAL = 300  # 5 minutes in seconds
    ALERT_THRESHOLDS = {
        'temperature': 35,
        'consecutive_alerts': 2,
        
    }
