from sqlalchemy import Column, Integer, String, Date, Time

from ..db_setup import Base

class Weather(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date, index=True)
    hour = Column(Time, index=True)
    temperature = Column(String(50), index=True)
    pressure = Column(String(50), index=True)
    humidity = Column(String(50), index=True)
    pm_2_5 = Column(String(50), index=True)
    pm_10 = Column(String(50), index=True)
    wind = Column(String(50), index=True)