"""Programtype Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError
from typing import List, Union, Optional
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.scheduleruleset import ScheduleRuleset
from app.models.energy.schedulefixedinterval import ScheduleFixedInterval


class PeopleAbridged(BaseModel):
    """Used to model the occupant's effect on the space conditions."""

    type: Enum('PeopleAbridged', {'type': 'PeopleAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    people_per_area: float = Schema(
        ...,
        ge=0,
        description='People per floor area expressed as people/m²'
    )

    radiant_fraction: float = Schema(
        0.3,
        ge=0,
        le=1,
        description='The radiant fraction of sensible heat released by people. The default'
        'value is 0.30.'
    )

    latent_fraction: Union[float, str] = Schema(
        'autocalculate',
        ge=0,
        le=1,
        description='Used to specify a fixed latent fraction of heat gain due to people.'
    )

    occupancy_schedule: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100,
        description='Used to describe the occupancy schedule for people.'
    )

    activity_schedule: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100,
        description='Schedule that determines the amount of heat gain per person.'
    )


class LightingAbridged(BaseModel):
    """Used to specify the information about the electric lighting system."""

    type: Enum('LightingAbridged', {'type': 'LightingAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    watts_per_area: float = Schema(
        ...,
        ge=0,
        description='Lighting per floor area expressed as watts/m².'
    )

    visible_fraction: float = Schema(
        0.25,
        ge=0,
        le=1,
        description='The fraction of heat from lights that goes into the zone as visible '
        '(short-wave) radiation. The default value is `0.25`.'
    )

    radiant_fraction: float = Schema(
        0.32,
        ge=0,
        le=1,
        description='The fraction of heat from lights that is long-wave radiation. Default'
        ' value is `0.32`.'
    )

    return_air_fraction: float = Schema(
        0.00,
        ge=0,
        le=1,
        description='The fraction of the heat from lights that goes into the zone return '
        'air. Default value is `0`.'
    )

    @validator('return_air_fraction')
    def check_sum(cls, v, values): 
        "Ensure sum is less than 1."
        if sum(values['visible_fraction'], values['radiant_fraction'], values['return_air_fraction']) > 1:
            raise ValueError(
        'Sum cannot be greater than 1.')

    schedule: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100,
        description='Used to describe the schedule for lighting as a fraction applied to '
        'design level of lights.'
    )


class ElectricalEquipmentAbridged(BaseModel):
    """Used to specify information about the electrical equipment."""

    type: Enum('ElectricalEquipmentAbridged', {'type': 'ElectricalEquipmentAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    watts_per_area: float = Schema(
        ...,
        ge=0,
        description='Equipment level per floor area expressed as watts/m².'
    )

    radiant_fraction: float = Schema(
        0,
        ge=0,
        le=1,
        description='Used to characterise the amount of long-wave radiation heat given off'
        ' by electric equipment.'
    )

    latent_fraction: Union[float, str] = Schema(
        'autocalculate',
        ge=0,
        le=1,
        description='Used to characterise the amount of latent heat given off by electric' 
        'equipment.'

    )

    lost_fraction: float = Schema(
        0,
        ge = 0,
        le = 1,
        description='Used to characterize the amount of “lost” heat being given off by '
        'equipment. The default value is 0.'
    )


    schedule: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100,
        description='Used to describe the schedule for equipment as a fraction applied to'
        ' design level for electric equipment.'
    )


class GasEquipmentAbridged(BaseModel):
    """Used to specify information about the gas equipment."""

    type: Enum('GasEquipmentAbridged', {'type': 'GasEquipmentAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    watts_per_area: float = Schema(
        ...,
        ge=0,
        description='Equipment level per floor area expressed as watts/m².'
    )

    radiant_fraction: float = Schema(
        0,
        ge=0,
        le=1,
        description='Used to characterise the amount of long-wave radiation heat given off'
        ' by electric equipment.'
    )

    latent_fraction: Union[float, str] = Schema(
        'autocalculate',
        ge=0,
        le=1,
        description='Used to characterise the amount of latent heat given off by electric' 
        'equipment.'

    )

    lost_fraction: float = Schema(
        0,
        ge = 0,
        le = 1,
        description='Used to characterize the amount of “lost” heat being given off by '
        'equipment. The default value is 0.'
    )    

    schedule: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100,
        description='Used to describe the schedule for equipment as a fraction applied to'
        ' design level for electric equipment.'
    )


class InfiltrationAbridged(BaseModel):
    """Used to model the infiltration of air from the outdoor environment into a thermal zone."""

    type: Enum('Infiltration', {'type': 'Infiltration'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    flow_per_exterior_area: float = Schema(
        ...,
        ge=0,
        description='Used to model the infiltration per exterior surface area in m3/s-m2.'
    )

    constant_coefficient: float = Schema(
        1,
        ge=0
    )

    temperature_coefficient: float = Schema(
        0,
        ge=0
    )

    velocity_coefficient: float = Schema(
        0,
        ge=0
    )

    schedule: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100,
        description='Used to describe the schedule for equipment as a fraction applied to'
        ' design level for electric equipment.'
    )


class Ventilation(BaseModel):
    """Used to model the purposeful flow of air from the outdoor environment directly into a thermal zone."""

    type: Enum('Ventilation')

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    air_changes_per_hour: float = Schema(
        ...
    )

    flow_per_zone: float = Schema(
        ...,
        description='Unit is m3/s-m2.'
    )

    flow_per_person: float = Schema(
        None,
        ge=0,
        description='Used to model the ventilation flow rate per person in m3/s-person.'
    )

    flow_per_area: float = Schema(
        None,
        ge=0,
        description='Used to model the ventilation flow rate per zone floor area in m3/s-m2.'
    )

    schedule: Optional[]

class Setpoint(BaseModel):
    """Used to specify information about the setpoint schedule."""

    cooling_schedule: ScheduleFixedInterval

    heating_schedule: ScheduleFixedInterval

    humidification_schedule: ScheduleFixedInterval

    dehumidification_schedule: ScheduleFixedInterval


class ProgramType(BaseModel):
    """A set of programs."""

    type: Enum('ProgramType', {'type': 'ProgramType'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    people: People

    lighting: Lighting

    electrical_equipment: ElectricalEquipment

    gas_equipment: GasEquipment

    setpoint: Setpoint

if __name__ == '__main__':
    print(ProgramType.schema_json(indent=2))