from app.models.energy.programset import People, Lighting, ElectricalEquipment, ProgramSet
from app.models.samples.energyprogramset import program_set, people, lighting, electrical_equipment
from pydantic import ValidationError
import pytest


def test_program_set():
    ProgramSet.parse_obj(program_set)


def test_people():
    People.parse_obj(people)


def test_lighting():
    Lighting.parse_obj(lighting)


def test_electrical_equipment():
    ElectricalEquipment.parse_obj(electrical_equipment)
