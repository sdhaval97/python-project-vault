# Project 10: Weather App with OpenWeatherMap API

## Project Overview
A command-line weather application that fetches and displays real-time meteorological data from the OpenWeatherMap API. The user can enter any city name and receive a current weather report, including temperature, condition, humidity, and wind speed. This project is a foundational exercise in consuming live data from a third-party API.

## What You'll Learn
- **API Integration**: How to make HTTP GET requests to a REST API using the `requests` library.
- **JSON Parsing**: Reading and extracting nested data from a JSON response.
- **Error Handling**: Gracefully managing potential issues like network errors, invalid API keys, and non-existent locations.
- **Data Presentation**: Formatting and displaying data in a clear, readable, and user-friendly way in the terminal.
- **Environment Management**: Understanding the importance of managing external dependencies with a `requirements.txt` file.

## Features
- **Real-Time Data**: Fetches up-to-the-minute weather information for any city in the world.
- **Key Weather Metrics**: Displays temperature, "feels like" temperature, main condition, humidity, and wind speed.
- **Robust Error Handling**: Provides clear feedback for common errors (e.g., "City not found," "Invalid API key").
- **Clean Interface**: Uses a simple and clean command-line interface with emojis for visual appeal.
- **Continuous Search**: Allows the user to look up weather for multiple cities without restarting the script.

## Crucial Setup: API Key
This application will **NOT** work without an API key from OpenWeatherMap.

1.  **Sign Up**: Go to the [OpenWeatherMap website](https://openweathermap.org/appid) and create a free account.
2.  **Get API Key**: Navigate to the 'API keys' tab in your user profile. A default key will be generated for you.
3.  **Activate Key**: It may take a few minutes to a couple of hours for your new API key to become active.
4.  **Add Key to Code**: Open the `weather_app.py` file and replace the placeholder text `"YOUR_API_KEY_HERE"` with the key you just copied.

## How to Run
1.  **Install Dependencies**: First, install the required `requests` library.
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Script**:
    ```bash
    python weather_app.py
    ```

## Sample Output
```
========================================
  Real-Time Weather Forecast App
========================================
Enter a city name (or 'q' to quit): London

Fetching weather data for London...

========================================
  Weather Forecast for London, GB ☁️
  Timestamp: 2025-09-26 22:30:15
========================================
  🌡️ Temperature: 14.5°C (Feels like: 13.9°C)
  📝 Condition:   Overcast Clouds
  💧 Humidity:    82%
  🌬️ Wind Speed:  4.1 m/s
========================================

Press Enter to check another city...
```

## Code Structure
- `weather_app.py`: The main Python script.
- `get_weather_data()`: Handles the API request, including passing parameters and managing potential network or HTTP errors.
- `display_weather()`: Parses the JSON data and prints it in a formatted, user-friendly way.
- `main()`: The main controller that runs the application loop and handles user input.

## Enhancements (Optional)
- **GUI Version**: Build a graphical front-end using a library like Tkinter or PyQt.
- **Data Caching**: Store recent search results locally to avoid making redundant API calls.
- **Hourly/Daily Forecast**: Extend the app to fetch and display a 5-day or hourly forecast, which is available through other OpenWeatherMap API endpoints.
- **Auto-Location**: Use a library like `geopy` to detect the user's location based on their IP address and show the local weather automatically.

## Time Estimate
**Beginner**: 90-120 minutes (plus API key activation time)
**With enhancements**: 4-6 hours

## Key Concepts
- REST APIs
- `requests` library
- JSON data structure
- Error/Exception Handling
- Environment Variables (for securely storing API keys)
