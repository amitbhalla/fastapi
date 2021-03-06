import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / "backend/.env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Job Board"
    PROJECT_VERSION: str = "0.1.0"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
        POSTGRES_USER,
        POSTGRES_PASSWORD,
        POSTGRES_SERVER,
        POSTGRES_PORT,
        POSTGRES_DB,
    )


settings = Settings()
