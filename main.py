import flet as ft
import requests
import sys
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Contacts OpenWeatherMap API and requests weather data
def get_weather(city_name):
    if not API_KEY:
        print('Critic ERROR: API key not found. Verify the file .env')
        sys.exit(1)

    parameters = {
        'q' : city_name,
        'appid' : API_KEY,
        'units' : 'metric',
        'lang' : 'en'
    }

    try: 
        response = requests.get(BASE_URL, params=parameters)
        response.raise_for_status()
        return response.json() 
    
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"Backend: City {city_name} not found.")
        elif response.status_code == 401:
            print(f"Backend: API key unvalid")
        else:
            print(f"Backend: Error HTTP: {err}")
        return None
    
    except requests.exceptions.RequestException as err:
        print(f"Backend: Connection error: {err}")
        return None


def main():
    pass

if __name__ == '__main__':
    main()