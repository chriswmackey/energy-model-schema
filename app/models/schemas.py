"""Model schemas."""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from .energy.Construction import EnergyConstructionOpaque, EnergyConstructionTransparent
from .energy.ScheduleRuleset import DateTime, UnitType, ScheduleContinuous, ScheduleDiscrete, NumericType, ScheduleTypeLimits, YesOrNo, ScheduleDay, ScheduleRule, ScheduleRuleset
from .energy.ScheduleFile import ScheduleFile
from .energy.ScheduleBase import UnitType, DateTime

class FaceType(str, Enum):
    wall = 'Wall'
    roof_ceiling = 'RoofCeiling'
    floor = 'Floor'
    air_wall = 'AirWall'
    shading = 'Shading'


class Parent(BaseModel):
    """Parent zone information"""
    id: UUID = Schema(default=None, description="Unique UUID value.")

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    schedule_ruleset: ScheduleRuleset = Schema(
        default=None,
        description='Schedule Ruleset for zone for energy simulation.'
    )

    schedule_file: ScheduleFile = Schema(
        default=None,
        description='Schedule File for zone for energy simulation'
    )


class Opaque(BaseModel):
    """Opaque Material Schema"""
    type: Enum('Opaque', {'type': 'Opaque'})

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    reflectance:  float = Schema(
        ...,
        ge=0,
        le=1
    )


class Transparent(BaseModel):
    """Transparent Material Schema"""
    type: Enum('Transparent', {'type': 'Transparent'})

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'

    )

    transmittance:  float = Schema(
        ...,
        ge=0,
        le=1
    )


class Plastic(BaseModel):
    """Plastic Material Schema"""
    type: Enum('Plastic', {'type': 'Plastic'})

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    r_reflectance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    g_reflectance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    b_reflectance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    specularity:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    roughness:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    modifier:  str = 'void'


class Glass(BaseModel):
    """Glass Material Schema"""
    type: Enum('Glass', {'type': 'Glass'})

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    r_transmittance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    g_transmittance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    b_transmittance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    refraction_index:  float = Schema(
        ...,
        ge=0,
        le=5
    )

    modifier:  str = 'void'


class Vertex(BaseModel):
    """Individual Vertex Schema"""
    x: float = Schema(..., description='X coordinate of the vertex')
    y: float = Schema(..., description='y coordinate of the vertex')
    z: float = Schema(..., description='z coordinate of the vertex')


class FaceBase(BaseModel):
    """The Base Face model"""

    id: UUID = Schema(default=None, description="Unique UUID value.")

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    vertices: List[Vertex] = Schema(
        ...,
        minItems=3
    )

    @validator('vertices', whole=True)
    def check_min_items(cls, v):
        assert len(v) >= 3, \
            'Number of face vertices must be 3 or more. Vertices count: %d.' % len(
                v)

    # TODO: write type assignment based on face normal direction as default value function
    face_type: FaceType = FaceType.wall

    rad_modifier: Union[Opaque, Transparent, Plastic, Glass] = Schema(
        default=None,
        description='Radiance material.'
    )

    rad_modifier_dir: Union[Opaque, Transparent, Plastic, Glass] = Schema(
        default=None,
        description='Radiance material for direct sunlight simulation.'
    )

    energy_construction_opaque: EnergyConstructionOpaque = Schema(
        default=None,
        description='Face opaque construction for energy simulation.'
    )

    energy_construction_transparent: EnergyConstructionTransparent = Schema(
        default=None,
        description='Face transparent construction for energy simulation'
    )

class ShadeFace(FaceBase):
    """ShadeFace Schema"""
    type: Enum('ShadeFace', {'type': 'ShadeFace'})

    face_type: Enum('Shading', {'face_type': 'Shading'})


class Aperture(FaceBase):
    """Aperture Schema"""
    type: Enum('Aperture', {'type': 'Aperture'})

    face_type: Enum('Window', {'face_type': 'Window'})

    rad_modifier: Union[Transparent, Glass] = None

    blinds: List[ShadeFace] = []


class Face(FaceBase):
    """A single model face.

    Some clever description
    """
    type: Enum('Face', {'type': 'Face'})

    apertures: List[Aperture] = Schema(
        default=[],
        description='List of Apertures bound to the Face'
    )

    parent: Parent = None


class Model(BaseModel):
    """Face by Face Model Schema"""
    type: Enum('Model', {'type': 'Model'})

    name: str = Schema(
        ...,
        description='Model name',
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    convert_to_meters: float = Schema(
        default=1,
        description='Value to use to convert the current model into meters'
    )

    faces: List[Union[Face, ShadeFace]] = Schema(
        default=[],
        description='List of model faces, can be of type Face or ShadeFace'
    )


class ModelOut(BaseModel):
    """Face by Face Model Schema Out"""
    type: Enum('Model', {'type': 'Model'})

    id: UUID = Schema(default=None, description="Unique UUID value.")

    name: str = Schema(
        ...,
        description='Model name',
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    convert_to_meters: float = Schema(
        default=1,
        description='Value to use to convert the current model into meters'
    )

    face_count: int = Schema(
        ...,
        description="Number of faces attached to this model"
    )

    created_at: datetime = Schema(
        ...,
        description="Model creation time.",
        example='2019-04-07 22:34:16.764143')

    url: UrlStr = Schema(
        ...,
        description='URL to the model',
        example='https://api.pollination.cloud/models/7bd00d58-6485-4ca6-b889-3da6d8df3ee4'
    )

    faces_url: UrlStr = Schema(
        ...,
        description='URL to get faces from this model.',
        example='https://api.pollination.cloud/models/7bd00d58-6485-4ca6-b889-3da6d8df3ee4/faces'
    )

if __name__ == '__main__':
    print(Model.schema_json(indent=2))
