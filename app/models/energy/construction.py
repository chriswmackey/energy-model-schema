"""Construction Schema"""
from pydantic import BaseModel, Schema, validator, ValidationError
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


class Roughness(str, Enum):
    """
    Relative roughness of a particular material layer.
    """
    very_rough = 'VeryRough'
    rough = 'Rough'
    medium_rough = 'MediumRough'
    medium_smooth = 'MediumSmooth'
    smooth = 'Smooth'
    very_smooth = 'VerySmooth'


class EnergyMaterial(BaseModel):
    """Material 'types' used to describe layers within opaque construction elements."""
    type: Enum('EnergyMaterial', {'type': 'EnergyMaterial'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    roughness: Roughness = Roughness.medium_rough

    thickness: float = Schema(
        ...,
        gt=0,
        le=3,
        description='Thickness of the material layer in meters.'
    )

    conductivity: float = Schema(
        ...,
        gt=0,
        description='Thermal conductivity of the material layer in W/(m-K).',
    )

    density: float = Schema(
        ...,
        gt=0,
        description='Density of the material layer in kg/m3.'
    )

    specific_heat: float = Schema(
        ...,
        gt=0,
        description='Specific heat of the material layer in J/(kg-K).'
    )

    thermal_absorptance: float = Schema(
        0.9,
        gt=0,
        le=0.99999,
        description='Fraction of incident long wavelength radiation that is absorbed by'
        ' the material. Default value is 0.9.'
    )

    solar_absorptance: float = Schema(
        0.7,
        ge=0,
        le=1,
        description='Fraction of incident solar radiation absorbed by the material.'
        ' Default value is 0.7.'
    )

    visible_absorptance: float = Schema(
        0.7,
        ge=0,
        le=1,
        description='Fraction of incident visible wavelength radiation absorbed by the'
        ' material. Default value is 0.7.'
    )


class EnergyMaterialNoMass(BaseModel):
    """
    Used when only the thermal resistance (R value) of the material is known. Used for 
    opaque construction elements.
    """

    type: Enum('EnergyMaterialNoMass', {'type': 'EnergyMaterialNoMass'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    r_value: float = Schema(
        ...,
        ge=0.001,
        description='Used to enter the thermal resistance (R-value) of the material'
        ' layer in (m2-K)/W.'
    )

    roughness: Roughness = Roughness.medium_rough

    thermal_absorptance: float = Schema(
        0.9,
        gt=0,
        le=0.99999,
        description='Fraction of incident long wavelength radiation that is absorbed by'
        ' the material. Default value is 0.9.'
    )

    solar_absorptance: float = Schema(
        0.7,
        ge=0,
        le=1,
        description='Fraction of incident solar radiation absorbed by the material.'
        ' Default value is 0.7.'
    )

    visible_absorptance: float = Schema(
        0.7,
        ge=0,
        le=1,
        description='Fraction of incident visible wavelength radiation absorbed by the'
        ' material. Default value is 0.7.'
    )


class GasType (str, Enum):
    air = 'Air'
    argon = 'Argon'
    krypton = 'Krypton'
    xenon = 'Xenon'
    custom = 'Custom'


class EnergyWindowMaterialAirGap(BaseModel):
    """Create single layer of air gap.

    Air gap can be combined with EnergyWindowMaterialGlazing to make multi-pane windows.
    """

    type: Enum('EnergyWindowMaterialAirGap', {
               'type': 'EnergyWindowMaterialAirGap'})

    name: str = Schema(
        'AIRGAP',
        regex=r'^[\s.A-Za-z0-9_-]*$'
    )

    gastype: GasType = GasType.air

    thickness: float = Schema(
        0.0125,
        gt=0,
        description='Thickness of the air gap in meters. Default value is 0.0125.'
    )
    # The following properties are used only when the gas type is custom.
    conductivity_coeff_A: float = Schema(
        0,
        description='The A coefficient for gas conductivity in W/(m-K). Used only if Gas'
        ' Type is Custom.'
    )

    conductivity_coeff_B: float = Schema(
        0,
        description='The A coefficient for gas conductivity in W/(m-K2). Used only if'
        ' Gas Type is Custom.'
    )

    conductivity_coeff_C: float = Schema(
        0,
        description='The A coefficient for gas conductivity in W/(m-K3). Used only if'
        ' Gas Type is Custom.'
    )

    viscosity_coeff_A: float = Schema(
        0,
        gt=0,
        description='The A coefficient for gas viscosity in kg/(m-s). Used only if Gas'
        ' Type is Custom.'
    )

    viscosity_coeff_B: float = Schema(
        0,
        description='The B coefficient for gas viscosity in kg/(m-s-K). Used only if Gas'
        ' Type is Custom.'
    )

    viscosity_coeff_C: float = Schema(
        0,
        description='The C coefficient for gas viscosity in kg/(m-s-K2). Used only if'
        ' Gas Type is Custom.'
    )

    specific_heat_coeff_A: float = Schema(
        0,
        gt=0,
        description='The A coefficient for gas specific heat in J/(kg-K). Used only if'
        ' Gas Type is Custom.'
    )

    specific_heat_coeff_B: float = Schema(
        0,
        gt=0,
        description='The B coefficient for gas specific heat in J/(kg-K2). Used only if'
        ' Gas Type is Custom.'
    )

    specific_heat_coeff_C: float = Schema(
        0,
        gt=0,
        description='The C coefficient for gas specific heat in J/(kg-K3). Used only if'
        ' Gas Type is Custom.'
    )

    specific_heat_ratio: float = Schema(
        1,
        gt=1,
        description='The specific heat ratio for gas. Used only if Gas Type is Custom.'
    )

    molecular_weight: float = Schema(
        20,
        ge=20,
        le=200,
        description='The molecular weight for gas in g/mol. Used only if Gas Type is'
        ' Custom.'
    )


class EnergyWindowMaterialSimpleGlazSys(BaseModel):
    """Describe an entire glazing system rather than individual layers.

    Used when only very limited information is available on the glazing layers or when
    specific performance levels are being targeted.
    """

    type: Enum('EnergyWindowMaterialSimpleGlazSys', {
               'type': 'EnergyWindowMaterialSimpleGlazSys'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    u_factor: float = Schema(
        ...,
        gt=0,
        le=5.8,
        description='Used to describe the value for window system U-Factor, or overall'
        ' heat transfer coefficient in W/(m2-K).'
    )

    SHGC: float = Schema(
        ...,
        gt=0,
        lt=1,
        description='Unitless  quantity describing Solar Heat Gain Coefficient for'
        ' normal incidence and vertical orientation.'
    )


class SlatOrientation (str, Enum):
    horizontal = 'Horizontal'
    vertical = 'Vertical'
    description = 'Choices including Horizontal and Vertical. Horizontal means the slats'
    ' are parallel to the X-axis of the window. Vertical means the slats are parallel'
    ' to the Y-axis of the window.'


class EnergyWindowMaterialBlind(BaseModel):
    """Window blind properties.

    Window blind properties consist of flat, equally-spaced slats.
    """

    type: Enum('EnergyWindowMaterialBlind', {
               'type': 'EnergyWindowMaterialBlind'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    slat_orientation: SlatOrientation

    slat_width: float = Schema(
        0.025,
        gt=0,
        le=1,
        description='The width of slat measured from edge to edge in meters.'
    )

    slat_separation: float = Schema(
        0.01875,
        gt=0,
        le=1,
        description='The distance between the front of a slat and the back of the'
        ' adjacent slat in meters.'
    )

    slat_thickness: float = Schema(
        0.001,
        gt=0,
        le=0.1,
        description='The distance between the faces of a slat in meters. The default'
        ' value is 0.001.'
    )

    slat_angle: float = Schema(
        45,
        ge=0,
        le=180,
        description='The angle (degrees) between the glazing outward normal and the slat'
        ' outward normal where the outward normal points away from the front face of the'
        ' slat (degrees). The default value is 45.'
    )

    slat_conductivity: float = Schema(
        221,
        gt=0,
        description='The thermal conductivity of the slat in W/(m-K). Default value is'
        ' 221.'
    )

    beam_solar_transmittance: float = Schema(
        0,
        ge=0,
        lt=1,
        description='The beam solar transmittance of the slat, assumed to be independent'
        ' of angle of incidence on the slat. Any transmitted beam radiation is assumed'
        ' to be 100% diffuse (i.e., slats are translucent). The default value is 0.'
    )

    front_beam_solar_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The beam solar reflectance of the front side of the slat, it is'
        ' assumed to be independent of the angle of incidence. Default value is 0.5.'
    )

    back_beam_solar_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The beam solar reflectance of the back side of the slat, it is'
        ' assumed to be independent of the angle of incidence. Default value is 0.5.'
    )

    diffuse_solar_transmittance: float = Schema(
        0,
        ge=0,
        lt=1,
        description='The slat transmittance for hemisperically diffuse solar radiation.'
        ' Default value is 0.'
    )

    front_diffuse_solar_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The front-side slat reflectance for hemispherically diffuse solar'
        ' radiation. Default value is 0.5.'
    )

    back_diffuse_solar_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The back-side slat reflectance for hemispherically diffuse solar'
        ' radiation. Default value is 0.5.'
    )

    beam_visible_transmittance: float = Schema(
        0,
        ge=0,
        lt=1,
        description='The beam visible tranmsittance of the slat, it is assumed to be'
        ' independent of the angle of incidence. Default value is 0.'
    )

    front_beam_visible_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The beam visible reflectance on the front side of the slat, it is'
        ' assumed to be independent of the angle of incidence. Default value is 0.5.'
    )

    back_beam_visible_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The beam visible reflectance on the back side of the slat, it is'
        ' assumed to be independent of the angle of incidence. Default value is 0.5.'
    )

    diffuse_visible_transmittance: float = Schema(
        0,
        ge=0,
        le=1,
        description='The slat transmittance for hemispherically diffuse visible'
        ' radiation. This value should equal “Slat Beam Visible Transmittance.”'
    )

    front_diffuse_visible_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The front-side slat reflectance for hemispherically diffuse visible'
        ' radiation. This value should equal “Front Side Slat Beam Visible Reflectance.”'
        ' Default value is 0.5.'
    )

    back_diffuse_visible_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The back-side slat reflectance for hemispherically diffuse visible'
        ' radiation. This value should equal “Back Side Slat Beam Visible Reflectance.'
        ' Default value is 0.5.”'
    )

    infrared_hemispherical_transmittance: float = Schema(
        0,
        ge=0,
        lt=1,
        description='The slat infrared transmittance. It is zero for solid metallic,'
        ' wooden or glass slats, but may be non-zero in some cases such as for thin'
        ' plastic slats. The default value is 0.'
    )

    front_infrared_hemispherical_emissivity: float = Schema(
        0.9,
        ge=0,
        lt=1,
        description='Front side hemispherical emissivity of the slat. Default is 0.9 for'
        ' most materials. The default value is 0.9.'
    )

    back_infrared_hemispherical_emissivity: float = Schema(
        0.9,
        ge=9,
        le=1,
        description='Back side hemispherical emissivity of the slat. Default is 0.9 for'
        ' most materials. The default value is 0.9.'
    )

    blind_toglass_distance: float = Schema(
        0.05,
        ge=0.01,
        le=1,
        description='The distance from the mid-plane of the blind to the adjacent glass'
        ' in meters. The default value is 0.05.'
    )

    top_opening_multiplier: float = Schema(
        0.5,
        ge=0,
        le=1,
        description='The effective area for air flow at the top of the shade, divided by'
        ' the horizontal area between glass and shade. The default value is 0.5'
    )

    bottom_opening_multiplier: float = Schema(
        0.5,
        ge=0,
        le=1,
        description='The effective area for air flow at the bottom of the shade, divided'
        ' by the horizontal area between glass and shade. The default value is 0.5.'
    )

    left_opening_multiplier: float = Schema(
        0.5,
        ge=0,
        le=1,
        description='The effective area for air flow at the left side of the shade,'
        ' divided by the vertical area between glass and shade. The default value is 0.5.'
    )

    right_opening_multiplier: float = Schema(
        0.5,
        ge=0,
        le=1,
        description='The effective area for air flow at the right side of the shade,'
        ' divided by the vertical area between glass and shade. The default value is 0.5.'
    )

    minimum_slat_angle: float = Schema(
        0,
        ge=0,
        le=180,
        description='The minimum allowed slat angle in degrees. The default value is 0.'
    )

    maximum_slat_angle: float = Schema(
        180,
        ge=0,
        le=180,
        description='The maximum allowed slat angle in degrees. The default value is 180.'
    )


