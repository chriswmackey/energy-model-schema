from app.models.energy.construction import EnergyConstructionOpaque, EnergyConstructionTransparent, EnergyMaterial, EnergyMaterialNoMass, EnergyWindowMaterialAirGap, EnergyWindowMaterialBlind, EnergyWindowMaterialGlazing, EnergyWindowMaterialShade, EnergyWindowMaterialSimpleGlazSys
from app.models.samples.energyconstruction import in_material_internalsource, in_material_concrete, in_material_no_mass, in_window_air_gap, in_window_simpleglazing, in_window_blind, in_window_glazing, in_window_shade, construction_internal_floor, construction_window, construction_window_blind
from copy import copy
from pydantic import ValidationError
import pytest


def test_material_wrong():
    wrong_thickness = copy(in_material_internalsource)
    wrong_thickness['thickness'] = 5
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_thickness)
    wrong_specificheat = copy(in_material_internalsource)
    wrong_specificheat['specific_heat'] = 0
    with pytest.raises(ValidationError):
        EnergyMaterial.parse_obj(wrong_specificheat)


def test_material_nomass():
    EnergyMaterialNoMass.parse_obj(in_material_no_mass)


def test_windowairgap_wrong():
    gastype = copy(in_window_air_gap)
    gastype['gastype'] = 'Argon'
    with pytest.raises(ValidationError):
        EnergyWindowMaterialAirGap.parse_obj(gastype)
    molecularweight = copy(in_window_air_gap)
    molecularweight['molecular_weight'] = 10
    with pytest.raises(ValidationError):
        EnergyWindowMaterialAirGap.parse_obj(molecularweight)


def test_windowblind_wrong():
    wrong_emissivity = copy(in_window_blind)
    if wrong_emissivity['front_diffuse_visible_reflectance'] + wrong_emissivity['back_diffuse_visible_reflectance'] > 1:
        with pytest.raises(ValidationError):
            EnergyWindowMaterialSimpleGlazSys.parse_obj(wrong_emissivity)


def test_windowglazing():
    EnergyWindowMaterialSimpleGlazSys.parse_obj(in_window_glazing)


def test_window_blind():
    EnergyWindowMaterialBlind.parse_obj(in_window_blind)


def test_windowshade_wrong():
    wrong_type = copy(in_window_shade)
    wrong_type['type'] = 'NotEnergyWindowMaterialShade'
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_type)
    wrong_shadedistance = copy(in_window_shade)
    wrong_shadedistance['shade_toglass_distance'] = 0
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_shadedistance)
    wrong_airflow = copy(in_window_shade)
    wrong_airflow['airflow_permeability'] = 0.85
    with pytest.raises(ValidationError):
        EnergyWindowMaterialShade.parse_obj(wrong_airflow)


def test_cons_transparent():
    EnergyConstructionTransparent.parse_obj(construction_window)


def test_cons_opaque():
    EnergyConstructionOpaque.parse_obj(construction_internal_floor)


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


def construction_window_layer():
    window_wrong = copy(construction_window)
    if ((window_wrong['materials'])[0])['type'] or ((window_wrong['materials'])[-1])['type'] == 'EnergyWindowMaterialAirGap':
        with pytest.raises(ValidationError):
            EnergyConstructionTransparent.parse_obj(construction_window)
