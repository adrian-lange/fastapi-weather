from pydantic import BaseModel
import datetime


class Weather(BaseModel):
    created_at: datetime.date
    hour: datetime.time
    temperature: str
    pressure: str
    humidity: str
    pm_2_5: str
    pm_10: str
    wind: str
