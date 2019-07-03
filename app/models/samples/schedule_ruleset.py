schedule_ruleset = {
    'type': 'scheduleruleset',
    'name': 'Schedule Ruleset',
    'schedule_type_limits': {
        'type': 'ScheduleTypeLimits',
        'numeric_type': {
            'numeric_type': {
                'type': 'ScheduleContinuous'
            }
        },
        'unit_type': 'Temperature',
        'name': 'Numeric Type',
        'lower_limit_value': 0,
        'upper_limit_value': 20
    },
    'default_day_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 1',
        'interpolate_to_timestep': False,
        'day_values': [
                {
                    'time': {
                        'hour': 24,
                        'minute': 00
                    },
                    'value_until_time': 20
                }
        ],
    },
    'summer_designday_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 2',
        'interpolate_to_timestep': False,
        'day_values': [
                {
                    'time': {
                        'hour': 24,
                        'minute': 00
                    },
                    'value_until_time': 20
                }
        ],
    },
    'winter_designday_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 3',
        'interpolate_to_timestep': False,
        'day_values': [
                {
                    'time': {
                        'hour': 24,
                        'minute': 00
                    },
                    'value_until_time': 20
                }
        ]
    },
    'schedule_rules': [
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Default Day 4',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 20
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 2,
                    'day': 45,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00
                }
            },
            'end_period': {
                'date': {
                    'month': 12,
                    'day': 31,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 59
                },
            },
            'name': 'Schedule Rule 1',
            'apply_sunday': True,
            'apply_monday': True,
            'apply_tuesday': True,
            'apply_wednesday': True,
            'apply_thursday': True,
            'apply_friday': True,
            'apply_saturday': True,
            'apply_holiday': True
        }
    ]
}

