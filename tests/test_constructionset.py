from app.models.energy.constructionset import ConstructionSet, WallSet, RoofCeilingSet, FloorSet, ApertureSet, DoorSet
from app.models.samples.energyconstructionset import construction_set, wall_set, roof_ceiling_set, floor_set, door_set, aperture_set
from copy import copy
from pydantic import ValidationError
import pytest


def test_construction_set():
    ConstructionSet.parse_obj(construction_set)


def test_wall_set():
    WallSet.parse_obj(wall_set)


def test_roof_set():
    RoofCeilingSet.parse_obj(roof_ceiling_set)


def test_floor_set():
    FloorSet.parse_obj(floor_set)


def test_aperture_set():
    ApertureSet.parse_obj(aperture_set)



