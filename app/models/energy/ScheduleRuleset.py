"""Schedule Ruleset Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


class DateSpecificationType(str, Enum):

    date_range = 'DateRange'
    specific_date = 'SpecificDate'


class ScheduleContinuous(BaseModel):
    """This Numeric Type allows all numbers, including fractional amounts, within the range to
  be valid."""

    schedule_continuous: float = Schema(
        ...,
    )


class ScheduleDiscrete(BaseModel):
    """This Numeric Type allows all only integers within the range to be valid."""

    schedule_discrete: int = Schema(
        ...,
    )


class NumericType (BaseModel):
    """Designates how the range values are validated."""

    numeric_type:  Union[ScheduleContinuous, ScheduleDiscrete]


class UnitType (str, Enum):
    dimensionless: 'Dimensionless'
    temperature: 'Temperature'
    delta_temperature: 'DeltaTemperature'
    precipitation_rate: 'PrecipitationRate'
    angle: 'Angle'
    convection_coefficient: 'ConvectionCoefficient'
    activity_level: 'ActivityLevel'
    velocity: 'Velocity'
    capacity: 'Capacity'
    power: 'Power'
    availability: 'Availability'
    percent: 'Percent'
    control: 'Control'
    mode: 'Mode'


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

    unit_type: UnitType


class YesOrNo (str, Enum):
    no = 'No'
    yes = 'Yes'


class ScheduleDay(BaseModel):
    """Used to describe the daily schedule for a single simulation day."""
    type: Enum('ScheduleDay', {'type': 'ScheduleDay'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    interpolate_to_timestep: YesOrNo = YesOrNo.no

    hour: int = Schema(
        ...,
        ge=0,
        le=23,
    )

    minute: int = Schema(
        ...,
        ge=0,
        le=59
    )

    value_until_time: float = Schema(
        ...
    )


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


class ScheduleRule(BaseModel):
    """A set of rules assigned to schedule ruleset for specific periods of time and for
  particular days of the week according to a priority sequence."""

    type: Enum('ScheduleDay', {'type': 'ScheduleDay'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    schedule_rule_set: ScheduleRuleset

    rule_order: float 

    schedule_day: ScheduleDay

    apply_sunday: YesOrNo = YesOrNo.no

    apply_monday: YesOrNo = YesOrNo.no

    apply_tuesday: YesOrNo = YesOrNo.no

    apply_wednesday: YesOrNo = YesOrNo.no

    apply_thursday: YesOrNo = YesOrNo.no

    apply_friday: YesOrNo = YesOrNo.no

    apply_saturday: YesOrNo = YesOrNo.no

    apply_holiday: YesOrNo = YesOrNo.no

    date_specification_type: DateSpecificationType = DateSpecificationType.date_range

    start_month: int = Schema(
        1,
        ge=1,
        le=12
    )

    start_day: int = Schema(
        1,
        ge=1,
        le=31,
    )

    end_month: int = Schema(
        12,
        ge=1,
        le=12
    )

    end_day: int = Schema(
        31,
        ge=1,
        le=31
    )

    specific_month: int = Schema(
        ...,
        ge=1,
        le=12
    )

    specific_day: int = Schema(
        ...,
        ge=1,
        le=31
    )


print(ScheduleRule.schema_json(indent=2))
