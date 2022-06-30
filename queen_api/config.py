from dotenv import dotenv_values, find_dotenv
from pydantic import BaseModel


def get_config():
    dotenv_path = find_dotenv(".env")
    return Config(**dotenv_values(dotenv_path))  # type: ignore
    # we want to fail on None so we disallow it with type hints


class Config(BaseModel):
    DB_HOST: str
    DB_PORT: int

    DB_USER: str
    DB_PASS: str

    DB_DEFAULT_DATABASE: str

    SERVER_HOST: str
    SERVER_PORT: int

    DEBUG: bool

    # type guard/not None validation!
