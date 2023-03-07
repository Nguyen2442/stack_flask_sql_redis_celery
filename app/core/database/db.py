
from app.config import settings



user = settings.POSTGRES_USER
password = settings.POSTGRES_PASSWORD
host = settings.POSTGRES_HOST
database = settings.POSTGRES_DB
port = settings.POSTGRES_PORT


DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'