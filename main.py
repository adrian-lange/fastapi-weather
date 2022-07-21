from fastapi import FastAPI
from api.weather import router
from db.db_setup import engine
from db.models import weather

weather.Base.metadata.create_all(bind=engine)

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

app.include_router(router)