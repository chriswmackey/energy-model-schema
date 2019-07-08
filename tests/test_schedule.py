from app.models.energy.scheduleruleset import ScheduleTypeLimits, DayValue, ScheduleDay, ScheduleRuleset, ScheduleRule
from app.models.energy.schedulefixedinterval import ScheduleFixedInterval
from app.models.energy.schedulebase import ScheduleContinuous, ScheduleDiscrete, ScheduleNumericType, ScheduleUnitType
from app.models.common.datetime import Date, Time
from app.models.samples.schedule_ruleset import schedule_ruleset, schedule_ruleset_1
from app.models.samples.schedule_fixed_interval import schedule_fixed_interval, schedule_fixed_interval1
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


def test_schedule_rule_wrong_lower():
    wrong_lower_limit = copy(schedule_ruleset_1)
    wrong_lower_limit['schedule_type_limits']['lower_limit_value'] = -1
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_lower_limit)


def test_schedule_rule_wrong_month():
    wrong_month = copy(schedule_ruleset_1)
    wrong_month['schedule_rules'][0]['start_period']['date']['month'] = 13
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_month)


def test_schedule_wrong_hour():
    wrong_default_day = copy(schedule_ruleset_1)
    wrong_default_day['default_day_schedule']['day_values'][0]['time']['hour'] = 25
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_default_day)


def test_schedule_wrong_minute():
    wrong_default_day_minute = copy(schedule_ruleset_1)
    wrong_default_day_minute['default_day_schedule']['day_values'][0]['time']['minute'] = 59.5
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_default_day_minute)


def test_schedule_wrong_day():
    wrong_schedule_rule = copy(schedule_ruleset_1)
    wrong_schedule_rule['schedule_rules'][0]['start_period']['date']['day'] = 32
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_schedule_rule)


def test_schedule_wrong_year():
    wrong_leap_year = copy(schedule_ruleset_1)
    wrong_leap_year['schedule_rules'][0]['start_period']['date']['is_leap_year'] = 'Yes'
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_leap_year)


def test_schedule_wrong_time():
    wrong_time = copy(schedule_ruleset_1)
    wrong_time['schedule_rules'][0]['start_period']['time']['hour'] = 24
    wrong_time['schedule_rules'][0]['start_period']['time']['minute'] = 20
    with pytest.raises(ValidationError):
        ScheduleRuleset.parse_obj(wrong_time)


def test_schedule_fixed_interval():
    ScheduleFixedInterval.parse_obj(schedule_fixed_interval)


def test_schedule_fixed_interval1():
    ScheduleFixedInterval.parse_obj(schedule_fixed_interval1)


def test_schedule_fixed_wrong_values():
    wrong_values = copy(schedule_fixed_interval)
    wrong_values['values'] = []
    with pytest.raises(ValidationError):
        ScheduleFixedInterval.parse_obj(wrong_values)


def test_schedule_fixed_wrong_type():
    wrong_type = copy(schedule_fixed_interval)
    wrong_type['type'] = 'wrongtype'
    with pytest.raises(ValidationError):
        ScheduleFixedInterval.parse_obj(wrong_type)


def test_schedule_fixed_wrong_date():
    wrong_date = copy(schedule_fixed_interval)
    wrong_date['start_date']['month'] = 2
    wrong_date['start_date']['day'] = 29
    with pytest.raises(ValidationError):
        ScheduleFixedInterval.parse_obj(wrong_date)


def test_schedule_fixed_wrong_date2():
    wrong_date = copy(schedule_fixed_interval)
    wrong_date['start_date']['month'] = 4
    wrong_date['start_date']['day'] = 31
    with pytest.raises(ValidationError):
        ScheduleFixedInterval.parse_obj(wrong_date)
