from typing import List
import fastapi
from models import Weather
import datetime
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import get_db, async_get_db
from pydantic_schemas.weather import WeatherCreate, Weather
from api.utils.weathers import get_day, get_days, create_day, get_day_hour

router = fastapi.APIRouter()


@router.get("/api/days", response_model=List[Weather])
async def get_all_days(db: Session = Depends(get_db)):
    users = get_days(db)
    return users

@router.get("/api/day", response_model=Weather)
async def get_one_day(day: datetime.date, db: AsyncSession = Depends(async_get_db)):
    db_day = await get_day(db=db, day=day)
    if db_day is None:
        raise HTTPException(status_code=404, detail="Day not found")
    return db_day

@router.post("/api/day", response_model=Weather, status_code=201)
async def create_measurement(measurement: WeatherCreate, db: Session = Depends(get_db)):
    db_hour = get_day_hour(db=db, day=measurement.created_at, time=measurement.hour)
    if db_hour:
        raise HTTPException(status_code=404, detail="This hour already exists in this day.")
    return create_day(db=db, measurement=measurement)