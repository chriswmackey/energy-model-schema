"""Schedule Base Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
import datetime

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
    @validator('day')
    def check_date(cls, v, values):
        try:
            datetime.date(2016, values['month'], v)
        except ValidationError:
            raise ValidationError('{}/{} is not a valid date.'.format(values['month'], v))
        else: 
            return v

class Time(BaseModel):
    """Time."""

    hour: int = Schema(
        0,
        description='A value for hour between `0`-`24`. Default is `0`.',
        ge=0,
        le=24
    )

    minute: int = Schema(
        0,
        description='A value for minutes between `0`-`59`. Default is `0`.',
        ge=0,
        le=59
    )

    @validator('minute')
    def check_time(cls, v, values):
        try: 
            datetime.time(v, values['hour'], 0)
        except ValidationError:
            raise ValidationError('{}/{} is not a valid time.'.format(values['hour'], v))
        else:
            return v

    @validator('minute')
    def check_time_after24(cls, v, values):
        if values['hour']==24 and v > 0:
            raise ValidationError('{}/{} is not a valid time.'.format(values['hour'], v))
        return v     

class ScheduleContinuous(BaseModel):
    """This Numeric Type allows all numbers, including fractional amounts, within the range to
  be valid."""

    type: Enum('ScheduleContinuous', {'type': 'ScheduleContinuous'})

    schedule_continuous: float = None


class ScheduleDiscrete(BaseModel):
    """This Numeric Type allows only integers within the range to be valid."""

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
