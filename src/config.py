from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_url: PostgresDsn

    class Config:
        env_file = '.env'
