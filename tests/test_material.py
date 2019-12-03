from app.models.energy.materials import EnergyMaterial, EnergyMaterialNoMass, \
    EnergyWindowMaterialGas, EnergyWindowMaterialGasMixture, \
    EnergyWindowMaterialGasCustom, EnergyWindowMaterialBlind, \
    EnergyWindowMaterialGlazing, EnergyWindowMaterialShade, \
    EnergyWindowMaterialSimpleGlazSys
from app.models.samples.energyconstruction import material_gypsum, material_stucco, \
    material_insulation, material_roof_insulation, material_metal_decking, \
    material_concrete, material_no_mass, window_simpleglazing, window_blind, \
    window_glazing, window_shade, window_gas, window_gas_custom, window_gas_mixture
from copy import copy
from pydantic import ValidationError
import pytest


def test_windowglazing():
    EnergyWindowMaterialGlazing.parse_obj(window_glazing)


def test_window_blind():
    EnergyWindowMaterialBlind.parse_obj(window_blind)


def test_energymaterial_gypsum():
    EnergyMaterial.parse_obj(material_gypsum)


def test_energymaterial_stucco():
    EnergyMaterial.parse_obj(material_stucco)


def test_energymaterial_insulation():
    EnergyMaterial.parse_obj(material_insulation)


def test_energymaterial_roofinsulation():
    EnergyMaterial.parse_obj(material_roof_insulation)


def test_energymaterial_metaldecking():
    EnergyMaterial.parse_obj(material_metal_decking)


def test_materialnomass():
    EnergyMaterialNoMass.parse_obj(material_no_mass)


def test_windowgas():
    EnergyWindowMaterialGas.parse_obj(window_gas)


def test_windowgasmixture():
    EnergyWindowMaterialGasMixture.parse_obj(window_gas_mixture)


def test_windowgascustom():
    EnergyWindowMaterialGasCustom.parse_obj(window_gas_custom)


def test_windowsimpleglazing():
    EnergyWindowMaterialSimpleGlazSys.parse_obj(window_simpleglazing)


def test_windowshade():
    EnergyWindowMaterialShade.parse_obj(window_shade)


def test_material_wrong():
    wrong_name = copy(material_gypsum)
    wrong_name['name'] = ''
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_name)
    wrong_thickness = copy(material_gypsum)
    wrong_thickness['thickness'] = 5
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_thickness)
    wrong_specificheat = copy(material_gypsum)
    wrong_specificheat['specific_heat'] = 0
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_specificheat)


def test_materialnomass_wrong():
    wrong_r_value = copy(material_no_mass)
    wrong_r_value['r_value'] = 0
    with pytest.raises(ValidationError):
        EnergyMaterialNoMass.parse_obj(wrong_r_value)
    wrong_solar_absorptance = copy(material_no_mass)
    wrong_solar_absorptance['solar_absorptance'] = 2
    with pytest.raises(ValidationError):
        EnergyMaterialNoMass.parse_obj(wrong_solar_absorptance)


def test_window_simpleglaz_wrong():
    wrong_values = copy(window_simpleglazing)
    wrong_values['u_factor'] = 6
    with pytest.raises(ValidationError):
        EnergyWindowMaterialSimpleGlazSys.parse_obj(wrong_values)
    wrong_values['SHGC'] = 2
    with pytest.raises(ValidationError):
        EnergyWindowMaterialSimpleGlazSys.parse_obj(wrong_values)


def test_windowshade_wrong():
    wrong_type = copy(window_shade)
    wrong_type['type'] = 'EnergyWindowMaterial'
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_type)
    wrong_shadedistance = copy(window_shade)
    wrong_shadedistance['distance_to_glass'] = 0
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_shadedistance)
    wrong_airflow = copy(window_shade)
    wrong_airflow['airflow_permeability'] = 1
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_airflow)
