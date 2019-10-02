"""Schedule Base Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4


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
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

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
