import json
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.command import upgrade as alembic_upgrade
from alembic.command import downgrade as alembic_downgrade
from alembic.config import Config as AlembicConfig

from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

from app.main import app
from app.core.config import POSTGRES_USER, POSTGRES_PASS, POSTGRES_HOST, POSTGRES_PORT


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def db(request):
    host_url = f'postgres+psycopg2://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}'
    pg_database_url = '{}/postgres'.format(host_url)
    engine = create_engine(pg_database_url, echo=True)
    conn = engine.connect()
    conn.execute('commit')
    try:
      conn.execute('create database test')
    except:
      pass
    conn.close()

    alembic_config = AlembicConfig('alembic.ini')
    alembic_config.set_main_option('sqlalchemy.url', '{}/test'.format(host_url))
    alembic_upgrade(alembic_config, 'head')
    
    yield

    conn = engine.connect()
    conn.execute("SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'test';")
    conn.execute('commit')
    conn.execute('DROP DATABASE test')
    conn.close()
    engine.dispose()

@pytest.fixture
def get_superuser_token_headers():
    """This is token for test user."""
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlcl9pZ' \
        'CI6IjY3ZDdlNjg3LWRkNGYtNGZlMC1iMWVlLWMyOWJmNzczZDk0NCIsIm5hbWUiOiJ0ZXN0X3VzZX' \
        'IiLCJpYXQiOjE1MTYyMzkwMjJ9.UzO8oEKvYeI-AFRJ6tH5xxntP2jMmRn8wr_sWL6YE_4'

    headers = {"Authorization": f"Bearer {token}"}
    return headers


@pytest.fixture(scope="module")
def created_item_data():
    return {'id': None, 'location': None}


@pytest.fixture
def face_by_face_model():
    with open('tests/fixtures/model_face_by_face.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def pollination_model():
    with open('tests/fixtures/model_pollination.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def opaque_material():
    return {
        "modifier": "void",
        "type": "Opaque",
        "name": "generic_wall",
        "reflectance": 0.5
    }


@pytest.fixture
def plastic_material():
    return {
        "modifier": "void",
        "type": "Plastic",
        "name": "generic_wall",
        "r_reflectance": 0.5,
        "g_reflectance": 0.5,
        "b_reflectance": 0.5,
        "specularity": 0,
        "roughness": 0
    }


@pytest.fixture
def glass_material():
    return {
        "modifier": "void",
        "type": "Glass",
        "name": "generic_glass",
        "r_transmittance": 0.6,
        "g_transmittance": 0.6,
        "b_transmittance": 0.6,
        "refraction_index": 1.52
    }

@pytest.fixture
def transparent_material():
    return {
        "modifier": "void",
        "type": "Transparent",
        "name": "generic_wall",
        "transmittance": 0.5
    }
