from pydantic import BaseModel
import datetime

class WeatherBase(BaseModel):
    created_at: datetime.date
    hour: datetime.time
    temperature: str
    pressure: str
    humidity: str
    pm_2_5: str
    pm_10: str
    wind: str

class WeatherCreate(WeatherBase):
    ...

class Weather(WeatherBase):
    ...

    class Config:
        orm_mode = True