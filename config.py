from pydantic import BaseSettings, Field
from pathlib import Path

class postgresSettings(BaseSettings):
    POSTGRES_DB_NAME : str = Field(..., env= 'POSTGRES_DB_NAME')
    POSTGRES_USER : str = Field(..., env = 'POSTGRES_USER')
    POSTGRES_PORT : str = Field(..., env = 'POSTGRES_PORT')
    POSTGRES_PASSWORD : str = Field(..., env = 'POSTGRES_PASSWORD')
    POSTGRES_TABLE_NAME : str = Field(..., env = 'POSTGRES_TABLE_NAME')
    POSTGRES_HOST : str = Field(..., env = 'POSTGRES_HOST')

    class Config:
        env_file = '.env'

def get_postgres_settings():
    return postgresSettings()
