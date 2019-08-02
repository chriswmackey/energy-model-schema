"""Model schema."""
from pydantic import BaseModel, Schema, validator, ValidationError, constr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.constructionset import ConstructionSetAbridged
from app.models.energy.construction import OpaqueConstructionAbridged, WindowConstructionAbridged
from app.models.energy.materials import EnergyMaterial, EnergyMaterialNoMass, EnergyWindowMaterialGas, EnergyWindowMaterialGasCustom, EnergyWindowMaterialGasMixture, EnergyWindowMaterialSimpleGlazSys, EnergyWindowMaterialBlind, EnergyWindowMaterialGlazing, EnergyWindowMaterialShade


class RoomEnergyPropertiesAbridged(BaseModel):

    type: Enum('RoomEnergyPropertiesAbridged', {
               'type': 'RoomEnergyPropertiesAbridged'})

    construction_set: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    program_type: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    people: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    lighting: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    electric_equipment: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    gas_equipment: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    infiltration: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    ventilation: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )


class RoomProperties(BaseModel):

    type: Enum('RoomProperties', {'type': 'RoomProperties'})

    energy: RoomEnergyPropertiesAbridged


class RoomAbridged(BaseModel):

    type: Enum('RoomAbridged', {'type': 'RoomAbridged'})

    name: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    display_name: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    properties: RoomProperties

    faces: List[constr(regex=r'[A-Za-z0-9_-]', min_length=1, max_length=100)] = Schema(
        ...
    )

    interior_shades:  List[constr(
        regex=r'[A-Za-z0-9_-]', min_length=1, max_length=100)] = Schema(
            default=None)

    outdoor_shades: List[constr(
        regex=r'[A-Za-z0-9_-]', min_length=1, max_length=100)] = Schema(
            default=None)


class FaceEnergyPropertiesAbridged(BaseModel):

    type: Enum('FaceEnergyPropertiesAbridged', {
               'type': 'FaceEnergyPropertiesAbridged'})

    construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )


class FaceProperties(BaseModel):

    type: Enum('FaceProperties', {'type': 'FaceProperties'})

    energy: FaceEnergyPropertiesAbridged = Schema(
        default=None
    )


class Wall(BaseModel):

    type: Enum('Wall', {'type': 'Wall'})


class RoofCeiling(BaseModel):

    type: Enum('RoofCeiling', {'type': 'RoofCeiling'})


class Floor(BaseModel):

    type: Enum('Floor', {'type': 'Floor'})


class AirWall(BaseModel):

    type: Enum('AirWall', {'type': 'AirWall'})


class Shading(BaseModel):

    type: Enum('Shading', {'type': 'Shading'})


class Plane(BaseModel):

    n: List[float] = Schema(
        ...,
        description="Normal"
    )

    o: List[float] = Schema(
        ...,
        description="Origin"
    )

    x: List[float] = Schema(
        default=None,
        description="x-axis"
    )


class Face3D(BaseModel):

    type: Enum('Face3D', {'type': 'Face3D'})

    boundary: List[List[float]]

    holes: List[List[List[float]]] = Schema(
        default=None
    )

    plane: Plane = Schema(
        default=None
    )

    @validator('boundary', whole=True)
    def check_num_items(cls, v):
        for i in v:
            if len(i) != 3:
                raise ValueError(
                    'Number of floats must be 3.'
                )
        return v

    @validator('holes', whole=True)
    def check_num_items_holes(cls, v):
        for pt_list in v:
            for pt in pt_list:
                if len(pt) != 3:
                    raise ValidationError(
                        'Number of floats must be 3.'
                    )
        return v


class Ground(BaseModel):

    type: Enum('Ground', {'type': 'Ground'})

    sun_exposure: bool = Schema(
        default=None
    )

    wind_exposure: bool = Schema(
        default=None
    )

    view_factor: Union[str, float] = Schema(
        'autocalculate',
        ge=0,
        le=1
    )


class Outdoors(Ground):

    type: Enum('Outdoors', {'type': 'Outdoors'})


class Adiabatic(Ground):

    type: Enum('Adiabatic', {'type': 'Adiabatic'})


class Surface(Ground):

    type: Enum('Surface', {'type': 'Surface'})

    boundary_condition_object: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )


class FaceAbridged(BaseModel):

    type: Enum('FaceAbridged', {'type': 'FaceAbridged'})

    name: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    display_name: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    geometry: Face3D

    properties: FaceProperties

    face_type: Union[Wall, RoofCeiling, Floor, AirWall,  Shading]

    boundary_condition: Union[Ground, Outdoors, Adiabatic, Surface]

    parent: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    apertures: List[constr(regex=r'[A-Za-z0-9_-]', min_length=1, max_length=100)] = Schema(
        default=None
    )

    doors: List[constr(regex=r'[A-Za-z0-9_-]', min_length=1, max_length=100)] = Schema(
        default=None
    )


