import os

from environs import Env

env = Env()
env.read_env()


class Settings:
    QUESTIONS_URL = env.str("QUESTIONS_URL", "https://jservice.io/api/random?count={}")
    POSTGRES_USER = env.str("POSTGRES_USER")
    POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
    POSTGRES_DB = env.str("POSTGRES_DB")
    POSTGRES_HOST = env.str("POSTGRES_HOST")


settings = Settings()
os.makedirs("logs", exist_ok=True)

