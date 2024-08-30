import requests
import os
from dotenv import load_dotenv


load_dotenv()


KEY = os.getenv('OPEN_WEATHER_API_KEY')


def getLocationDetails(location):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&appid={KEY}"
    response = requests.request("GET", url)
    locationObject = {
        "place": response.json()[0]["name"], 
        "country": response.json()[0]["country"],
        "latitude": response.json()[0]["lat"],
        "longitude": response.json()[0]["lon"],
    }
    return locationObject


def getCurrentWeather(location):
    placeObject = getLocationDetails(location)
    latitude, longitude = placeObject["latitude"], placeObject["longitude"]
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={KEY}")
    weatherObject = {
        "description": response.json()["weather"][0]["description"],
        "icon": response.json()["weather"][0]["icon"],
        "temperature": response.json()["main"]["temp"],
        "feel": response.json()["main"]["feels_like"],
        "min": response.json()["main"]["temp_min"],
        "max": response.json()["main"]["temp_max"],
    }
    return weatherObject
