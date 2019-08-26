"""Schedule Fixed Interval Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
import datetime
from app.models.energy.schedulebase import ScheduleType
from app.models.common.datetime import Date


class ScheduleFixedInterval(BaseModel):
    """Used to specify a start date and a list of values for a period of analysis."""

    type: Enum('ScheduleFixedInterval', {'type': 'ScheduleFixedInterval'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    schedule_type: ScheduleType = Schema(
        default=None
    )

    interpolate_to_timestep: bool = Schema(
        False
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
        "Ensure correct number of values."
        if not 'start_date' in values:
            return v
        if values['start_date'].is_leap_year == False and len(v) < 24 or len(v) > 8760:
            raise ValueError(
                'Number of values can not be lesser than 24 or greater than 8760 for non-leap year')
        elif values['start_date'].is_leap_year == True and len(v) < 24 or len(v) > 8784:
            raise ValueError(
                'Number of values can not be lesser than 24 or greater than 8784 for leap year')
        return v


if __name__ == '__main__':
    print(ScheduleFixedInterval.schema_json(indent=2))
