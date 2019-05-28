"""Schedule File Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


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


class ScheduleFile(BaseModel):
    """A list of values used to create a .csv file for the entire year or a period of
  analysis within the year."""

    type: Enum('ScheduleFile', {'type': 'ScheduleFile'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    start_day_of_year: int = Schema(
        ...,
        ge=1,
        le=366,
        description='Used to define the start day for the analysis period.'
    )

    values: List[int] = Schema(
        ...,
        le=8784,
        description='A list of hourly values for the simulation.'
    )

    units: UnitType = Schema(
        'Dimensionless',
        description='Units for the hourly values for simulation. The default value is'
         'Dimensionless for a fractional schedule.'
    )

print(ScheduleFile.schema_json(indent=2))