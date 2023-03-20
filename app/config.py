from typing import Optional, List, Union, Tuple
from pydantic import BaseSettings
import os


class AppEnvConfig(BaseSettings):
    APP_PROJECT_NAME = "demo-flask-sql-redis-celery"
    APP_DEBUG: bool = True
    APP_DOCS_URL: Optional[str] = '/docs'

    GUNICORN_HOST: str = '0.0.0.0'
    GUNICORN_PORT: str = '8000'

    POSTGRES_HOST: str = 'localhost'
    POSTGRES_DB: str = 'postgres'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_PORT: str = '5432'

    REDIS_URL: str = "127.0.0.1"
    REDIS_RESPONSE: bool = True
    REDIS_DB: int = 9
    
    BROKER_URL: str = "redis://127.0.0.1/9"
    BACKEND_URL: str = "redis://127.0.0.1/9"
    
    SECRET_KEY: str =  'nguyennt65'
    SECURITY_ALGORITHM: str = 'HS256'

    class Config:
        case_sensitive = True
        validate_assignment = True


settings = AppEnvConfig(_env_file='.env')
if __name__ == "__main__":
    pass