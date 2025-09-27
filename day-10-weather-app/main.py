import requests
import os
import json
from datetime import datetime

API_KEY = "6035fc0721ca386ce38ba22e51c215ec"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_weather_data(city):
    """Fetches weather data from the OpenWeatherMap API."""
    if API_KEY == "6035fc0721ca386ce38ba22e51c215ec":
        return None, "API key is not set."
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'   
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json(), None
    
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 401:
            return None, "Authentication failed."
        elif http_err.response.status_code == 404:
            return None, f"{city} not found. Please check the spelling."
        else:
            return None, f"An HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return None, f"A network error occurred: {req_err}"

def display_weather(data):
    """Formats and displays parsed weather data."""
    if not data:
        return
    
    main = data.get('main', {})
    weather = data.get('weather', [{}])[0]
    wind = data.get('wind', {})
    sys_info = data.get('sys', {})
    
    city = data.get('name')
    country = sys_info.get('country')
    description = weather.get('description', 'N/A').title()
    temp = main.get('temp')
    feels_like = main.get('feels_like')
    humidity = main.get('humidity')
    wind_speed = wind.get('speed')
    
    # Weather emojis for better visualization
    weather_icons = {
        "Clear": "☀️", "Clouds": "☁️", "Rain": "🌧️",
        "Drizzle": "💧", "Thunderstorm": "⛈️", "Snow": "❄️",
        "Mist": "🌫️", "Smoke": "🌫️", "Haze": "🌫️",
        "Dust": "💨", "Fog": "🌫️", "Sand": "💨",
        "Ash": "🌋", "Squall": "🌬️", "Tornado": "🌪️"
    }
    icon = weather_icons.get(weather.get('main'), '🌐')

    print("\n" + "="*40)
    print(f"  Weather Forecast for {city}, {country} {icon}")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*40)
    
    print(f"  🌡️ Temperature: {temp}°C (Feels like: {feels_like}°C)")
    print(f"  📝 Condition:   {description}")
    print(f"  💧 Humidity:    {humidity}%")
    print(f"  🌬️ Wind Speed:  {wind_speed} m/s")
    
    print("="*40)


def main():
    """Main application controller."""
    while True:
        clear_screen()
        print("========================================")
        print("  Real-Time Weather Forecast App")
        print("========================================")
        city = input("Enter a city name (or 'q' to quit): ").strip()

        if city.lower() == 'q':
            print("\nGoodbye! 👋")
            break

        if not city:
            print("\n❌ City name cannot be empty.")
            input("Press Enter to try again...")
            continue
            
        print(f"\nFetching weather data for {city}...")
        weather_data, error = get_weather_data(city)

        if error:
            print(f"\n❌ Error: {error}")
        else:
            display_weather(weather_data)
        
        input("\nPress Enter to check another city...")


if __name__ == "__main__":
    main()
    
    