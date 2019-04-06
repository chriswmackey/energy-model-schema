import os

from dotenv import load_dotenv
from starlette.datastructures import CommaSeparatedStrings, URLPath, Secret, URL

load_dotenv('.env')

DATABASE_URL = os.getenv('DATABASE_URL', '')
if not DATABASE_URL:
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', 5432))
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASS = os.getenv('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_NAME = os.getenv('POSTGRES_DB', 'postgres')

    DATABASE_URL = URL(
        f'postgres+psycopg2://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}'
    )
else:
    DATABASE_URL = URL(DATABASE_URL)

PROJECT_NAME = os.getenv('PROJECT_NAME', 'Pollination Cloud')
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv('ALLOWED_HOSTS', ''))
