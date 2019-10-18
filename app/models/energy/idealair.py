"""Ideal Air Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError
from typing import List, Union
from enum import Enum

class EconomizerType(str, Enum):
    no_economizer = 'NoEconomizer'
    differential_dry_bulb = 'DifferentialDryBulb'
    differential_enthalpy = 'DifferentialEnthalpy'


class IdealAirSystem(BaseModel):
    """ Provides a model for an ideal HVAC system."""
    type: Enum('IdealAirSystem', {'type': 'IdealAirSystem'})

    heating_limit: Union[float, str] = Schema(
        'autocalculate',
        ge=0
    )

    @validator('heating_limit')
    def check_string_heating_limit(cls, v):
        "Ensure the text input is nothing other than autocalculate."
        if v != 'autocalculate':
            raise ValueError( 'This is not a valid entry for heating_limit')

    cooling_limit: Union[float, str] = Schema(
        'autocalculate',
        ge=0
    )

    @validator('cooling_limit')
    def check_string_cooling_limit(cls, v):
        "Ensure the text input is nothing other than autocalculate."
        if v != "autocalculate":
            raise ValueError( 'This is not a valid entry for heating_limit')

    economizer_type: EconomizerType = EconomizerType.differential_dry_bulb

    demand_control_ventilation: bool = Schema(
        False
    )

    sensible_heat_recovery: float = Schema(
        0,
        ge=0,
        le=1
    )

    latent_heat_recovery: float = Schema(
        0,
        ge=0,
        le=1
    )