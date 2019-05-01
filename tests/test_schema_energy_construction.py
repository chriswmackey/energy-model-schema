from app.models.energy.construction import EnergyConstruction, EnergyMaterial
from app.models.samples.construction import in_material, in_const
from copy import copy
from pydantic import ValidationError
import pytest


def test_material():
    EnergyMaterial.parse_obj(in_material)


def test_construction():
    EnergyConstruction.parse_obj(in_const)


def test_construction_no_material():
    const = copy(in_const)
    const['materials'] = []
    with pytest.raises(ValidationError):
        EnergyConstruction.parse_obj(const)
