"""Schedule Ruleset Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
#from app.models.energy.ScheduleBase import UnitType, DateTime

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
        ' `False`.'
    )


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



class ScheduleContinuous(BaseModel):
    """This Numeric Type allows all numbers, including fractional amounts, within the range to
  be valid."""

    type: Enum('ScheduleContinuous', {'type': 'ScheduleContinuous'})

    schedule_continuous: float = None


class ScheduleDiscrete(BaseModel):
    """This Numeric Type allows all only integers within the range to be valid."""

    type: Enum('ScheduleDiscrete', {'type': 'ScheduleDiscrete'})


    schedule_discrete: int = None


class NumericType (BaseModel):
    """Designates how the range values are validated."""

    numerictype:  Union[ScheduleContinuous, ScheduleDiscrete] #Should be oneOf 


class ScheduleTypeLimits (BaseModel):
    """Specifies the data types and limits for values contained in schedules."""

    type: Enum('ScheduleTypeLimits', {'type': 'ScheduleTypeLimits'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    lower_limit_value: float = Schema(
        0,
        description='Lower limit for the schedule type is entered.'
    )

    upper_limit_value: float = Schema(
        1,
        description='Upper limit for the schedule type is entered.'
    )

    numeric_type: NumericType

    unit_type: UnitType


    #@validator('lower_limit_value')
    #def check_lower_limit(lower_limit_value, upper_limit_value):
    #    if upper_limit_value < lower_limit_value:
    #        raise 'Upper Limit should be greater than the lower limit.'

    #@validator('unit_type')
    #def check_unit_type(unit_type, numeric_type):
    #    if unit_type == 'Dimensionless':
    #        numeric_type = NumericType.ScheduleContinuous
    #    else:
    #        raise 'Incorrect %(numeric_type) for %(unit_type).' 


class YesOrNo (str, Enum):
    no = 'No'
    yes = 'Yes'


class ScheduleDay(BaseModel):
    """Used to describe the daily schedule for a single simulation day."""
    type: Enum('ScheduleDay', {'type': 'ScheduleDay'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    interpolate_to_timestep: YesOrNo = YesOrNo.no

    hour: int = Schema(
        ...,
        ge=0,
        le=23,
    )

    minute: int = Schema(
        ...,
        ge=0,
        le=59
    )

    value_until_time: float = Schema(
        ...
    )


class ScheduleRule(BaseModel):
    """A set of rules assigned to schedule ruleset for specific periods of time and for
  particular days of the week according to a priority sequence."""

    type: Enum('ScheduleRule', {'type': 'ScheduleRule'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    schedule_day: List[ScheduleDay]

    apply_sunday: YesOrNo = YesOrNo.no

    apply_monday: YesOrNo = YesOrNo.no

    apply_tuesday: YesOrNo = YesOrNo.no

    apply_wednesday: YesOrNo = YesOrNo.no

    apply_thursday: YesOrNo = YesOrNo.no

    apply_friday: YesOrNo = YesOrNo.no

    apply_saturday: YesOrNo = YesOrNo.no

    apply_holiday: YesOrNo = YesOrNo.no

    start_period: DateTime

    end_period: DateTime


class ScheduleRuleset (BaseModel):
    """Used to define a schedule for a default day, further described by ScheduleRule."""

    type: Enum('ScheduleRuleset', {'type': 'ScheduleRuleset'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    schedule_type_limits: ScheduleTypeLimits

    default_day_schedule: List[ScheduleDay]

    summer_designday_schedule: List[ScheduleDay]

    winter_designday_schedule: List[ScheduleDay]

    schedule_rule: List[ScheduleRule]

if __name__== '__main__': 
    print(ScheduleRuleset.schema_json(indent=2))
