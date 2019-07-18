"""Construction Abridged Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError, constr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


class EnergyConstructionWindowAbridged(BaseModel):
    """
    Group of objects to describe the physical properties and configuration for
    the building envelope and interior elements that is the windows of the building.
    """
    type: Enum('EnergyConstructionWindowAbridged', {
               'type': 'EnergyConstructionWindowAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    layers: List[constr(regex=r'^[\s.A-Za-z0-9_-]*$', min_length=1, max_length=100)] = Schema(
        ...,
        description='List of materials. The order of the materials is from outside to'
        ' inside.',
        minItems=1,
        maxItems=8
    )

    @validator('layers', whole=True)
    def check_num_items(cls, layers):
        "Ensure length of material is at least 1 and not more than 8."
        if len(layers) == 0:
            raise ValidationError(
                'Window construction should at least have one material.'
            )

        elif len(layers) > 8:
            raise ValidationError(
                'Window construction cannot have more than 8 materials.'
            )
        else:
            return layers


class EnergyConstructionOpaqueAbridged(BaseModel):
    """
    Group of objects to describe the physical properties and configuration for
    the building envelope and interior elements that is the walls, roofs, floors,
    and doors of the building.
    """
    type: Enum('EnergyConstructionOpaqueAbridged', {
               'type': 'EnergyConstructionOpaqueAbridged'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    layers: List[constr(regex=r'^[\s.A-Za-z0-9_-]*$', min_length=1, max_length=100)] = Schema(
        ...,
        description='List of materials. The order of the materials is from outside to'
        ' inside.',
        minItems=1,
        maxItems=10
    )

    @validator('layers', whole=True)
    def check_num_items(cls, layers):
        "Ensure length of material is at least 1 and not more than 10."
        if len(layers) == 0:
            raise ValidationError(
                'Opaque construction should at least have one material.'
            )
        elif len(layers) > 10:
            raise ValidationError(
                'Opaque construction cannot have more than 10 materials.'
            )
        else:
            return layers


if __name__ == '__main__':
    print(EnergyConstructionWindowAbridged.schema_json(indent=2))

if __name__ == '__main__':
    print(EnergyConstructionOpaqueAbridged.schema_json(indent=2))
