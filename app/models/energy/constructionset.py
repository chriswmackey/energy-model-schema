"""Construction Set Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.construction import OpaqueConstructionAbridged, WindowConstructionAbridged


class WallSetAbridged(BaseModel):
    """A set of constructions for wall assemblies."""

    type: Enum('WallSetAbridged', {
               'type': 'WallSetAbridged'})

    interior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    exterior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    ground_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )


class FloorSetAbridged(BaseModel):
    """A set of constructions for floor assemblies."""

    type: Enum('FloorSetAbridged', {
               'type': 'FloorSetAbridged'})

    interior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    exterior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    ground_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )


class RoofCeilingSetAbridged(BaseModel):
    """A set of constructions for roof and ceiling assemblies."""

    type: Enum('RoofCeilingSetAbridged', {
               'type': 'RoofCeilingSetAbridged'})

    interior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    exterior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    ground_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )


class ApertureSetAbridged(BaseModel):
    """A set of constructions for aperture assemblies."""

    type: Enum('ApertureSetAbridged', {
               'type': 'ApertureSetAbridged'})

    interior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    fixed_window_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    skylight_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    operable_window_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    glass_door_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )


class DoorSetAbridged(BaseModel):
    """A set of constructions for door assemblies."""

    type: Enum('DoorSetAbridged', {
               'type': 'DoorSetAbridged'})

    interior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    exterior_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    overhead_construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )


class ConstructionSetAbridged(BaseModel):
    """A set of constructions for different surface types and boundary conditions."""

    type: Enum('ConstructionSetAbridged', {
               'type': 'ConstructionSetAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    wall_set: WallSetAbridged = Schema(
        default=None
    )

    floor_set: FloorSetAbridged = Schema(
        default=None
    )

    roof_ceiling_set: RoofCeilingSetAbridged = Schema(
        default=None
    )

    aperture_set: ApertureSetAbridged = Schema(
        default=None
    )

    door_set: DoorSetAbridged = Schema(
        default=None
    )


if __name__ == '__main__':
    print(ConstructionSetAbridged.schema_json(indent=2))
