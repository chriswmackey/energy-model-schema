from app.models.energy.scheduleruleset import ScheduleRulesetAbridged
from app.models.energy.schedulefixedinterval import ScheduleFixedInterval
from app.models.common.datetime import Date, Time
from app.models.samples.schedule_fixed_interval import schedule_fixed_interval, schedule_fixed_interval1
from copy import copy
from pydantic import ValidationError
import pytest
import os
import json
import pytest
from pathlib import Path
from os import listdir

def test_office_occupancy():
        root = os.path.dirname(os.path.dirname(__file__))
        target_folder = os.path.join(root, 'app','models','samples','json')
        file_path = os.path.join(target_folder, 'schedule_office_occupancy.json')
        ScheduleRulesetAbridged.parse_file(file_path)

def test_primary_school_occupancy():
        root = os.path.dirname(os.path.dirname(__file__))
        target_folder = os.path.join(root, 'app','models','samples','json')
        file_path = os.path.join(target_folder, 'schedule_primary_school_occupancy.json')
        ScheduleRulesetAbridged.parse_file(file_path)

def test_schedule_fixed_interval():
    ScheduleFixedInterval.parse_obj(schedule_fixed_interval)


def test_schedule_fixed_interval1():
    ScheduleFixedInterval.parse_obj(schedule_fixed_interval1)


def test_schedule_fixed_wrong_values():
    wrong_values = copy(schedule_fixed_interval)
    wrong_values['values'] = []
    with pytest.raises(ValidationError):
        ScheduleFixedInterval.parse_obj(wrong_values)