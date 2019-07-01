"""Schedule Fixed Interval Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
import datetime
from app.models.energy.ScheduleBase import ScheduleContinuous, ScheduleDiscrete, ScheduleNumericType, ScheduleUnitType, Date, Time


class ScheduleFixedInterval(BaseModel):
    """Used to specify a start date and a list of values for a period of analysis."""

    type: Enum('ScheduleFixedInterval', {'type': 'ScheduleFixedInterval'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    start_date: Date


    is_leap_year: bool = Schema(
        False,
        description='A boolean to indicate if datetime is for a leap year. Default is'
        ' `false`.'
    )

    values: List[int] = Schema(
        ...,
        minItems=24,
        maxItems=8784,
        description='A list of hourly values for the simulation.'
    )


    @validator('values', whole=True)
    def check_min_items(cls, v, values):
        "Ensure the number of values are not less than 24."
        if len(v) < 24:
            raise ValidationError(
                'Number of values must be atleast 24.'
            )
        return v

    @validator('values', whole=True)
    def check_max_items(cls, v, values): 
        if 'is_leap_year' == 'True' and len(v) > 8784:
            raise ValidationError('Number of values for leap year can not be more than `8784`.') 
        elif 'is_leap_year' == 'False' and len(v) > 8760:
            raise ValidationError('Number of values for a year can not be more than `8760`.')
        return v

    #@validator('is_leap_year')
    #def check_leap_year(cls, v, values):
    #    if v == False and values['start_date'].month == 2 and values['start_date'].day == 29:
    #        raise ValidationError('A non leap year can not have `2`/`29` as the start date.')
    #    return v

if __name__ == '__main__':
    print(ScheduleFixedInterval.schema_json(indent=2))
