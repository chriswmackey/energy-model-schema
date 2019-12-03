material_gypsum = {
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

material_stucco = {
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

material_insulation = {
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

material_concrete = {
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

material_no_mass = {
    'type': 'EnergyMaterialNoMass',
    'name': 'CP02 Carpet Pad',
    'r_value': 0.9,
    'roughness': 'Smooth',
    'thermal_absorptance': 0.8,
    'solar_absorptance': 0.8,
    'visible_absorptance': 0.8
}

material_roof_membrane = {
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

material_roof_insulation = {
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

material_metal_decking = {
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

window_gas = {
    'type': 'EnergyWindowMaterialGas',
    'name': 'Air 13mm',
    'gas_type': 'Air',
    'thickness': 0.0127
}

window_gas_mixture = {
    'type': 'EnergyWindowMaterialGasMixture',
    'name': 'Gas Mixture',
    'thickness': 0.003,
    'gas_type_fraction': [
        {
            'gas_type': 'Air',
            'gas_fraction': 0.97
        },
        {
            'gas_type': 'Argon',
            'gas_fraction': 0.02
        },
        {
            'gas_type': 'Krypton',
            'gas_fraction': 0.01
        }
    ]
}

window_gas_custom = {
    'type': 'EnergyWindowMaterialGasCustom',
    'name': 'Custom Gas',
    'thickness': 0.0125,
    'conductivity_coeff_a': 1,
    'viscosity_coeff_a': 1,
    'specific_heat_coeff_a': 1,
    'specific_heat_ratio': 2,
    'molecular_weight': 20
}

window_simpleglazing = {
    'type': 'EnergyWindowMaterialSimpleGlazSys',
    'name': 'Fixed Window 2.00 0.40 0.31',
    'u_factor': 1.98,
    'shgc': 0.4
}

window_blind = {
    'type': 'EnergyWindowMaterialBlind',
    'name': 'Window Material Blind 1',
    'slat_orientation': 'Horizontal',
}

window_glazing = {
    'type': 'EnergyWindowMaterialGlazing',
    'name': 'Theoretical Glass 167',
    'thickness': 0.029,
    'solar_transmittance': 0.2374,
    'solar_reflectance': 0.7126,
    'solar_reflectance_back': 0,
    'visible_transmittance': 0.2512,
    'visible_reflectance': 0.6988,
    'visible_reflectance_back': 0,
    'infrared_transmittance': 0,
    'emissivity': 0.985,
    'emissivity_back': 0.985,
    'conductivity': 2.1073,
    'dirt_correction': 1,
    'solar_diffusing': False
}

window_shade = {
    'type': 'EnergyWindowMaterialShade',
    'name': 'window Shade',
    'thickness': 0.005,

}

construction_internal_floor = {
    'type': 'OpaqueConstruction',
    'name': 'Internal Floor',
    'layers': ['CP02 Carpet Pad', 'Internal Source', '8in Concrete HW'],
    'materials': [material_no_mass, material_concrete]
}

construction_window = {
    'type': 'WindowConstruction',
    'name': 'Exterior Window',
    'layers': ['Theoretical Glass 167', 'Air 13mm', 'Theoretical Glass 167'],
    'materials': [window_glazing, window_gas, window_glazing]
}

construction_window2 = {
    'type': 'WindowConstruction',
    'name': 'Exterior Window - Gas Mixture',
    'layers': ['Theoretical Glass 167',  'Gas Mixture', 'Theoretical Glass 167'],
    'materials': [window_glazing, window_gas_mixture, window_glazing]
}

construction_window_blind = {
    'type': 'WindowConstruction',
    'name': 'Window with Blinds',
    'layers': ['Window Material Blind 1', 'Fixed Window 2.00 0.40 0.31'],
    'materials': [window_blind, window_simpleglazing]
}

construction_wall = {
    'type': 'OpaqueConstruction',
    'name': 'Exterior Wall ASHRAE 2009',
    'layers': ['1 in Gypsum', '8in Concrete HW', 'Wall Insulation', '1.5 in Gypsum'],
    'materials': [material_stucco, material_concrete, material_insulation, material_gypsum]
}

construction_roof = {
    'type': 'OpaqueConstruction',
    'name': 'Exterior Roof ASHRAE 2009',
    'layers': ['Metal Surface', 'Insulation Board'],
    'materials': [material_roof_membrane, material_roof_insulation, material_metal_decking]
}
