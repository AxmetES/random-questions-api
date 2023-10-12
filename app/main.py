import logging
import uvicorn
import models

from fastapi import FastAPI
from environs import Env

from database import engine
from routers import api

models.Base.metadata.create_all(bind=engine)

env = Env()
env.read_env()

app = FastAPI()
app.include_router(api.router)


logging.basicConfig(
    format="%(levelname)s - %(message)s",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("logs/logfile.log"), logging.StreamHandler()],
)


app.include_router(api.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
