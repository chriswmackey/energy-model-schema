"""Schedule Base Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


class UnitType (str, Enum):
    dimensionless = 'Dimensionless'
    temperature = 'Temperature'
    delta_temperature = 'DeltaTemperature'
    precipitation_rate = 'PrecipitationRate'
    angle = 'Angle'
    convection_coefficient = 'ConvectionCoefficient'
    activity_level = 'ActivityLevel'
    velocity =  'Velocity'
    capacity =  'Capacity'
    power =  'Power'
    availability =  'Availability'
    percent = 'Percent'
    control = 'Control'
    mode = 'Mode'

class DateTime(BaseModel):
    """DateTime."""

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
    
    hour: int = Schema(
        0,
        description='A value for hour between `0`-`23`. Default is `0`.',
        ge=0,
        le=23,
    )
    
    minute: int = Schema(
        0,
        description='A value for month between `0`-`59`. Default is `0`.',
        ge=0,
        le=59,
    )
    
    is_leap_year: bool = Schema(
        False,
        description='A boolean to indicate if datetime is for a leap year. Default is'
        ' `false`.'
    )
