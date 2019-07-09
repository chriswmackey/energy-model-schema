"""Programset Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.energy.scheduleruleset import ScheduleRuleset
from app.energy.schedulefixedinterval import ScheduleFixedInterval


class People(BaseModel):
    """Used to model the occupant's effect on the space conditions."""

    type: Enum('People', {'type': 'People'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    people_per_area: float = Schema(
        ...,
        ge=0,
        description='People per floor area expressed as people/m^2'
    )

    radiant_fraction: float = Schema(
        0.3,
        ge=0,
        le=1,
        description='The radiant fraction of sensible heat released by people. The default value is 0.30.'
    )

    latent_fraction: float = Schema(
        ...,
        ge=0,
        le=1,
        description='Used to specify a fixed latent fraction of heat gain due to people.'
    )

    occupancy_schedule: Union[ScheduleRuleset, ScheduleFixedInterval] = Schema(
        ...,
        description='Used to describe the occupancy schedule for people.'
    )

    activity_schedule: Union[ScheduleRuleset, ScheduleFixedInterval] = Schema(
        ...,
        description='Schedule that determines the amount of heat gain per person.'
    )


class Lighting(BaseModel):
    """Used to specify the information about the electric lighting system."""

    type: Enum('Lighting', {'type': 'Lighting'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    lighting_per_area: float = Schema(
        ...,
        ge=0,
        description='Lighting per floor area expressed as watts/m^2.'
    )

    radiant_fraction: float = Schema(
        0,
        ge=0,
        le=1,
        description='The fraction of heat from lights that is long-wave radiation. Default value is `0`.'
    )

    schedule: Union[ScheduleRuleset, ScheduleFixedInterval] = Schema(
        ...,
        description='Used to describe the schedule for lighting as a fraction applied to design level of lights.'
    )
