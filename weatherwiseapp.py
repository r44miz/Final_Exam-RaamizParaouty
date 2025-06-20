# -*- coding: utf-8 -*-
"""WeatherWiseApp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q2bsGErdEg_blnpH3b9KPrr3SrfZuVXb

Old Code WeatherWise
"""

import requests

def safe_weather_data_fetch(city):
    """Fetch weather data for a city from wttr.in API - Week 8 version"""
    try:
        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()

        weather_info = {
            'city': city,
            'temperature': data['current_condition'][0]['temp_C'],
            'wind_speed': data['current_condition'][0]['windspeedKmph'],
            'description': data['current_condition'][0]['weatherDesc'][0]['value']
        }
        return weather_info
    except:
        return "Error occurred"

def ideal_safe_weather_data_fetch(city):
    """Improved version using Week 8 error handling concepts"""
    try:
        # Basic input validation - Week 6 concept
        if not city:
            print("Error: City name cannot be empty")
            return None

        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()

        # Safe data extraction with basic error checking
        try:
            current = data['current_condition'][0]
            weather_info = {
                'city': city,
                'temperature': current['temp_C'],
                'wind_speed': current['windspeedKmph'],
                'description': current['weatherDesc'][0]['value']
            }
            return weather_info
        except:
            print("Error: Could not extract weather data from response")
            return None

    except:
        print("Error: Could not connect to weather service")
        return None

"""New Code"""

import requests

def refined_safe_weather_data_fetch(city):
    """
    Fetch weather data using basic input validation and exception handling.
    Week 8 style: No advanced exception types or modules.

    >>> refined_safe_weather_data_fetch("")  # empty input
    Error: City name cannot be empty

    >>> refined_safe_weather_data_fetch("InvalidCity123") # doctest: +SKIP
    Error: Could not connect to weather service

    >>> result = refined_safe_weather_data_fetch("London") # doctest: +SKIP
    >>> isinstance(result, dict)
    True
    """
    if not city:
        print("Error: City name cannot be empty")
        return None

    try:
        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()

        try:
            current = data['current_condition'][0]
            weather_info = {
                'city': city,
                'temperature': current['temp_C'],
                'wind_speed': current['windspeedKmph'],
                'description': current['weatherDesc'][0]['value']
            }
            return weather_info
        except:
            print("Error: Could not extract weather data from response")
            return None

    except:
        print("Error: Could not connect to weather service")
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)