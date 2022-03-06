from pydantic import BaseModel


class Config(BaseModel):
    DB_HOST: str
    DB_PORT: int

    DB_USER: str
    DB_PASS: str

    DB_DEFAULT_DATABASE: str

    SERVER_HOST: str
    SERVER_PORT: int

    DEBUG: bool
