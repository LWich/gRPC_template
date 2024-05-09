import os
from dotenv import load_dotenv


load_dotenv()


SERVER_ADDR = '[::]'
SERVER_PORT = 50051


def get_postgres_url() -> str:
    host = os.environ.get('DB_HOST', 'localhost')
    port = 5432
    password = os.environ.get('DB_PASSWORD', '12345678')
    user = os.environ.get('DB_USER')
    db_name = os.environ.get('DB_NAME')
    return f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}'
