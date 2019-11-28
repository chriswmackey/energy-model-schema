from app.models.energy.scheduleruleset import ScheduleRulesetAbridged
from app.models.energy.schedulefixedinterval import ScheduleFixedIntervalAbridged
from app.models.common.datetime import Date, Time
from copy import copy
from pydantic import ValidationError
import pytest
import os
import json
import pytest
from pathlib import Path
from os import listdir


def test_ruleset_office_occupancy():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'schedule_ruleset_office_occupancy.json')
    ScheduleRulesetAbridged.parse_file(file_path)


def test_primary_school_occupancy():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'schedule_primary_school_occupancy.json')
    ScheduleRulesetAbridged.parse_file(file_path)    


def test_ruleset_simple_repeating():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'schedule_ruleset_simple_repeating.json')
    ScheduleRulesetAbridged.parse_file(file_path)


def test_fixedinterval_increasing_fine_timestep():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'schedule_fixedinterval_increasing_fine_timestep.json')
    ScheduleFixedIntervalAbridged.parse_file(file_path)


def test_fixedinterval_increasing_single_day():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'schedule_fixedinterval_increasing_single_day.json')
    ScheduleFixedIntervalAbridged.parse_file(file_path)


def test_fixedinterval_random_annual():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'schedule_fixedinterval_random_annual.json')
    ScheduleFixedIntervalAbridged.parse_file(file_path)
