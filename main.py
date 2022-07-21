from fastapi import FastAPI
from api.weather import router

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