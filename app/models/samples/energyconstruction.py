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

in_material_gypsum = {
    'type': 'EnergyMaterial',
    'name': '1.5 in Gypsum',
    'roughness': 'Smooth',
    'thickness': 0.012,
    'conductivity': 0.16,
    'density': 784.9,
    'specific_heat': 830,
    'thermal_absorptance': 0.9,
    'solar_absorptance': 0.4,
    'visible_absorptance': 0.4
}

in_material_stucco = {
    'type': 'EnergyMaterial',
    'name': '1 in Gypsum',
    'roughness': 'Smooth',
    'thickness': 0.025,
    'conductivity': 0.69,
    'density': 1858,
    'specific_heat': 836.9,
    'thermal_absorptance': 0.9,
    'solar_absorptance': 0.92,
    'visible_absorptance': 0.92
}

in_material_insulation = {
    'type': 'EnergyMaterial',
    'name': 'Wall Insulation',
    'roughness': 'MediumRough',
    'thickness': 0.033,
    'conductivity': 0.0432,
    'density': 91,
    'specific_heat': 836.9,
    'thermal_absorptance': 0.9,
    'solar_absorptance': 0.5,
    'visible_absorptance': 0.5
}

in_material_concrete = {
    'type': 'EnergyMaterial',
    'name': '8in Concrete HW',
    'roughness': 'MediumRough',
    'thickness': 0.20,
    'conductivity': 1.72,
    'density': 2242,
    'specific_heat': 836,
    'thermal_absorptance': 0.9,
    'solar_absorptance': 0.65,
    'visible_absorptance': 0.65
}

in_material_no_mass = {
    'type': 'EnergyMaterialNoMass',
    'name': 'CP02 Carpet Pad',
    'r_value': 0.9,
    'roughness': 'Smooth',
    'thermal_absorptance': 0.8,
    'solar_absorptance': 0.8,
    'visible_absorptance': 0.8
}

in_material_roof_membrane = {
    'type': 'EnergyMaterial',
    'name': 'Roof Membrane',
    'roughness': 'VeryRough',
    'thickness': 0.0095,
    'conductivity': 0.16,
    'density': 1121.29,
    'specific_heat': 1460,
    'thermal_absorptance': 0.9,
    'solar_absorptance': 0.7,
    'visible_absorptance': 0.7
}

in_material_roof_insulation = {
    'type': 'EnergyMaterial',
    'name': 'Roof Insulation',
    'roughness': 'MediumRough',
    'thickness': 0.1693,
    'conductivity': 0.049,
    'density': 265,
    'specific_heat': 836.8,
    'thermal_absorptance': 0.9,
    'solar_absorptance': 0.7,
    'visible_absorptance': 0.7
}

in_material_metal_decking = {
    'type': 'EnergyMaterial',
    'name': 'Metal Decking',
    'roughness': 'MediumSmooth',
    'thickness': 0.0015,
    'conductivity': 45,
    'density': 7680,
    'specific_heat': 418.4,
    'thermal_absorptance': 0.9,
    'solar_absorptance': 0.6,
    'visible_absorptance': 0.6
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
    'dirt_correction': 1,
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
    'materials': []
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

construction_wall = {
    'type': 'EnergyConstructionOpaque',
    'name': 'Exterior Wall ASHRAE 2009',
    'materials': [in_material_stucco, in_material_concrete, in_material_insulation, in_material_gypsum]
}

construction_roof = {
    'type': 'EnergyConstructionOpaque',
    'name': 'Exterior Roof ASHRAE 2009',
    'materials': [in_material_roof_membrane, in_material_roof_insulation, in_material_metal_decking]
}

construction_window_wrong = {
    'type': 'EnergyConstructionTransparent',
    'name': 'Wrong Window',
    'materials': [in_window_air_gap, in_window_glazing, in_window_glazing]
}
