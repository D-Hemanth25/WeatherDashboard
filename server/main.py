from fastapi import FastAPI
from caller import *

app = FastAPI()

@app.get("/")
def index():
    return {"message": "welcome"}

@app.get("/weather/{location}")
async def get_weather(location: str):
    weatherObject = getCurrentWeather(location)
    return weatherObject
