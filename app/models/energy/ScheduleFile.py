"""Schedule File Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.ScheduleBase import ScheduleUnitType


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
        minItems=24,
        maxItems=8784,
        description='A list of hourly values for the simulation.'
    )

    @validator('values', whole=True)
    def check_num_items(cls, values):
        "Ensure the number of values are not less than 24 and greater than 8784."
        if len(values)<24:
            raise ValidationError(
                'Number of values must be atleast 24.'
            )
        elif len(values)>8784:
            raise ValidationError(
                'Number of values should not be greater than 8784.'
            )
        return values
    

    units: ScheduleUnitType = Schema(
        'Dimensionless',
        description='Units for the hourly values for simulation. The default value is'
         'Dimensionless for a fractional schedule.'
    )

if __name__ == '__main__':
    print(ScheduleFile.schema_json(indent=2))
    