"""Schedule Ruleset Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.ScheduleBase import ScheduleUnitType, DateTime, Date, Time, YesOrNo


class ScheduleContinuous(BaseModel):
    """This Numeric Type allows all numbers, including fractional amounts, within the range to
  be valid."""

    type: Enum('ScheduleContinuous', {'type': 'ScheduleContinuous'})

    schedule_continuous: float = None


class ScheduleDiscrete(BaseModel):
    """This Numeric Type allows all only integers within the range to be valid."""

    type: Enum('ScheduleDiscrete', {'type': 'ScheduleDiscrete'})


    schedule_discrete: int = None


class NumericType (BaseModel):
    """Designates how the range values are validated."""

    numerictype:  Union[ScheduleContinuous, ScheduleDiscrete] #Should be oneOf 


class ScheduleTypeLimits (BaseModel):
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

    numeric_type: NumericType

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

    interpolate_to_timestep: YesOrNo = YesOrNo.no

    day_values = List[DayValue]
    

class ScheduleRule(BaseModel):
    """A set of rules assigned to schedule ruleset for specific periods of time and for
  particular days of the week according to a priority sequence."""

    type: Enum('ScheduleRule', {'type': 'ScheduleRule'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    schedule_day: ScheduleDay

    apply_sunday: YesOrNo = YesOrNo.no

    apply_monday: YesOrNo = YesOrNo.no

    apply_tuesday: YesOrNo = YesOrNo.no

    apply_wednesday: YesOrNo = YesOrNo.no

    apply_thursday: YesOrNo = YesOrNo.no

    apply_friday: YesOrNo = YesOrNo.no

    apply_saturday: YesOrNo = YesOrNo.no

    apply_holiday: YesOrNo = YesOrNo.no

    start_period: DateTime

    end_period: DateTime




class ScheduleRuleset (BaseModel):
    """Used to define a schedule for a default day, further described by ScheduleRule."""

    type: Enum('ScheduleRuleset', {'type': 'ScheduleRuleset'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    schedule_type_limits: ScheduleTypeLimits

    default_day_schedule: ScheduleDay

    summer_designday_schedule: ScheduleDay

    winter_designday_schedule: ScheduleDay

    schedule_rules: List[ScheduleRule]

if __name__== '__main__': 
    print(ScheduleRuleset.schema_json(indent=2))
