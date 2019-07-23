from app.models.energy.programset import PeopleAbridged, LightingAbridged, ElectricalEquipmentAbridged, ProgramSetAbridged
from app.models.samples.energyprogramset import program_set_abridged, people_abridged, lighting_abridged, electrical_equipment_abridged
from pydantic import ValidationError
import pytest


def test_program_set():
    ProgramSetAbridged.parse_obj(program_set_abridged)


def test_people():
    PeopleAbridged.parse_obj(people_abridged)


def test_lighting():
    LightingAbridged.parse_obj(lighting_abridged)


def test_electrical_equipment():
    ElectricalEquipmentAbridged.parse_obj(electrical_equipment_abridged)
