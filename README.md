# Real-Time Weather Monitoring System

## Overview
The **Real-Time Weather Monitoring System** is designed to provide users with up-to-date information about weather conditions in major metropolitan areas of India. By leveraging the OpenWeatherMap API, this system continuously retrieves and processes weather data, enabling users to gain insights into current and historical weather patterns.

### Key Functionalities
- **Real-Time Data Retrieval**: The system polls the OpenWeatherMap API at configurable intervals to fetch the latest weather data for six key cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad. This ensures that users always have access to the most recent information.
  
- **Data Processing and Analysis**: Upon receiving weather updates, the system performs several processing tasks, including:
  - **Temperature Conversion**: The application converts temperature values from Kelvin to Celsius (or Fahrenheit), allowing for easier interpretation by users.
  - **Daily Weather Aggregates**: The system aggregates data daily to compute key metrics such as average, maximum, and minimum temperatures. It also determines the dominant weather condition based on the frequency of reported conditions throughout the day.

- **User-Configurable Alerts**: Users can define thresholds for temperature and specific weather conditions (e.g., alerts for extreme heat). The system continuously monitors the latest weather data and triggers alerts when these thresholds are breached, ensuring that users are informed of significant weather changes.

- **Visualizations**: The application provides intuitive visualizations to help users understand daily weather summaries, historical trends, and any alerts triggered by severe weather conditions. These visual representations aid in quickly grasping complex data and trends.

### Significance
The Real-Time Weather Monitoring System serves as an essential tool for both individuals and organizations that require timely weather updates. Whether for daily planning, travel arrangements, or agricultural needs, having access to real-time weather information can significantly impact decision-making. Furthermore, the ability to visualize weather trends and receive alerts enhances situational awareness, enabling users to prepare for adverse weather conditions proactively.

Overall, this project aims to combine data science and real-time processing to deliver a robust and user-friendly weather monitoring solution, ultimately contributing to improved safety and convenience in daily life.

## Getting Started

### Prerequisites
To run this application, you'll need:
- **Python**: Ensure you have Python installed on your system. You can download it from [Python Official Website](https://www.python.org/).
- **Flask**: The web framework for building the application.
- **API Key**: Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/) to obtain your API key.

### Installation
 **Clone the repository**:
  git clone https://github.com/Munitejasree06/weather-monitoring.git

 **Run the application** :

python app.py

### Usage
Once the application is running, you can access the real-time weather data by navigating to http://localhost:5000 in your web browser. You will find the following features:

Enter a city name to fetch its current weather data.
View the daily weather summary and historical trends.
Set temperature thresholds to receive alerts for extreme weather conditions.
### Visualizations
The application provides several visualizations, including:

**Daily Weather Summaries**: View aggregate weather data for each day, including average, maximum, and minimum temperatures.
**Weather Trends**: Historical trends showing how weather conditions change over time.
**Alerts**: Visual indicators when weather conditions exceed user-defined thresholds.

### Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.
