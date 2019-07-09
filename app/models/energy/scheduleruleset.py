"""Schedule Ruleset Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.schedulebase import ScheduleNumericType, ScheduleUnitType
from app.models.common.datetime import Date, Time


class ScheduleTypeLimits(BaseModel):
    """Specifies the data types and limits for values contained in schedules."""

    type: Enum('ScheduleTypeLimits', {'type': 'ScheduleTypeLimits'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    lower_limit_value: float = Schema(
        0,
        description='Lower limit for the schedule type is entered.'
    )

    upper_limit_value: float = Schema(
        1,
        description='Upper limit for the schedule type is entered.'
    )

    numeric_type: ScheduleNumericType

    unit_type: ScheduleUnitType


class DayValue(BaseModel):
    """Values for daily schedule"""

    time: Time

    value_until_time: float


class ScheduleDay(BaseModel):
    """Used to describe the daily schedule for a single simulation day."""
    type: Enum('ScheduleDay', {'type': 'ScheduleDay'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    interpolate_to_timestep: bool = Schema(
        False
    )

    day_values: List[DayValue]


class ScheduleRule(BaseModel):
    """A set of rules assigned to schedule ruleset for specific periods of time and for
  particular days of the week according to a priority sequence."""

    type: Enum('ScheduleRule', {'type': 'ScheduleRule'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    schedule_day: ScheduleDay

    apply_sunday: bool = Schema(
        False
    )

    apply_monday: bool = Schema(
        False
    )

    apply_tuesday: bool = Schema(
        False
    )

    apply_wednesday: bool = Schema(
        False
    )

    apply_thursday: bool = Schema(
        False
    )

    apply_friday: bool = Schema(
        False
    )

    apply_saturday: bool = Schema(
        False
    )

    apply_holiday: bool = Schema(
        False
    )

    start_period: Date

    end_period: Date


class ScheduleRuleset(BaseModel):
    """Used to define a schedule for a default day, further described by ScheduleRule."""

    type: Enum('scheduleruleset', {'type': 'scheduleruleset'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    schedule_type_limits: ScheduleTypeLimits

    default_day_schedule: ScheduleDay

    summer_designday_schedule: ScheduleDay

    winter_designday_schedule: ScheduleDay

    schedule_rules: List[ScheduleRule]


if __name__ == '__main__':
    print(ScheduleRuleset.schema_json(indent=2))
