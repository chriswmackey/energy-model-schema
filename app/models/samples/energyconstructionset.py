construction_set = {
    'type': 'ConstructionSet', 
    'name': 'Construction Set 1', 
    'wall_set': {
        'type': 'WallSet',
        'exterior_wall': {
            'type': 'EnergyConstructionOpaque',
            'name': 'Exterior Wall ASHRAE 2009',
            'materials': [
                {
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
                }, 
                {
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
                },
                {
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
                },
                {
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
            ]
        }
    },
    'floor_set': {
        'type': 'FloorSet',
        'interior_floor': {
            'type': 'EnergyConstructionOpaque',
            'name': 'Internal Floor',
            'materials': [
                {
                    'type': 'EnergyMaterialNoMass',
                    'name': 'CP02 Carpet Pad',
                    'r_value': 0.9,
                    'roughness': 'Smooth',
                    'thermal_absorptance': 0.8,
                    'solar_absorptance': 0.8,
                    'visible_absorptance': 0.8
                },
                {
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
                },
                {
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
            ]
        }
    },
    'roof_ceiling_set': {
        'type': 'RoofCeilingSet',
        'exterior_roof': {
            'type': 'EnergyConstructionOpaque',
            'name': 'Exterior Roof ASHRAE 2009',
            'materials': [
                {
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
                },
                {
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
                },
                {
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
            ]
        }
    },
    'aperture_set': {
        'type': 'ApertureSet',
        'fixed_window': {
            'type': 'EnergyConstructionTransparent',
            'name': 'Exterior Window',
            'materials': [
                {
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
                },
                {
                    'type': 'EnergyWindowMaterialGas',
                    'name': 'Air 13mm',
                    'gas_type': 'Air',
                    'thickness': 0.0127
                },
                {
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
            ]
        }
    }
}