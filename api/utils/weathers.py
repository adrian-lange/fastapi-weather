from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import datetime

from pydantic_schemas.weather import WeatherCreate
from db.models.weather import Weather


async def get_day(db: AsyncSession, day: datetime.date):
    query = select(Weather).where(Weather.created_at == day)
    result = await db.execute(query)
    return result.scalar_one_or_none()

def get_days(db: Session):
    return db.query(Weather).all()

def create_day(db: Session, measurement: WeatherCreate):
    db_weather = Weather(created_at=measurement.created_at, 
    hour=measurement.hour, 
    temperature=measurement.temperature, 
    pressure=measurement.pressure,
    humidity=measurement.humidity,
    pm_2_5=measurement.pm_2_5,
    pm_10=measurement.pm_10,
    wind=measurement.wind
    )
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

def get_day_hour(db: Session, day: datetime.date, time: datetime.time):
    return db.query(Weather).filter(Weather.created_at == day, Weather.hour == time).all()