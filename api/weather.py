import fastapi
from models import Weather
import datetime

router = fastapi.APIRouter()

users = []

@router.get("/api/days")
async def get_all_days():
    return users;

@router.get("/api/day")
async def get_one_day(date: datetime.date):
    values = []
    for list in users:
        if list.created_at == date:
            values.append(list)
    return values; 

@router.post("/api/day")
async def create_measurement(measurement: Weather):
    users.append(measurement)
    return users;