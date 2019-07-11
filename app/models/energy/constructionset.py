"""Construction Set Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.construction import EnergyConstructionOpaque, EnergyConstructionWindow


class WallSet(BaseModel):
    """A set of constructions for wall assemblies."""

    type: Enum('WallSet', {
               'type': 'WallSet'})


    interior_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

    exterior_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

    ground_construction: EnergyConstructionOpaque = Schema(
        default=None
    )


class FloorSet(BaseModel):
    """A set of constructions for floor assemblies."""

    type: Enum('FloorSet', {
               'type': 'FloorSet'})


    interior_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

    exterior_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

    ground_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

class RoofCeilingSet(BaseModel): 
    """A set of constructions for roof and ceiling assemblies."""

    type: Enum('RoofCeilingSet', {
               'type': 'RoofCeilingSet'})

    interior_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

    exterior_construction: EnergyConstructionOpaque = Schema(
        default=None
    )    

    ground_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

class ApertureSet(BaseModel): 
    """A set of constructions for aperture assemblies."""

    type: Enum('ApertureSet', {
               'type': 'ApertureSet'})

    interior_construction: EnergyConstructionWindow = Schema(
        default=None
    )

    fixed_window_construction: EnergyConstructionWindow = Schema(
        default=None
    )    

    skylight_construction: EnergyConstructionWindow = Schema(
        default=None
    )

    operable_window_construction: EnergyConstructionWindow = Schema(
        default=None
    ) 

    glass_door_construction: EnergyConstructionWindow = Schema(
        default=None
    )

class DoorSet(BaseModel): 
    """A set of constructions for door assemblies."""

    type: Enum('DoorSet', {
               'type': 'DoorSet'})


    interior_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

    exterior_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

    overhead_construction: EnergyConstructionOpaque = Schema(
        default=None
    )

class ConstructionSet(BaseModel):
    """A set of constructions for different surface types and boundary conditions."""


    type: Enum('ConstructionSet', {
               'type': 'ConstructionSet'})


    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )
    
    wall_set: WallSet = Schema(
        default=None
    )

    floor_set: FloorSet = Schema(
        default=None
    )

    roof_ceiling_set: RoofCeilingSet = Schema(
        default=None
    )

    aperture_set: ApertureSet = Schema(
        default=None
    )

    door_set: DoorSet = Schema(
        default=None
    )
    
if __name__ == '__main__':
    print(ConstructionSet.schema_json(indent=2))
