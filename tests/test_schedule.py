from app.models.energy.ScheduleRuleset import ScheduleTypeLimits, DayValue, ScheduleDay, ScheduleRuleset, ScheduleRule
from app.models.energy.ScheduleFile import ScheduleFile
from app.models.energy.ScheduleBase import ScheduleContinuous, ScheduleDiscrete, ScheduleNumericType, ScheduleUnitType, Date, Time, DateTime
from app.models.samples.schedule_ruleset import schedule_ruleset, schedule_ruleset_1
from app.models.samples.schedule_file import schedule_file
from copy import copy
from pydantic import ValidationError
import pytest


def test_schedule_rule():
    ScheduleRuleset.parse_obj(schedule_ruleset)


def test_schedule_rule1():
    ScheduleRuleset.parse_obj(schedule_ruleset_1)


def test_schedule_rule_wrong():
    wrong_schedule_type_limits = copy(schedule_ruleset_1)
    wrong_schedule_type_limits['schedule_type_limits']['numeric_type'] = 'Empty'
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_schedule_type_limits)
    wrong_lower_limit = copy(schedule_ruleset_1)
    wrong_lower_limit['lower_limit_value'] = -1
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_lower_limit)
    wrong_default_day = copy(schedule_ruleset_1)
    wrong_default_day['default_day_schedule']['day_values'][0]['time']['hour'] = 25
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_default_day)
    wrong_default_day_minute = copy(schedule_ruleset_1)
    wrong_default_day_minute['default_day_schedule']['day_values'][2]['time']['minute'] = 59.5
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_default_day_minute)
    wrong_schedule_rule = copy(schedule_ruleset_1)
    wrong_schedule_rule['schedule_rules'][0]['start_period']['date']['month'] = 24
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_schedule_rule)
    wrong_leap_year = copy(schedule_ruleset_1)
    wrong_leap_year['schedule_rules'][0]['start_period']['is_leap_year'] = 'Yes'
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_leap_year)


def test_schedule_file():
    ScheduleFile.parse_obj(schedule_file)


def test_schedule_file_wrong():
    wrong_values = copy(schedule_file)
    wrong_values['values'] = []
    with pytest.raises(ValidationError):
        ScheduleFile.parse_obj(wrong_values)
    wrong_start = copy(schedule_file)
    wrong_start['start_day_of_year'] = 367
    with pytest.raises(ValidationError):
        ScheduleFile.parse_obj(wrong_start)
    wrong_unit = copy(schedule_file)
    wrong_unit['unit_type'] = 'Nil'
    with pytest.raises(ValidationError):
        ScheduleFile.parse_obj(wrong_unit)
