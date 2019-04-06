import json
import pytest


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