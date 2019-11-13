"""Schedule Base Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
import re

class ScheduleNumericType (str, Enum):
    """Designates how the range values are validated."""
    continuous = 'Continuous'
    discrete = 'Discrete'

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


class ScheduleTypeLimit(BaseModel):
    """Specifies the data types and limits for values contained in schedules."""

    type: Enum('ScheduleTypeLimit', {'type': 'ScheduleTypeLimit'})

    name: str = Schema(
        ...,
        min_length=1,
        max_length=100
    )

    @validator('name')
    def check_name(cls, v):
        try:
            val = ''.join(i for i in v if ord(i) < 128)
            val = re.sub(r'[,;!\n\t]', '', v)
        except  TypeError:
            raise TypeError('Invalid String')
        val = val.strip()

    lower_limit: float = Schema(
        default=None,
        description='Lower limit for the schedule type is entered.'
    )

    upper_limit: float = Schema(
        default=None,
        description='Upper limit for the schedule type is entered.'
    )

    numeric_type: ScheduleNumericType = ScheduleNumericType.continuous

    unit_type: ScheduleUnitType = ScheduleUnitType.dimensionless
