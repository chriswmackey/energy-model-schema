program_set = {
    'type': 'ProgramSet',
    'name': 'Program Set',
    'people': {
        'type': 'People',
        'name': 'People Definition',
        'people_per_area': 0.35,
        'occupancy_schedule': {
            'type': 'ScheduleFixedInterval',
            'name': 'Schedule-People Occupancy',
            'start_date': {
                'month': 1,
                'day': 1,
                'is_leap_year': False,
            },
            'values': [0, 0, 0, 0, 0, 0, 0, 0.55, 0.55, 1, 1, 1, 1, 1, 0.55, 0.55, 0.55, 0.55, 0.10, 0.10, 0, 0, 0, 0]
        },
        'activity_schedule': {
            'type': 'ScheduleFixedInterval',
            'name': 'Schedule-People Activity',
            'start_date': {
                'month': 1,
                'day': 1,
                'is_leap_year': False,
            },
            'values': [117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117]
        },
    },
    'lighting': {
        'type': 'Lighting',
        'name': 'Lighting Definition',
        'lighting_per_area': 17,
        'schedule': {
            'type': 'ScheduleFixedInterval',
            'name': 'Schedule-Lighting',
            'start_date': {
                'month': 1,
                'day': 1,
                'is_leap_year': False
            },
            'values': [0, 0, 0, 0, 0, 0, 0, 0.55, 0.55, 1, 1, 1, 1, 1, 0.55, 0.55, 0.55, 0.55, 0.10, 0.10, 0, 0, 0, 0]
        }
    },
    'electrical_equipment': {
        'type': 'ElectricalEquipment',
        'name': 'Electrical Equipment Definition',
        'equipment_per_area': 12.5,
        'schedule': {
            'type': 'ScheduleFixedInterval',
            'name': 'Schedule-Equipment',
            'start_date': {
                'month': 1,
                'day': 1,
                'is_leap_year': False
            },
            'values': [0.05, 0.05, 0.05, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.8, 1, 1, 1, 1, 1, 0.55, 0.55, 0.35, 0.35, 0.35, 0, 0, 0, 0]
        }
    }
}

people = {
    'type': 'People',
    'name': 'People Definition',
    'people_per_area': 0.35,
    'occupancy_schedule': {
            'type': 'ScheduleFixedInterval',
            'name': 'Schedule-People Occupancy',
            'start_date': {
                'month': 1,
                'day': 1,
                'is_leap_year': False,
            },
        'values': [0, 0, 0, 0, 0, 0, 0, 0.55, 0.55, 1, 1, 1, 1, 1, 0.55, 0.55, 0.55, 0.55, 0.10, 0.10, 0, 0, 0, 0]
    },
    'activity_schedule': {
        'type': 'ScheduleFixedInterval',
        'name': 'Schedule-People Activity',
        'start_date': {
                'month': 1,
                'day': 1,
                'is_leap_year': False,
        },
        'values': [117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117, 117]
    },
}

lighting = {
    'type': 'Lighting',
    'name': 'Lighting Definition',
    'lighting_per_area': 17,
    'schedule': {
            'type': 'ScheduleFixedInterval',
            'name': 'Schedule-Lighting',
            'start_date': {
                'month': 1,
                'day': 1,
                'is_leap_year': False
            },
        'values': [0, 0, 0, 0, 0, 0, 0, 0.55, 0.55, 1, 1, 1, 1, 1, 0.55, 0.55, 0.55, 0.55, 0.10, 0.10, 0, 0, 0, 0]
    }
}

electrical_equipment = {
    'type': 'ElectricalEquipment',
    'name': 'Electrical Equipment Definition',
    'equipment_per_area': 12.5,
    'schedule': {
            'type': 'ScheduleFixedInterval',
            'name': 'Schedule-Equipment',
            'start_date': {
                'month': 1,
                'day': 1,
                'is_leap_year': False
            },
        'values': [0.05, 0.05, 0.05, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.8, 1, 1, 1, 1, 1, 0.55, 0.55, 0.35, 0.35, 0.35, 0, 0, 0, 0]
    }
}
