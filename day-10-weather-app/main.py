import requests
import os
import json
from datetime import datetime

API_KEY = "4793fd8e4b457992a0e0578d8fe3128e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_weather_data(city):
    """Fetches weather data from the OpenWeatherMap API."""
    if API_KEY == "4793fd8e4b457992a0e0578d8fe3128e":
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
        if response.status_code == 401:
            return None, "Authentication failed."
        elif response.status_code == 404:
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
    
    