in_material_internalsource = {
    'type': 'EnergyMaterial',
    'name': 'Internal Source',
    'roughness': 'Smooth',
    'thickness': 0.012,
    'conductivity': 0.6,
    'density': 1000,
    'specific_heat': 4185,
    'thermal_absorptance': 0.95,
    'solar_absorptance': 0.7,
    'visible_absorptance': 0.7
}

in_material_concrete = {
    'type': 'EnergyMaterial',
    'name': '8in Concrete HW',
    'roughness': 'MediumRough',
    'thickness': 0.20,
    'conductivity': 1.72,
    'density': 2242,
    'specific_heat': 836,
    'thermal_abosrptance': 0.9,
    'solar_absorptance': 0.65,
    'visible_absorptance': 0.65
}

in_material_no_mass = {
    'type': 'EnergyMaterialNoMass',
    'name': 'CP02 Carpet Pad',
    'r_value': 0.9,
    'roughness': 'Smooth',
    'thermal_absorptance': 0.8,
    'solar_abosrptance': 0.8,
    'visible_absorptance': 0.8
}

in_window_air_gap = {
    'type': 'EnergyWindowMaterialAirGap',
    'name': 'Air 13mm',
    'gastype': 'Air',
    'thickness': 0.0127
}

in_window_simpleglazing = {
    'type': 'EnergyWindowMaterialSimpleGlazSys',
    'name': 'Fixed Window 2.00 0.40 0.31',
    'u_factor': 1.98,
    'SHGC': 0.4
}

in_window_blind = {
    'type': 'EnergyWindowMaterialBlind',
    'name': 'Window Material Blind 1',
    'slat_orientation': 'Horizontal',
}

in_window_glazing = {
    'type': 'EnergyWindowMaterialGlazing',
    'name': 'Theoretical Glass 167',
    'optical_datatype': 'SpectralAverage',
    'spectral_dataset_name': '',
    'thickness_glass': 0.029,
    'solar_transmittance': 0.2374,
    'solar_reflectance': 0.7126,
    'solar_reflectance_back': 0,
    'visible_transmittance': 0.2512,
    'visible_reflectance': 0.6988,
    'visible_reflectance_back': 0,
    'infrared_transmittance': 0,
    'front_emissivity': 0.985,
    'back_emissivity': 0.985,
    'conductivity_glass': 2.1073,
    'dirt_correlation': 1,
    'solar_diffusing': 'No'
}

in_window_shade = {
    'type': 'EnergyWindowMaterialShade',
    'name': 'window Shade',
    'solar_transmittance': 0.4,
    'solar_reflectance': 0.4,
    'visible_transmittance': 0.4,
    'visible_reflectance': 0.4,
    'infrared_hemispherical_emissivity': 0.9,
    'infrared_transmittance': 0,
    'thickness': 0.005,
    'conductivity': 0.1,
    'shade_toglass_distance': 0.05,
    'top_opening_multiplier': 0,
    'bottom_opening_multiplier': 0,
    'left_opening_multiplier': 0,
    'right_opening_multiplier': 0,
    'airflow_permeability': 0
}

construction_internal_floor = {
    'type': 'EnergyConstructionOpaque',
    'name': 'Internal Floor',
    'materials': [in_material_no_mass, in_material_internalsource, in_material_concrete]
}

construction_window = {
    'type': 'EnergyConstructionTransparent',
    'name': 'Exterior Window',
    'materials': [in_window_glazing, in_window_air_gap, in_window_glazing]
}

construction_window_blind = {
    'type': 'EnergyConstruction',
    'name': 'Window with Blinds',
    'materials': [in_window_blind, in_window_simpleglazing]
}
