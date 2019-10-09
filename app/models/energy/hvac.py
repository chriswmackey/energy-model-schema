"""HVAC Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


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

    cooling_limit: Union[float, str] = Schema(
        'autocalculate',
        ge=0
    )

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
