"""Model schema."""
from pydantic import BaseModel, Schema, validator, ValidationError, constr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from app.models.energy.constructionset import ConstructionSetAbridged
from app.models.energy.construction import OpaqueConstructionAbridged, WindowConstructionAbridged
from app.models.energy.materials import EnergyMaterial, EnergyMaterialNoMass, EnergyWindowMaterialGas, EnergyWindowMaterialGasCustom, EnergyWindowMaterialGasMixture, EnergyWindowMaterialSimpleGlazSys, EnergyWindowMaterialBlind, EnergyWindowMaterialGlazing, EnergyWindowMaterialShade


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
                    raise ValueError(
                        'Number of floats must be 3.'
                    )
        return v


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


class ShadePropertiesAbridged(BaseModel):

    type: Enum('ShadePropertiesAbridged', {'type': 'ShadePropertiesAbridged'})

    energy: ShadeEnergyPropertiesAbridged


class Shade(BaseModel):

    type: Enum('Shade', {'type': 'Shade'})

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

    properties: ShadePropertiesAbridged


class Outdoors(BaseModel):

    type: Enum('Outdoors', {'type': 'Outdoors'})

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


class Ground(BaseModel):

    type: Enum('Ground', {'type': 'Ground'})


class Adiabatic(BaseModel):

    type: Enum('Adiabatic', {'type': 'Adiabatic'})


class Surface(BaseModel):

    type: Enum('Surface', {'type': 'Surface'})

    boundary_condition_objects: List[str] = Schema(
        ...,
        minItems=2,
        maxItems=3
    )

    @validator('boundary_condition_objects', whole=True)
    def check_num(cls, v):
        if len(v) != (2 or 3):
            raise ValueError('Incorrect number of boundary condition objects.')
        return v


class ApertureEnergyPropertiesAbridged(BaseModel):

    type: Enum('ApertureEnergyPropertiesAbridged', {
               'type': 'ApertureEnergyPropertiesAbridged'})

    construction: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )


class AperturePropertiesAbridged(BaseModel):

    type: Enum('AperturePropertiesAbridged', {
               'type': 'AperturePropertiesAbridged'})

    energy: ApertureEnergyPropertiesAbridged = Schema(
        default=None
    )


class ApertureType(str, Enum):

    window = 'Window'
    operable_window = 'OperableWindow'
    glass_door = 'GlassDoor'


class Aperture(BaseModel):

    type: Enum('Aperture', {'type': 'Aperture'})

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

    properties: AperturePropertiesAbridged

    aperture_type: ApertureType

    boundary_condition: Union[Ground, Outdoors, Adiabatic, Surface]

    indoor_shades: List[Shade] = Schema(
        default=None
    )

    outdoor_shades : List[Shade] = Schema(
        default=None
    )


class DoorEnergyPropertiesAbridged(BaseModel):

    type: Enum('DoorEnergyPropertiesAbridged', {
               'type': 'DoorEnergyPropertiesAbridged'})

    construction: str = Schema(
        default=None,
        regex=r'[A-Za-z0-9_-]',
        min_length=1,
        max_length=100
    )


class DoorPropertiesAbridged(BaseModel):

    type: Enum('DoorPropertiesAbridged', {'type': 'DoorPropertiesAbridged'})

    energy: DoorEnergyPropertiesAbridged = Schema(
        default=None
    )


class Door(BaseModel):

    type: Enum('Door', {'type': 'Door'})

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

    boundary_condition: Union[Ground, Outdoors, Adiabatic, Surface]

    properties: DoorPropertiesAbridged


class FaceEnergyPropertiesAbridged(BaseModel):

    type: Enum('FaceEnergyPropertiesAbridged', {
               'type': 'FaceEnergyPropertiesAbridged'})

    construction: str = Schema(
        default=None,
        regex=r'^[\s.A-Za-z0-9_-]*$',
        min_length=1,
        max_length=100
    )


class FacePropertiesAbridged(BaseModel):

    type: Enum('FacePropertiesAbridged', {'type': 'FacePropertiesAbridged'})

    energy: FaceEnergyPropertiesAbridged = Schema(
        default=None
    )


class FaceType(str, Enum):

    wall = 'Wall'
    floor = 'Floor'
    roof_ceiling = 'RoofCeiling'
    air_wall = 'AirWall'


class Face(BaseModel):

    type: Enum('Face', {'type': 'Face'})

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

    properties: FacePropertiesAbridged

    face_type: FaceType

    boundary_condition: Union[Ground, Outdoors, Adiabatic, Surface]

    apertures: List[Aperture] = Schema(
        default=None
    )

    doors: List[Door] = Schema(
        default=None
    )

    indoor_shades: List[Shade] = Schema(
        default=None
    )

    outdoor_shades : List[Shade] = Schema(
        default=None
    )


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


class RoomPropertiesAbridged(BaseModel):

    type: Enum('RoomPropertiesAbridged', {'type': 'RoomPropertiesAbridged'})

    energy: RoomEnergyPropertiesAbridged


class Room(BaseModel):

    type: Enum('Room', {'type': 'Room'})

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

    properties: RoomPropertiesAbridged

    faces: List[Face] = Schema(
        ...
    )

    indoor_shades:  List[Shade] = Schema(
        default=None)

    outdoor_shades: List[Shade] = Schema(
        default=None)


class ModelEnergyProperties(BaseModel):

    type: Enum('ModelEnergyProperties', {'type': 'ModelEnergyProperties'})

    construction_sets: List[ConstructionSetAbridged] = Schema(
        default=None
    )

    global_construction_set: str = Schema(
        default=None,
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

    rooms: List[Room] = Schema(
        default=None
    )

    orphaned_faces: List[Face] = Schema(
        default=None
    )

    orphaned_shades: List[Shade] = Schema(
        default=None
    )

    orphaned_apertures: List[Aperture] = Schema(
        default=None
    )

    orphaned_doors: List[Door] = Schema(
        default=None
    )

    north_angle: float = Schema(
        default=None,
        ge=0,
        lt=360
    )


if __name__ == '__main__':
    print(Model.schema_json(indent=2))
