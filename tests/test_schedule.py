from app.models.energy.scheduleruleset import ScheduleRulesetAbridged
from app.models.energy.schedulefixedinterval import ScheduleFixedIntervalAbridged
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'app', 'models', 'samples')


def test_ruleset_office_occupancy():
    file_path = os.path.join(
        target_folder, 'schedule_ruleset_office_occupancy.json')
    ScheduleRulesetAbridged.parse_file(file_path)


def test_primary_school_occupancy():
    file_path = os.path.join(
        target_folder, 'schedule_primary_school_occupancy.json')
    ScheduleRulesetAbridged.parse_file(file_path)    


def test_ruleset_simple_repeating():
    file_path = os.path.join(
        target_folder, 'schedule_ruleset_simple_repeating.json')
    ScheduleRulesetAbridged.parse_file(file_path)


def test_fixedinterval_increasing_fine_timestep():
    file_path = os.path.join(
        target_folder, 'schedule_fixedinterval_increasing_fine_timestep.json')
    ScheduleFixedIntervalAbridged.parse_file(file_path)


def test_fixedinterval_increasing_single_day():
    file_path = os.path.join(
        target_folder, 'schedule_fixedinterval_increasing_single_day.json')
    ScheduleFixedIntervalAbridged.parse_file(file_path)


def test_fixedinterval_random_annual():
    file_path = os.path.join(
        target_folder, 'schedule_fixedinterval_random_annual.json')
    ScheduleFixedIntervalAbridged.parse_file(file_path)
