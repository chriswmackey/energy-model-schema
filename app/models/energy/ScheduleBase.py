"""Schedule Base Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


class ScheduleContinuous(BaseModel):
    """This Numeric Type allows all numbers, including fractional amounts, within the range to
  be valid."""

    type: Enum('ScheduleContinuous', {'type': 'ScheduleContinuous'})

    schedule_continuous: float = None


class ScheduleDiscrete(BaseModel):
    """This Numeric Type allows all only integers within the range to be valid."""

    type: Enum('ScheduleDiscrete', {'type': 'ScheduleDiscrete'})

    schedule_discrete: int = None

class ScheduleNumericType (BaseModel):
    """Designates how the range values are validated."""

    numeric_type:  Union[ScheduleContinuous, ScheduleDiscrete]


class ScheduleUnitType (str, Enum):
    dimensionless = 'Dimensionless'
    temperature = 'Temperature'
    delta_temperature = 'DeltaTemperature'
    precipitation_rate = 'PrecipitationRate'
    angle = 'Angle'
    convection_coefficient = 'ConvectionCoefficient'
    activity_level = 'ActivityLevel'
    velocity = 'Velocity'
    capacity = 'Capacity'
    power = 'Power'
    availability = 'Availability'
    percent = 'Percent'
    control = 'Control'
    mode = 'Mode'


class Date(BaseModel):
    """Date."""

    month: int = Schema(
        1,
        description='A value for month between `1`-`12`. Default is `1`.',
        ge=1,
        le=12
    )

    day: int = Schema(
        1,
        description='A value for day between `1`-`31`. Default is `1`.',
        ge=1,
        le=31
    )


class Time(BaseModel):
    """Time."""

    hour: int = Schema(
        0,
        description='A value for hour between `0`-`24`. Default is `0`.',
        ge=0,
        le=24,
    )

    minute: int = Schema(
        0,
        description='A value for month between `0`-`60`. Default is `0`.',
        ge=0,
        le=60,
    )


class DateTime(BaseModel):
    """DateTime."""

    date: Date

    time: Time

    is_leap_year: bool = Schema(
        False,
        description='A boolean to indicate if datetime is for a leap year. Default is'
        ' `false`.'
    )





