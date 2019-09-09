from app.models.energy.constructionset import ConstructionSetAbridged, WallSetAbridged, RoofCeilingSetAbridged, FloorSetAbridged, ApertureSetAbridged, DoorSetAbridged
from app.models.samples.energyconstructionsetabridged import construction_set, wall_set, roof_ceiling_set, floor_set, door_set, aperture_set, construction_set_1
from copy import copy
from pydantic import ValidationError
import pytest


def test_construction_set():
    ConstructionSetAbridged.parse_obj(construction_set)


def test_wall_set():
    WallSetAbridged.parse_obj(wall_set)


def test_roof_set():
    RoofCeilingSetAbridged.parse_obj(roof_ceiling_set)


def test_floor_set():
    FloorSetAbridged.parse_obj(floor_set)


def test_aperture_set():
    ApertureSetAbridged.parse_obj(aperture_set)


def test_construction_set_1():
    ConstructionSetAbridged.parse_obj(construction_set_1)
