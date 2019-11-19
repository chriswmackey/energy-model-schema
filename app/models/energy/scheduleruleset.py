"""Schedule Ruleset Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.schedulebase import ScheduleTypeLimit
from app.models.common.datetime import Date, Time


class ScheduleDay(BaseModel):
    """Used to describe the daily schedule for a single simulation day."""
    type: Enum('ScheduleDay', {'type': 'ScheduleDay'})

    name: str = Schema(
        ...,
        min_length=1,
        max_length=100
    )

    @validator('name')
    def check_name(cls, v):
        assert all(ord(i) < 128 for i in v), 'Name contains non ASCII characters.'
        assert all(char not in v for char in (',',';','!','\n','\t')), \
            'Name contains invalid character for EnergyPlus (, ; ! \n \t).'
        assert len(v) > 0, 'Name is an empty string.'
        assert len(v) <=100, 'Number of characters must be less than 100.'

    values: List[float]

    times: List[List[float]]

    @validator('times', whole=True)
    def check_len_times(cls, v):
        for i in v:
            if len(i) != 2:
                raise ValueError(
                    'Incorrect number of values.'
                )

    interpolate: bool = Schema(
        False
    )


class ScheduleRule(BaseModel):
    """A set of rules assigned to schedule ruleset for specific periods of time and for
  particular days of the week according to a priority sequence."""

    type: Enum('ScheduleRule', {'type': 'ScheduleRule'})

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

    start_date: List[float] = Schema(
        [1, 1]
    )

    @validator('start_date', whole=True)
    def check_len_start_date(cls, v):
        if len(v) != 2:
            raise ValueError(
                'Incorrect number of values.'
            )

    end_date: List[float] = Schema(
        [12, 31]
    )

    @validator('end_date', whole=True)
    def check_len_end_date(cls, v):
        if len(v) != 2:
            raise ValueError(
                'Incorrect number of values.'
            )


class ScheduleRulesetAbridged(BaseModel):
    """Used to define a schedule for a default day, further described by ScheduleRule."""

    type: Enum('ScheduleRulesetAbridged', {'type': 'ScheduleRulesetAbridged'})

    name: str = Schema(
        ...,
        min_length=1,
        max_length=100
    )

    @validator('name')
    def check_name(cls, v):
        assert all(ord(i) < 128 for i in v), 'Name contains non ASCII characters.'
        assert all(char not in v for char in (',',';','!','\n','\t')), \
            'Name contains invalid character for EnergyPlus (, ; ! \n \t).'
        assert len(v) > 0, 'Name is an empty string.'
        assert len(v) <=100, 'Number of characters must be less than 100.'

    schedule_type_limit: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    default_day_schedule: ScheduleDay

    schedule_rules: List[ScheduleRule] = Schema(
        default=None
    )

    summer_designday_schedule: ScheduleDay = Schema(
        default=None
    )

    winter_designday_schedule: ScheduleDay = Schema(
        default=None
    )


if __name__ == '__main__':
    print(ScheduleRulesetAbridged.schema_json(indent=2))
