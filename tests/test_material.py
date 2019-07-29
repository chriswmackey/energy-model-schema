from app.models.energy.materials import EnergyMaterial, EnergyMaterialNoMass, EnergyWindowMaterialGas, EnergyWindowMaterialGasMixture, EnergyWindowMaterialGasCustom, EnergyWindowMaterialBlind, EnergyWindowMaterialGlazing, EnergyWindowMaterialShade, EnergyWindowMaterialSimpleGlazSys
from app.models.samples.energyconstruction import in_material_internalsource, in_material_gypsum, in_material_stucco, in_material_insulation, in_material_roof_insulation, in_material_metal_decking, in_material_concrete, in_material_no_mass, in_window_simpleglazing, in_window_blind, in_window_glazing, in_window_shade, in_window_gas, in_window_gas_custom, in_window_gas_mixture
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


def test_material_wrong():
    wrong_name = copy(in_material_internalsource)
    wrong_name['name'] = ''
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_name)
    wrong_thickness = copy(in_material_internalsource)
    wrong_thickness['thickness'] = 5
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_thickness)
    wrong_specificheat = copy(in_material_internalsource)
    wrong_specificheat['specific_heat'] = 0
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_specificheat)


def test_materialnomass_wrong():
    wrong_r_value = copy(in_material_no_mass)
    wrong_r_value['r_value'] = 0
    with pytest.raises(ValidationError):
        EnergyMaterialNoMass.parse_obj(wrong_r_value)
    wrong_solar_absorptance = copy(in_material_no_mass)
    wrong_solar_absorptance['solar_absorptance'] = 2
    with pytest.raises(ValidationError):
        EnergyMaterialNoMass.parse_obj(wrong_solar_absorptance)


def test_window_simpleglaz_wrong():
    wrong_values = copy(in_window_simpleglazing)
    wrong_values['u_factor'] = 6
    with pytest.raises(ValidationError):
        EnergyWindowMaterialSimpleGlazSys.parse_obj(wrong_values)
    wrong_values['SHGC'] = 2
    with pytest.raises(ValidationError):
        EnergyWindowMaterialSimpleGlazSys.parse_obj(wrong_values)


def test_windowshade_wrong():
    wrong_type = copy(in_window_shade)
    wrong_type['type'] = 'EnergyWindowMaterial'
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_type)
    wrong_shadedistance = copy(in_window_shade)
    wrong_shadedistance['distance_to_glass'] = 0
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_shadedistance)
    wrong_airflow = copy(in_window_shade)
    wrong_airflow['airflow_permeability'] = 1
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_airflow)
