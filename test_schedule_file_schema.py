"""Schedule Fixed Interval Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
import datetime
from app.models.common.datetime import Date


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

    is_leap_year: bool = Schema(
        False,
        description='A boolean to indicate if datetime is for a leap year. Default is'
        ' `false`.'
    )

    @validator('day')
    def check_date(cls, v, values):
        try:
            datetime.date(2016, values['month'], v)
        except ValidationError:
            raise ValidationError(
                '{}/{} is not a valid date.'.format(values['month'], v))
        else:
            return v

    @validator('is_leap_year')
    def check_leap_year(cls, v, values):
        if values['month'] == 2 and values['day'] == 29 and v == False:
            raise ValidationError( '`2`/`29` is not a valid date for a non leap year.')
        return v



class schedulefixedinterval(BaseModel):
    """Used to specify a start date and a list of values for a period of analysis."""

    type: Enum('schedulefixedinterval', {'type': 'schedulefixedinterval'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    start_date: Date

    values: List[int] = Schema(
        ...,
        minItems=24,
        maxItems=8784,
        description='A list of hourly values for the simulation.'
    )

    @validator('values', whole=True)
    def check_range(cls, v, values):
        "Ensure the number of values are not less than 24."
        if values['start_date'].is_leap_year == False:
            len(v) <= 8760
        else:
            raise ValueError('Number of values can not be greater than 8760 for non-leap year')
        return v

if __name__ == '__main__':
    print(schedulefixedinterval.schema_json(indent=2))
