from pydantic import BaseModel


class Config(BaseModel):
    DB_HOST: str
    DB_PORT: int
    SERVER_HOST: str
    SERVER_PORT: int
    DEBUG: bool
