from app.models.energy.construction import EnergyConstructionOpaque, EnergyConstructionTransparent, EnergyMaterial, EnergyMaterialNoMass, EnergyWindowMaterialGas, EnergyWindowMaterialGasMixture, EnergyWindowMaterialGasCustom, EnergyWindowMaterialBlind, EnergyWindowMaterialGlazing, EnergyWindowMaterialShade, EnergyWindowMaterialSimpleGlazSys
from app.models.samples.energyconstruction import in_material_internalsource, in_material_gypsum, in_material_stucco, in_material_insulation, in_material_roof_insulation, in_material_metal_decking, in_material_concrete, in_material_no_mass, in_window_simpleglazing, in_window_blind, in_window_glazing, in_window_shade, construction_internal_floor, construction_window, construction_window_blind, construction_roof, construction_wall, in_window_gas, in_window_gas_custom, in_window_gas_mixture,construction_window2
from copy import copy
from pydantic import ValidationError
import pytest


def test_windowglazing():
    EnergyWindowMaterialGlazing.parse_obj(in_window_glazing)


def test_window_blind():
    EnergyWindowMaterialBlind.parse_obj(in_window_blind)


def test_energymaterial_gypsum():
    EnergyMaterial.parse_obj(in_material_gypsum)


def test_energymaterial_stucco():
    EnergyMaterial.parse_obj(in_material_stucco)


def test_energymaterial_insulation():
    EnergyMaterial.parse_obj(in_material_insulation)


def test_energymaterial_roofinsulation():
    EnergyMaterial.parse_obj(in_material_roof_insulation)


def test_energymaterial_metaldecking():
    EnergyMaterial.parse_obj(in_material_metal_decking)


def test_materialnomass():
    EnergyMaterialNoMass.parse_obj(in_material_no_mass)


def test_windowgas():
    EnergyWindowMaterialGas.parse_obj(in_window_gas)


def test_windowgasmixture(): 
    EnergyWindowMaterialGasMixture.parse_obj(in_window_gas_mixture)


def test_windowgascustom(): 
    EnergyWindowMaterialGasCustom.parse_obj(in_window_gas_custom)


def test_windowsimpleglazing():
    EnergyWindowMaterialSimpleGlazSys.parse_obj(in_window_simpleglazing)


def test_windowshade():
    EnergyWindowMaterialShade.parse_obj(in_window_shade)


def test_cons_transparent():
    EnergyConstructionTransparent.parse_obj(construction_window2)


def test_cons_opaque():
    EnergyConstructionOpaque.parse_obj(construction_internal_floor)


def test_cons_opaqueroof():
    EnergyConstructionOpaque.parse_obj(construction_roof)


def test_cons_opaquewall():
    EnergyConstructionOpaque.parse_obj(construction_wall)


def test_material_wrong():
    wrong_name = copy(in_material_internalsource)
    wrong_name['name'] = ''
    with pytest.raises(ValidationError): EnergyMaterial.parse_obj(wrong_name)
    wrong_thickness = copy(in_material_internalsource)
    wrong_thickness['thickness'] = 5
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_thickness)
    wrong_specificheat = copy(in_material_internalsource)
    wrong_specificheat['specific_heat'] = 0
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_specificheat)


def test_windowshade_wrong():
    wrong_type = copy(in_window_shade)
    wrong_type['type'] = 'NotEnergyWindowMaterialShade'
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_type)
    wrong_shadedistance = copy(in_window_shade)
    wrong_shadedistance['shade_to_glass_distance'] = 0
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_shadedistance)
    wrong_airflow = copy(in_window_shade)
    wrong_airflow['airflow_permeability'] = 1
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_airflow)


def test_length_opaque():
    cons_length = copy(construction_internal_floor)
    if len(cons_length['materials']) > 10:
        with pytest.raises(ValidationError):
            EnergyConstructionOpaque.parse_obj(construction_internal_floor)
    elif len(cons_length['materials']) == 0:
        with pytest.raises(ValidationError):
            EnergyConstructionOpaque.parse_obj(construction_internal_floor)


def test_cons_wind():
    wind_len = copy(construction_window)
    if len(wind_len['materials']) > 8:
        with pytest.raises(ValidationError):
            EnergyConstructionTransparent.parse_obj(construction_window)
    elif len(wind_len['materials']) == 0:
        with pytest.raises(ValidationError):
            EnergyConstructionTransparent.parse_obj(construction_window)