class ShadeEnergyPropertiesAbridged(BaseModel):

    type: Enum('ShadeEnergyPropertiesAbridged', {
               'type': 'ShadeEnergyPropertiesAbridged'})

    diffuse_reflectance: float = Schema(
        0.2,
        ge=0,
        le=1
    )

    specular_reflectance: float = Schema(
        0,
        ge=0,
        le=1
    )

    transmittance: float = Schema(
        0,
        ge=0,
        le=1
    )

    transmittance_schedule: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    @validator('transmittance_schedule')
    def check_field(cls, v, values):
        if values['transmittance'] != "" and v != "":
            raise ValueError(
                'Can not specify both transmittance and transmittance_schedule.'
            )


class ShadeProperties(BaseModel):

    type: Enum('ShadeProperties', {'type': 'ShadeProperties'})

    energy: ShadeEnergyPropertiesAbridged


class ShadeAbridged(BaseModel):

    type: Enum('ShadeAbridged', {'type': 'ShadeAbridged'})

    name: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    display_name: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    geometry: Face3D

    properties: ShadeProperties

    parent: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )


class ApertureEnergyPropertiesAbridged(BaseModel):

    type: Enum('ApertureEnergyPropertiesAbridged', {
               'type': 'ApertureEnergyPropertiesAbridged'})

    construction: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )


class ApertureProperties(BaseModel):

    type: Enum('ApertureProperties', {'type': 'ApertureProperties'})

    energy: ApertureEnergyPropertiesAbridged = Schema(
        default=None
    )


class Window(BaseModel):

    type: Enum('Window', {'type': 'Window'})


class OperableWindow(BaseModel):

    type: Enum('OperableWindow', {'type': 'OperableWindow'})


class GlassDoor(BaseModel):

    type: Enum('GlassDoor', {'type': 'GlassDoor'})


class ApertureAbridged(BaseModel):

    type: Enum('ApertureAbridged', {'type': 'ApertureAbridged'})

    name: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    display_name: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    geometry: Face3D

    properties: ApertureProperties

    aperture_type: Union[Window, OperableWindow, GlassDoor]

    boundary_condition: Union[Ground, Outdoors, Adiabatic, Surface]

    parent: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )


class DoorEnergyPropertiesAbridged(BaseModel):

    type: Enum('DoorEnergyPropertiesAbridged', {
               'type': 'DoorEnergyPropertiesAbridged'})


class DoorProperties(BaseModel):

    type: Enum('DoorProperties', {'type': 'DoorProperties'})

    energy: DoorEnergyPropertiesAbridged


class DoorAbridged(BaseModel):

    type: Enum('DoorAbridged', {'type': 'DoorAbridged'})

    name: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    display_name: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    geometry: Face3D

    properties: DoorProperties


class ModelEnergyProperties(BaseModel):

    type: Enum('ModelEnergyProperties', {'type': 'ModelEnergyProperties'})

    construction_sets: List[ConstructionSetAbridged] = Schema(
        default=None
    )

    global_construction_set: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    constructions: List[Union[OpaqueConstructionAbridged,
                              WindowConstructionAbridged]]

    materials: List[Union[EnergyMaterial, EnergyMaterialNoMass, EnergyWindowMaterialGas, EnergyWindowMaterialGasCustom, EnergyWindowMaterialGasMixture,
                          EnergyWindowMaterialSimpleGlazSys, EnergyWindowMaterialBlind, EnergyWindowMaterialGlazing, EnergyWindowMaterialShade]]


class ModelProperties(BaseModel):

    type: Enum('ModelProperties', {'type': 'ModelProperties'})

    energy: ModelEnergyProperties


class Model(BaseModel):

    type: Enum('Model', {'type': 'Model'})

    name: str = Schema(
        ...,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )

    display_name: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )

    properties: ModelProperties

    rooms: List[RoomAbridged] = Schema(
        default=None
    )

    faces: List[FaceAbridged] = Schema(
        default=None
    )

    shades: List[ShadeAbridged] = Schema(
        default=None
    )

    apertures: List[ApertureAbridged] = Schema(
        default=None
    )

    doors: List[DoorAbridged] = Schema(
        default=None
    )

    north_angle: float = Schema(
        default=None,
        ge=0,
        lt=360
    )


if __name__ == '__main__':
    print(Model.schema_json(indent=2))
