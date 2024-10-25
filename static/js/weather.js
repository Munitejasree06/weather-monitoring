//weather.js
let weatherData = {};



function updateWeather() {
    fetch('/api/weather')
        .then(response => response.json())
        .then(data => {
            weatherData = data.weather_data;
            updateAlerts(data.alerts);
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
        });
}

function searchCustomCity() {
    const cityInput = document.getElementById('custom-city');
    const city = cityInput.value.trim();
    const errorDiv = document.getElementById('search-error');
    const loadingSpinner = document.getElementById('loading-spinner');
    
    if (!city) {
        errorDiv.textContent = 'Please enter a city name';
        errorDiv.classList.remove('hidden');
        return;
    }
    
    // Show loading spinner
    loadingSpinner.classList.remove('hidden');
    errorDiv.classList.add('hidden');
    
    fetch(`/api/weather/city/${encodeURIComponent(city)}`)
        .then(response => response.json())
        .then(result => {
            loadingSpinner.classList.add('hidden');
            
            if (result.success) {
                displayWeatherData(result.data);
            } else {
                errorDiv.textContent = result.error || 'City not found';
                errorDiv.classList.remove('hidden');
            }
        })
        .catch(error => {
            loadingSpinner.classList.add('hidden');
            errorDiv.textContent = 'Error fetching weather data';
            errorDiv.classList.remove('hidden');
            console.error('Error:', error);
        });
}

function displayWeatherData(data) {
    document.getElementById('weather-display').classList.remove('hidden');
    
    document.getElementById('selected-city').textContent = data.city;
    document.getElementById('weather-icon').src = `http://openweathermap.org/img/wn/${data.icon}@2x.png`;
    document.getElementById('weather-condition').textContent = data.condition;
    document.getElementById('temperature').textContent = `${data.temp}°C`;
    document.getElementById('feels-like').textContent = `${data.feels_like}°C`;
    document.getElementById('humidity').textContent = `${data.humidity}%`;
    document.getElementById('wind-speed').textContent = `${data.wind_speed} m/s`;
    document.getElementById('last-updated').textContent = data.dt;
}

function showWeather(city) {
    const data = weatherData[city];
    if (!data) {
        alert('Weather data not available for ' + city);
        return;
    }
    
    displayWeatherData(data);
    
    // Highlight the selected button
    document.querySelectorAll('.metro-btn').forEach(btn => {
        if (btn.textContent === city) {
            btn.style.background = 'linear-gradient(135deg, #2c6aa0, #1d4e79)';
        } else {
            btn.style.background = 'linear-gradient(135deg, #4a90e2, #357abd)';
        }
    });
}

function updateAlerts(alerts) {
    const alertsContainer = document.getElementById('alerts-container');
    alertsContainer.innerHTML = '';
    
    if (!alerts || alerts.length === 0) {
        const noAlertsElement = document.createElement('div');
        noAlertsElement.className = 'text-gray-500 text-center py-4';
        noAlertsElement.textContent = 'No active weather alerts';
        alertsContainer.appendChild(noAlertsElement);
        return;
    }
    
    alerts.forEach(alert => {
        const alertElement = document.createElement('div');
        alertElement.className = 'alert bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-2';
        
        const alertContent = document.createElement('div');
        alertContent.className = 'flex justify-between items-center';
        
        const alertText = document.createElement('span');
        alertText.textContent = alert.text;
        
        const alertTime = document.createElement('span');
        alertTime.className = 'text-sm text-gray-600';
        alertTime.textContent = alert.timestamp;
        
        alertContent.appendChild(alertText);
        alertContent.appendChild(alertTime);
        alertElement.appendChild(alertContent);
        
        alertsContainer.appendChild(alertElement);
    });
}

// Add event listener for Enter key in the search input
document.addEventListener('DOMContentLoaded', () => {
    const cityInput = document.getElementById('custom-city');
    cityInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            searchCustomCity();
        }
    });
    
    // Initial weather update
    updateWeather();
});

// Update weather data every 5 minutes
setInterval(updateWeather, 300000);