from typing import List
from fastapi import FastAPI, Path
from models import Weather
import datetime

app = FastAPI(
    title="Fast API",
    description="API for retrieving data about weather.",
    version="0.0.1",
    contact={
        "name": "Adrian",
        "email": "test@test.com",
    },
    license_info={
        "name": "MIT",
    }

)

db: List[Weather] = [
    Weather(
        created_at=datetime.date.today(),
        hour=datetime.datetime.now().strftime("%H:%M:%S"),
        temperature="1",
        pressure="1",
        humidity="1",
        pm_2_5="1",
        pm_10="1",
        wind="1",
        )
]

@app.get("/api/days")
async def get_all_days():
    return db;

@app.get("/api/day")
async def get_one_day(
    date: str = Path(..., description="Date of day you want to retrive (YYYY-MM-DD)")
):
    for weather in db:
        if weather.created_at == date:
            print(weather)
            return weather; 

@app.post("/api/day")
async def create_measurement(measurement: Weather):
    db.append(measurement)
    return db;