schedule_ruleset_1 = {
    'type': 'scheduleruleset',
    'name': 'Schedule Ruleset 1',
    'schedule_type_limits': {
        'type': 'ScheduleTypeLimits',
        'numeric_type': {
            'numeric_type': {
                'type': 'ScheduleContinuous'
            }
        },
        'unit_type': 'Dimensionless',
        'name': 'Numeric Type',
        'lower_limit_value': 0,
        'upper_limit_value': 1
    },
    'default_day_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 1',
        'interpolate_to_timestep': False,
        'day_values': [
                {
                    'time': {
                        'hour': 7,
                        'minute': 00
                    },
                    'value_until_time': 0
                },
            {
                    'time': {
                        'hour': 19,
                        'minute': 00
                    },
                    'value_until_time': 1
            },
            {
                    'time': {
                        'hour': 24,
                        'minute': 00
                    },
                    'value_until_time': 0
            }
        ]
    },
    'summer_designday_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 2',
        'interpolate_to_timestep': False,
        'day_values': [
                {
                    'time': {
                        'hour': 24,
                        'minute': 00
                    },
                    'value_until_time': 0
                }
        ]
    },
    'winter_designday_schedule': {
        'type': 'ScheduleDay',
        'name': 'Default Day 3',
        'interpolate_to_timestep': False,
        'day_values': [
                {
                    'time': {
                        'hour': 24,
                        'minute': 00
                    },
                    'value_until_time': 0
                }
        ]
    },
    'schedule_rules': [
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 180 Day 1',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 0
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 8,
                    'day': 17,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00
                },
            },
            'end_period': {
                'date': {
                    'month': 12,
                    'day': 11,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 00
                },
            },
            'name': 'Schedule Rule 180',
            'apply_sunday': True,
            'apply_monday': False,
            'apply_tuesday': False,
            'apply_wednesday': False,
            'apply_thursday': False,
            'apply_friday': False,
            'apply_saturday': False,
            'apply_holiday': False
        },
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 181 Day 2',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 7,
                                'minute': 00
                            },
                            'value_until_time': 0
                        },
                        {
                            'time': {
                                'hour': 16,
                                'minute': 00
                            },
                            'value_until_time': 0.3
                        },
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 0
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 8,
                    'day': 17,
                },
                'time': {
                    'hour': 0,
                    'minute': 00
                },
            },
            'end_period': {
                'date': {
                    'month': 12,
                    'day': 11
                },
                'time': {
                    'hour': 24,
                    'minute': 00,
                },
            },
            'name': 'Schedule Rule 181',
            'apply_sunday': False,
            'apply_monday': False,
            'apply_tuesday': False,
            'apply_wednesday': False,
            'apply_thursday': False,
            'apply_friday': False,
            'apply_saturday': True,
            'apply_holiday': False
        },
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 182 Day',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 7,
                                'minute': 00
                            },
                            'value_until_time': 0
                        },
                        {
                            'time': {
                                'hour': 19,
                                'minute': 00
                            },
                            'value_until_time': 1
                        },
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00,
                            },
                            'value_until_time': 0
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 8,
                    'day': 17,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00
                },
            },
            'end_period': {
                'date': {
                    'month': 12,
                    'day': 11,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 00
                },
            },
            'name': 'Schedule Rule 182',
            'apply_sunday': False,
            'apply_monday': True,
            'apply_tuesday': True,
            'apply_wednesday': True,
            'apply_thursday': True,
            'apply_friday': True,
            'apply_saturday': False,
            'apply_holiday': False
        },
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 183 Day',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 0
                        }
                    ],
            },
            'start_period': {
                'date': {
                    'month': 4,
                    'day': 13,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00
                },
                'is_leap_year': False
            },
            'end_period': {
                'date': {
                    'month': 6,
                    'day': 12,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 00,
                },
                'is_leap_year': False
            },
            'name': 'Schedule Rule 183',
            'apply_sunday': True,
            'apply_monday': False,
            'apply_tuesday': False,
            'apply_wednesday': False,
            'apply_thursday': False,
            'apply_friday': False,
            'apply_saturday': False,
            'apply_holiday': False
        },
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 184 Day',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 7,
                                'minute': 00
                            },
                            'value_until_time': 0,
                        },
                        {
                            'time': {
                                'hour': 16,
                                'minute': 00
                            },
                            'value_until_time': 0.29
                        },
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 0
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 4,
                    'day': 13,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00,
                },
            },
            'end_period': {
                'date': {
                    'month': 6,
                    'day': 12,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 00,
                },
            },
            'name': 'Schedule Rule 184',
            'apply_sunday': False,
            'apply_monday': False,
            'apply_tuesday': False,
            'apply_wednesday': False,
            'apply_thursday': False,
            'apply_friday': False,
            'apply_saturday': True,
            'apply_holiday': False
        },
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 185 Day',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 7,
                                'minute': 00
                            },
                            'value_until_time': 0
                        },
                        {
                            'time': {
                                'hour': 20,
                                'minute': 00
                            },
                            'value_until_time': 0.57
                        },
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 0
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 4,
                    'day': 13,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00,
                },
            },
            'end_period': {
                'date': {
                    'month': 6,
                    'day': 12,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 00,
                },
            },
            'name': 'Schedule Rule 185',
            'apply_sunday': False,
            'apply_monday': True,
            'apply_tuesday': True,
            'apply_wednesday': True,
            'apply_thursday': True,
            'apply_friday': True,
            'apply_saturday': False,
            'apply_holiday': False
        },
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 186 Day',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 0
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 1,
                    'day': 5,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00,
                },
            },
            'end_period': {
                'date': {
                    'month': 4,
                    'day': 3,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 00,
                },
            },
            'name': 'Schedule Rule 186',
            'apply_sunday': True,
            'apply_monday': False,
            'apply_tuesday': False,
            'apply_wednesday': False,
            'apply_thursday': False,
            'apply_friday': False,
            'apply_saturday': False,
            'apply_holiday': False
        },
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 187 Day',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 7,
                                'minute': 00
                            },
                            'value_until_time': 0
                        },
                        {
                            'time': {
                                'hour': 16,
                                'minute': 00
                            },
                            'value_until_time': 0.29
                        },
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 0
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 1,
                    'day': 5,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00,
                },
            },
            'end_period': {
                'date': {
                    'month': 4,
                    'day': 3,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 00,
                },
            },
            'name': 'Schedule Rule 187',
            'apply_sunday': False,
            'apply_monday': False,
            'apply_tuesday': False,
            'apply_wednesday': False,
            'apply_thursday': False,
            'apply_friday': False,
            'apply_saturday': True,
            'apply_holiday': False
        },
        {
            'type': 'ScheduleRule',
            'schedule_day': {
                    'type': 'ScheduleDay',
                    'name': 'Schedule Rule 188 Day',
                    'interpolate_to_timestep': False,
                    'day_values': [
                        {
                            'time': {
                                'hour': 7,
                                'minute': 00
                            },
                            'value_until_time': 0
                        },
                        {
                            'time': {
                                'hour': 18,
                                'minute': 00
                            },
                            'value_until_time': 0.57
                        },
                        {
                            'time': {
                                'hour': 24,
                                'minute': 00
                            },
                            'value_until_time': 0
                        }
                    ]
            },
            'start_period': {
                'date': {
                    'month': 1,
                    'day': 5,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 0,
                    'minute': 00,
                },
            },
            'end_period': {
                'date': {
                    'month': 4,
                    'day': 3,
                    'is_leap_year': False
                },
                'time': {
                    'hour': 24,
                    'minute': 00,
                },
            },
            'name': 'Schedule Rule 188',
            'apply_sunday': False,
            'apply_monday': True,
            'apply_tuesday': True,
            'apply_wednesday': True,
            'apply_thursday': True,
            'apply_friday': True,
            'apply_saturday': False,
            'apply_holiday': False
        }
    ]
}