class OpticalDatatype (str, Enum):
    """
    For SpectralAverage optical data type, solar transmittance and
    reflectance are assumed to be averaged over the solar spectrum and values
    for visible transmittance and reflectance are assumed to be averaged over
    the solar spectrum and weighted by the response of the human eye.'
    """
    spectral = 'Spectral'
    spectral_average = 'SpectralAverage'
    bsdf = 'BSDF'
    spectral_and_angle = 'SpectralAngle'


class SolarDiffusing (str, Enum):
    """
    Takes values No and Yes. If No (default), the beam solar radiation incident on the
    glass is transmitted as beam radiation with no diffuse component.
    If Yes, the beam  solar radiation incident on the glass is transmitted as
    hemisphericall diffuse radiation with no beam component.
    """
    no = 'No'
    yes = 'Yes'


class EnergyWindowMaterialGlazing(BaseModel):
    """Describe a single glass pane corresponding to a layer in a window construction."""

    type: Enum('EnergyWindowMaterialGlazing', {
               'type': 'EnergyWindowMaterialGlazing'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    optical_datatype: OpticalDatatype = OpticalDatatype.spectral_average

    spectral_dataset_name: str = Schema(
        '',
        description='Used to specify name of the spectral data set if optical data'
        ' type = Spectral.'
    )

    thickness_glass: float = Schema(
        0.003,
        gt=0,
        description='The surface-to-surface of the glass in meters. Default value is'
        ' 0.003.'
    )

    solar_transmittance: float = Schema(
        0,
        ge=0,
        le=1,
        description='Transmittance of solar radiation through the glass at normal'
        ' incidence. Default value is 0.'
    )

    solar_reflectance: float = Schema(
        0,
        ge=0,
        le=1,
        description='Reflectance of solar radiation off of the front side of the glass'
        ' at normal incidence, averaged over the solar spectrum. Default value is 0.'
    )

    solar_reflectance_back: float = Schema(
        0,
        description='Reflectance of solar radiation off of the back side of the glass at'
        ' normal incidence, averaged over the solar spectrum.'
    )

    visible_transmittance: float = Schema(
        0,
        ge=0,
        le=1,
        description='Transmittance of visible light through the glass at normal incidence.'
        ' Default value is 0.'
    )

    visible_reflectance: float = Schema(
        0,
        ge=0,
        le=1,
        description='Reflectance of visible light off of the front side of the glass at'
        ' normal incidence. Default value is 0.'
    )

    visible_reflectance_back: float = Schema(
        0,
        description='Reflectance of visible light off of the back side of the glass at'
        ' normal incidence averaged over the solar spectrum and weighted by the response'
        ' of the human eye.'
    )

    infrared_transmittance: float = Schema(
        0,
        description='Long-wave transmittance at normal incidence.'
    )

    front_emissivity: float = Schema(
        0.84,
        ge=0,
        le=1,
        description='Infrared hemispherical emissivity of the front (outward facing)'
        ' side of the glass.  Default value is 0.84, which is typical for clear glass'
        ' without a low-e coating.'
    )

    back_emissivity: float = Schema(
        0.84,
        ge=0,
        le=1,
        description='Infrared hemispherical emissivity of the back (inward facing) side'
        ' of the glass.  Default value is 0.84, which is typical for clear glass without'
        ' a low-e coating.'
    )

    conductivity_glass: float = Schema(
        0.9,
        gt=0,
        description='Thermal conductivity of the glass in W/(m-K). Default value is 0.9,'
        ' which is  typical for clear glass without a low-e coating.'
    )

    dirt_correction: float = Schema(
        1,
        description='Factor that corrects for the presence of dirt on the glass. A'
        ' default value of 1 indicates the glass is clean.'
    )

    solar_diffusing: SolarDiffusing = SolarDiffusing.no


class EnergyWindowMaterialShade (BaseModel):
    """This object specifies the properties of window shade materials."""

    type: Enum('EnergyWindowMaterialShade', {
               'type': 'EnergyWindowMaterialShade'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    solar_transmittance: float = Schema(
        0.4,
        ge=0,
        lt=1,
        description='The transmittance averaged over the solar spectrum. It is assumed'
        ' independent of incidence angle. Default value is 0.4.'
    )

    solar_reflectance: float = Schema(
        0.5,
        ge=0,
        lt=1,
        description='The reflectance averaged over the solar spectrum. It us assumed'
        ' same on both sides of shade and independent of incidence angle. Default'
        ' value is 0.5'
    )

    visible_transmittance: float = Schema(
        0.4,
        ge=0,
        lt=1,
        description='The transmittance averaged over the solar spectrum and weighted by'
        ' the response of the human eye. It is assumed independent of incidence angle.'
        ' Default value is 0.4.'
    )

    visible_reflectance: float = Schema(
        0.4,
        ge=0,
        lt=1,
        description='The transmittance averaged over the solar spectrum and weighted by'
        ' the response of the human eye. It is assumed independent of incidence angle.'
        ' Default value is 0.4'
    )

    infrared_hemispherical_emissivity: float = Schema(
        0.9,
        gt=0,
        lt=1,
        description='The effective long-wave emissivity. It is assumed same on both'
        ' sides of shade. Default value is 0.9.'
    )

    infrared_transmittance: float = Schema(
        0,
        ge=0,
        lt=1,
        description='The effective long-wave transmittance. It is assumed independent'
        ' of incidence angle. Default value is 0.'
    )

    thickness: float = Schema(
        0.005,
        gt=0,
        description='The thickness of the shade material in meters. Default value is'
        ' 0.005.'
    )

    conductivity: float = Schema(
        0.1,
        gt=0,
        description='The conductivity of the shade material in W/(m-K). Default value'
        ' is 0.1.'
    )

    shade_toglass_distance: float = Schema(
        0.05,
        ge=0.001,
        le=1,
        description='The distance from shade to adjacent glass in meters. Default value'
        ' is 0.05'
    )

    top_opening_multiplier: float = Schema(
        0,
        ge=0,
        le=1,
        description='The effective area for air flow at the top of the shade, divided by'
        ' the horizontal area between glass and shade. Default value is 0.'
    )

    bottom_opening_multiplier: float = Schema(
        0,
        ge=0,
        le=1,
        description='The effective area for air flow at the bottom of the shade, divided'
        ' by the horizontal area between glass and shade. Default value is 0.'
    )

    left_opening_multiplier: float = Schema(
        0,
        ge=0,
        le=1,
        description='The effective area for air flow at the left side of the shade,'
        ' divided by the vertical area between glass and shade. Default value is 0.'
    )

    right_opening_multiplier: float = Schema(
        0,
        ge=0,
        le=1,
        description='The effective area for air flow at the right side of the shade,'
        ' divided by the vertical area between glass and shade. Default value is 0.'
    )

    airflow_permeability: float = Schema(
        0,
        ge=0,
        le=0.8,
        description='The fraction of the shade surface that is open to air flow.'
        ' If air cannot pass through the shade material, airflow_permeability = 0.'
        ' Default value is 0.'
    )


class EnergyConstructionTransparent(BaseModel):
    """
    Group of objects to describe the physical properties and configuration for 
    the building envelope and interior elements that is the windows of the building.

    """
    type: Enum('EnergyConstructionTransparent', {
               'type': 'EnergyConstructionTransparent'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    materials: List[
        Union[
            EnergyWindowMaterialAirGap,
            EnergyWindowMaterialSimpleGlazSys, EnergyWindowMaterialBlind,
            EnergyWindowMaterialGlazing, EnergyWindowMaterialShade
        ]
    ] = Schema(
        ...,
        description='List of materials. The order of the materials is from outside to'
        ' inside.',
        minItems=1
    )

    @validator('materials', whole=True)
    def check_min_items(cls, materials):
        "Ensure length of material is at least 1."
        if len(materials) == 0:
            raise ValidationError(
                'Window construction should at least have one material.'
            )

        elif len(materials) > 8:
            raise ValidationError(
                'Window construction cannot have more than 8 materials.'
            )
        return materials
# check
    # @validator('materials', whole=True)
    # def check_item_sequence(cls, materials):
    #    "Ensure Air Gap is not the outermost layer."
    #    if (materials[0]).type or (materials[-1]).type == 'EnergyWindowMaterialAirGap':
    #        raise ValidationError(
    #            'Air Gap can not be outermost layer'
    #        )
    #    return materials


class EnergyConstructionOpaque(BaseModel):
    """
    Group of objects to describe the physical properties and configuration for 
    the building envelope and interior elements that is the walls, roofs, floors, 
    and doors of the building.
    """
    type: Enum('EnergyConstructionOpaque', {
               'type': 'EnergyConstructionOpaque'})

    name: str = Schema(
        ...,
        regex=r'^[\s.A-Za-z0-9_-]*$',
    )

    materials: List[
        Union[
            EnergyMaterial, EnergyMaterialNoMass
        ]
    ] = Schema(
        ...,
        description='List of materials. The order of the materials is from outside to'
        ' inside.',
        minItems=1
    )

    @validator('materials', whole=True)
    def check_min_items(cls, materials):
        "Ensure length of material is at least 1."
        if len(materials) == 0:
            raise ValidationError(
                'Opaque construction should at least have one material.'
            )
        elif len(materials) > 10:
            raise ValidationError(
                'Opaque construction cannot have more than 10 materials.'
            )
        return materials


if __name__ == '__main__':
    print(EnergyConstructionTransparent.schema_json(indent=2))

if __name__ == '__main__':
    print(EnergyConstructionOpaque.schema_json(indent=2))
