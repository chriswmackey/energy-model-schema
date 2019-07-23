from app.models.energy.constructionabridged import OpaqueConstructionAbridged, WindowConstructionAbridged
from app.models.samples.energyconstructionabridged import construction_internal_floor, construction_window, construction_window_blind, construction_roof, construction_wall, construction_window2
from copy import copy
from pydantic import ValidationError
import pytest


def test_cons_window():
    WindowConstructionAbridged.parse_obj(construction_window2)


def test_cons_opaqueroof():
    OpaqueConstructionAbridged.parse_obj(construction_roof)


def test_cons_opaquewall():
    OpaqueConstructionAbridged.parse_obj(construction_wall)


def test_length_opaque():
    cons_length = copy(construction_internal_floor)
    if len(cons_length['layers']) > 10:
        with pytest.raises(ValidationError):
            OpaqueConstructionAbridged.parse_obj(
                construction_internal_floor)
    elif len(cons_length['layers']) == 0:
        with pytest.raises(ValidationError):
            OpaqueConstructionAbridged.parse_obj(
                construction_internal_floor)


def test_cons_wind():
    wind_len = copy(construction_window)
    if len(wind_len['layers']) > 8:
        with pytest.raises(ValidationError):
            WindowConstructionAbridged.parse_obj(construction_window)
    elif len(wind_len['layers']) == 0:
        with pytest.raises(ValidationError):
            WindowConstructionAbridged.parse_obj(construction_window)
