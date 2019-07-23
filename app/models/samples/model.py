model_sample = {
    "convert_to_meters": 1,
    "type": "Model",
    "name": "face_by_face_model",
    "faces": [
        {
            "name": "floor",
            "face_type": "Floor",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone", 
			},
            "rad_modifier": {
                "modifier": "void",
                "type": "Plastic",
                "name": "generic_floor",
                "r_reflectance": 0.2,
                "g_reflectance": 0.2,
                "b_reflectance": 0.2,
                "specularity": 0,
                "roughness": 0
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 0,
                    "y": 0,
                    "z": 3.2
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 3.2
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 3.2
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 3.2
                }
            ],
            "energy_construction_opaque": {
                "type": "OpaqueConstruction",
                "name": "construction_internal_floor",
                "materials": [
                    {
                        "type": "EnergyMaterialNoMass",
                        "name": "CP02 Carpet Pad",
                        "r_value": 0.9,
                        "roughness": "Smooth",
                        "thermal_absorptance": 0.8,
                        "solar_absorptance": 0.8,
                        "visible_absorptance": 0.8 
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "Internal Source", 
                        "roughness": "Smooth",
                        "thickness": 0.012,
                        "conductivity": 0.6,
                        "density": 1000,
                        "specific_heat": 4185,
                        "thermal_absorptance": 0.95,
                        "solar_absorptance": 0.7
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "8in Concrete HW",
                        "roughness": "MediumRough",
                        "thickness": 0.20,
                        "conductivity": 1.72,
                        "density": 2242,
                        "specific_heat": 836,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.65,
                        "visible_absorptance": 0.65                    
                    }
                ]

            }
        },
        {
            "name": "ceiling",
            "face_type": "RoofCeiling",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "rad_modifier": {
                "modifier": "void",
                "type": "Plastic",
                "name": "generic_roof",
                "r_reflectance": 0.8,
                "g_reflectance": 0.8,
                "b_reflectance": 0.8,
                "specularity": 0,
                "roughness": 0
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 0,
                    "y": 0,
                    "z": 7.4
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 7.4
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 7.4
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 7.4
                }
            ],
            "energy_construction_opaque": {
                "type": "OpaqueConstruction", 
                "name": "Exterior Roof ASHRAE 2009",
                "materials": [
                    {
                        "type": "EnergyMaterial",
                        "name": "Roof Membrane",
                        "roughness": "VeryRough",
                        "thickness": 0.0095,
                        "conductivity": 0.16,
                        "density": 1121.29,
                        "specific_heat": 1460,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.7,
                        "visible_absorptance": 0.7
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "Roof Insulation",
                        "roughness": "MediumRough",
                        "thickness": 0.1693,
                        "conductivity": 0.049,
                        "density": 265,
                        "specific_heat": 836.8,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.7,
                        "visible_absorptance": 0.7
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "Metal Decking",
                        "roughness": "MediumSmooth",
                        "thickness": 0.0015,
                        "conductivity": 45,
                        "density": 7680,
                        "specific_heat": 418.4,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.6,
                        "visible_absorptance": 0.6
                    }
                ]
            }
        },
        {
            "name": "back_wall",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "face_type": "Wall",
            "rad_modifier": {
                "modifier": "void",
                "type": "Plastic",
                "name": "generic_wall",
                "r_reflectance": 0.5,
                "g_reflectance": 0.5,
                "b_reflectance": 0.5,
                "specularity": 0,
                "roughness": 0
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 0,
                    "y": 0,
                    "z": 3.2
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 3.2
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 7.4
                },
                {
                    "x": 0,
                    "y": 0,
                    "z": 7.4
                }
            ],
            "energy_construction_opaque": {
                "type": "OpaqueConstruction",
                "name": "construction_internal_floor",
                "materials": [
                    {
                        "type": "EnergyMaterialNoMass",
                        "name": "CP02 Carpet Pad",
                        "r_value": 0.9,
                        "roughness": "Smooth",
                        "thermal_absorptance": 0.8,
                        "solar_absorptance": 0.8,
                        "visible_absorptance": 0.8 
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "Internal Source", 
                        "roughness": "Smooth",
                        "thickness": 0.012,
                        "conductivity": 0.6,
                        "density": 1000,
                        "specific_heat": 4185,
                        "thermal_absorptance": 0.95,
                        "solar_absorptance": 0.7
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "8in Concrete HW",
                        "roughness": "MediumRough",
                        "thickness": 0.20,
                        "conductivity": 1.72,
                        "density": 2242,
                        "specific_heat": 836,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.65,
                        "visible_absorptance": 0.65                    
                    }
                ]
            },
            "apertures": [
                {
                    "name": "back_glazing",
                    "face_type": "Window",
                    "type": "Aperture",
                    "rad_modifier": {
                        "modifier": "void",
                        "type": "Glass",
                        "name": "generic_glass",
                        "r_transmittance": 0.6,
                        "g_transmittance": 0.6,
                        "b_transmittance": 0.6,
                        "refraction_index": 1.52
                    },
                    "vertices": [
                        {
                            "x": 0.7778174593052024,
                            "y": 0.7778174593052023,
                            "z": 3.9000000000000004
                        },
                        {
                            "x": 2.1920310216782974,
                            "y": 2.192031021678297,
                            "z": 3.9000000000000004
                        },
                        {
                            "x": 2.1920310216782974,
                            "y": 2.192031021678297,
                            "z": 5.9
                        },
                        {
                            "x": 0.7778174593052024,
                            "y": 0.7778174593052023,
                            "z": 5.9
                        }
                    ],
                    "energy_construction_transparent": {
                        "type": "EnergyConstructionTransparent",
                        "name": "Exterior Window",
                        "materials": [
                            {
                                "type": "EnergyWindowMaterialGlazing",
                                "name": "Theoretical Glass 167",
                                "thickness": 0.029,
                                "solar_transmittance": 0.2374,
                                "solar_reflectance": 0.7126,
                                "solar_reflectance_back": 0,
                                "visible_transmittance": 0.2512,
                                "visible_reflectance": 0.6988,
                                "visible_reflectance_back": 0,
                                "infrared_transmittance": 0,
                                "emissivity": 0.985,
                                "emissivity_back": 0.985,
                                "conductivity": 2.1073,
                                "dirt_correlation": 1,
                                "solar_diffusing": "No"
                            },
                            {
                                "type": "EnergyWindowMaterialGas",
                                "name": "Air 13mm",
                                "gas_type": "Air",
                                "thickness": 0.0127
                            },
                            {
                                "type": "EnergyWindowMaterialGlazing",
                                "name": "Theoretical Glass 167",
                                "thickness": 0.029,
                                "solar_transmittance": 0.2374,
                                "solar_reflectance": 0.7126,
                                "solar_reflectance_back": 0,
                                "visible_transmittance": 0.2512,
                                "visible_reflectance": 0.6988,
                                "visible_reflectance_back": 0,
                                "infrared_transmittance": 0,
                                "emissivity": 0.985,
                                "emissivity_back": 0.985,
                                "conductivity": 2.1073,
                                "dirt_correlation": 1,
                                "solar_diffusing": "No"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "name": "right_wall",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "face_type": "Wall",
            "rad_modifier": {
                "modifier": "void",
                "type": "Plastic",
                "name": "generic_wall",
                "r_reflectance": 0.5,
                "g_reflectance": 0.5,
                "b_reflectance": 0.5,
                "specularity": 0,
                "roughness": 0
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 3.2
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 3.2
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 7.4
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 7.4
                }
            ],
            "energy_construction_opaque": {
                "type": "OpaqueConstruction",
                "name": "Exterior Wall ASHRAE 2009",
                "materials": [
                    {
                        "type": "EnergyMaterial",
                        "name": "1 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.025,
                        "conductivity": 0.69,
                        "density": 1858,
                        "specific_heat": 836.9,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.92,
                        "visible_absorptance": 0.92
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "8in Concrete HW",
                        "roughness": "MediumRough",
                        "thickness": 0.20,
                        "conductivity": 1.72,
                        "density": 2242,
                        "specific_heat": 836,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.65,
                        "visible_absorptance": 0.65
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "1 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.025,
                        "conductivity": 0.69,
                        "density": 1858,
                        "specific_heat": 836.9,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.92,
                        "visible_absorptance": 0.92
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "1.5 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.012,
                        "conductivity": 0.16,
                        "density": 784.9,
                        "specific_heat": 830,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.4,
                        "visible_absorptance": 0.4
                    }
                ]

            }
        },
        {
            "name": "front_wall",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "face_type": "Wall",
            "rad_modifier": {
                "modifier": "void",
                "type": "Opaque",
                "name": "generic_wall",
                "reflectance": 0.5
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 3.2
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 3.2
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 7.4
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 7.4
                }
            ],
            "energy_construction_opaque": {
                "type": "OpaqueConstruction",
                "name": "Exterior Wall ASHRAE 2009",
                "materials": [
                    {
                        "type": "EnergyMaterial",
                        "name": "1 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.025,
                        "conductivity": 0.69,
                        "density": 1858,
                        "specific_heat": 836.9,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.92,
                        "visible_absorptance": 0.92
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "8in Concrete HW",
                        "roughness": "MediumRough",
                        "thickness": 0.20,
                        "conductivity": 1.72,
                        "density": 2242,
                        "specific_heat": 836,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.65,
                        "visible_absorptance": 0.65
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "1 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.025,
                        "conductivity": 0.69,
                        "density": 1858,
                        "specific_heat": 836.9,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.92,
                        "visible_absorptance": 0.92
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "1.5 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.012,
                        "conductivity": 0.16,
                        "density": 784.9,
                        "specific_heat": 830,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.4,
                        "visible_absorptance": 0.4
                    }
                ]

            }
        },
        {
            "name": "left_wall",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "face_type": "Wall",
            "rad_modifier": {
                "modifier": "void",
                "type": "Opaque",
                "name": "generic_wall",
                "reflectance": 0.5
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 0,
                    "y": 0,
                    "z": 3.2
                },
                {
                    "x": 0,
                    "y": 0,
                    "z": 7.4
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 7.4
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 3.2
                }
            ],
            "energy_construction_opaque": {
                "type": "OpaqueConstruction",
                "name": "Exterior Wall ASHRAE 2009",
                "materials": [
                    {
                        "type": "EnergyMaterial",
                        "name": "1 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.025,
                        "conductivity": 0.69,
                        "density": 1858,
                        "specific_heat": 836.9,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.92,
                        "visible_absorptance": 0.92
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "8in Concrete HW",
                        "roughness": "MediumRough",
                        "thickness": 0.20,
                        "conductivity": 1.72,
                        "density": 2242,
                        "specific_heat": 836,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.65,
                        "visible_absorptance": 0.65
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "1 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.025,
                        "conductivity": 0.69,
                        "density": 1858,
                        "specific_heat": 836.9,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.92,
                        "visible_absorptance": 0.92
                    },
                    {
                        "type": "EnergyMaterial",
                        "name": "1.5 in Gypsum",
                        "roughness": "Smooth",
                        "thickness": 0.012,
                        "conductivity": 0.16,
                        "density": 784.9,
                        "specific_heat": 830,
                        "thermal_absorptance": 0.9,
                        "solar_absorptance": 0.4,
                        "visible_absorptance": 0.4
                    }
                ]

            }
        }
    ]
}
