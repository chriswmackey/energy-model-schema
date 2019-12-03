from app.models.energy.construction import OpaqueConstruction, WindowConstruction
from app.models.samples.energyconstruction import construction_internal_floor, construction_window, construction_window_blind, construction_roof, construction_wall, construction_window2
from copy import copy
from pydantic import ValidationError
import pytest


def test_cons_window():
    WindowConstruction.parse_obj(construction_window2)


def test_cons_opaqueroof():
    OpaqueConstruction.parse_obj(construction_roof)


def test_cons_opaquewall():
    OpaqueConstruction.parse_obj(construction_wall)


def test_length_opaque():
    cons_length = copy(construction_internal_floor)
    if len(cons_length['materials']) > 10:
        with pytest.raises(ValidationError):
            OpaqueConstruction.parse_obj(
                construction_internal_floor)
    elif len(cons_length['materials']) == 0:
        with pytest.raises(ValidationError):
            OpaqueConstruction.parse_obj(
                construction_internal_floor)


def test_cons_wind():
    wind_len = copy(construction_window)
    if len(wind_len['materials']) > 8:
        with pytest.raises(ValidationError):
            WindowConstruction.parse_obj(construction_window)
    elif len(wind_len['materials']) == 0:
        with pytest.raises(ValidationError):
            WindowConstruction.parse_obj(construction_window)
