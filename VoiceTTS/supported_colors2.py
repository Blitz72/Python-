# Color values can be found here: https://en.wikipedia.org/wiki/List_of_colors_(compact)

# RGB color values given in tuples are (R, G, B)

# tcs34725 color temperature equation y = 0.6091(x) + 986.41, where x = CCT value spoken to the voice agent
# and y = calculated sensor value to verify with (values around 5000 deg. K will be less than sensor reading).
# TCS34725 sesnor gain is set at 4.

# tcs_color_100 values are tcs.rgb_bytes values taken at 100% brightness and sensor gain set to 60.

# lux_coeff are (b0, b1, b2) where f(brightness) = b2*x^2 + b1*x + b0

supported_colors_list = [
    {
        'name': 'alice blue',
        'google': {
            'is_rgb': True,
            'color_values': (240, 248, 255),
            'tsl_brt_100': 16100,
            'tcs_color_100': (31, 22, 31),
            'lux_coeff': (2497, 164.67, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 248, 255),
            'tsl_brt_100': 16300,
            'tcs_color_100': (33, 21, 30),
            'lux_coeff': (2497, 164.67, 0)
        }
    },
    # {
    #     'name': 'almond',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (239, 222, 205),
    #         'tsl_brt_100': None,
    #         'lux_coeff': (None, None, None)
    #     },
    #     # 'alexa': {
    #     #     'is_rgb': True,
    #     #     'color_values': (0, 0, 0),
    #     #     'tsl_brt_100': None,
    #     #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     # }
    # },
    {
        'name': 'antique white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5500,
            'tsl_brt_100': 70800,
            'tcs_color_100': 4380,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 235, 215),
            'tsl_brt_100': 16500,
            'tcs_color_100': (30, 20, 41),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'aqua',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tsl_brt_100': 15200,
            'tcs_color_100': (0, 57, 90),
            'lux_coeff': (487.98, 229.39, -0.7593)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tsl_brt_100': 15200,
            'tcs_color_100': (0, 57, 90),
            'lux_coeff': (487.98, 229.39, -0.7593)
        }
    },
    {
        'name': 'aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (127, 255, 212),
            'tsl_brt_100': 15600,
            'tcs_color_100': (17, 35, 29),
            'lux_coeff': (2640, 157.81, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 212),
            'tsl_brt_100': 15600,
            'tcs_color_100': (17, 34, 27),
            'lux_coeff': (2640, 157.81, 0)
        }
    },
    {
        'name': 'azure',
        'google': {
            'is_rgb': True,
            'color_values': (0, 127, 255),
            'tsl_brt_100': 15300,
            'tcs_color_100': (0, 46, 128),
            'lux_coeff': (1925, 155, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 255, 255),
            'tsl_brt_100': 16300,
            'tcs_color_100': (32, 23, 30),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'beige',              # Google uses cct for this color
    #     'google': {
    #         'is_rgb': False,
    #         'color_values': 5000,
    #         'tsl_brt_100': 71300,
    #         'tcs_color_100': 4150,
    #         'lux_coeff': (None, None, None)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (245, 245, 220),
    #         'tsl_brt_100': 16400,
    #         'tcs_color_100': (27, 22, 42),
    #         'lux_coeff': (None, None, None)
    #     }
    # },
    # {
    #     'name': 'bisque',             # Google uses cct for this color
    #     # 'google': {
    #     #     'is_rgb': False,
    #     #     'color_values': '',
    #     #     'tsl_brt_100': None,
    #     #     'tcs_color_100': None,
    #     #     'lux_coeff': (None, None, None)
    #     # },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (255, 228, 196),
    #         'tsl_brt_100': 16200,
    #         'tcs_color_100': (33, 19, 38),
    #         'lux_coeff': (None, None, None)
    #     }
    # },
    # {
    #     'name': 'black',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'blanched almond',    # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': '',
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 235, 205),
            'tsl_brt_100': 16600,
            'tcs_color_100': (31, 20, 39),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 255),
            'tsl_brt_100': 15400,
            'tcs_color_100': (0, 30, 215),
            'lux_coeff': (2000, 155, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 255),
            'tsl_brt_100': 15400,
            'tcs_color_100': (0, 30, 215),
            'lux_coeff': (2000, 155, 0)
        }
    },
    {
        'name': 'blue violet',
        'google': {
            'is_rgb': True,
            'color_values': (138, 43, 226),
            'tsl_brt_100': 16300,
            'tcs_color_100': (17, 16, 119),
            'lux_coeff': (1450, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (138, 43, 226),
            'tsl_brt_100': 16300,
            'tcs_color_100': (17, 16, 116),
            'lux_coeff': (1450, 175, 0)
        }
    },
    {
        'name': 'brown',
        'google': {
            'is_rgb': True,
            'color_values': (150, 75, 0),
            'tsl_brt_100': 16700,
            'tcs_color_100': (111, 9, 5),
            'lux_coeff': (1150, 190, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (165, 42, 42),
            'tsl_brt_100': 19000,
            'tcs_color_100': (172, 2, 5),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'burlywood',         # Google uses cct for this color
    #     'google': {
    #         'is_rgb': False,
    #         'color_values': '',
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     },
    #     'alexa': {
    #         'is_rgb': False,
    #         'color_values': '',
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'candlelight',       # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 2000,
            'tsl_brt_100': 41200,
            'tcs_color_100': 2200,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tsl_brt_100': 46000,
            'tcs_color_100': 2319,
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'cadet blue',
        'google': {
            'is_rgb': True,
            'color_values': (95, 158, 160),
            'tsl_brt_100': 15700,
            'tcs_color_100': (18, 32, 37),
            'lux_coeff': (1600, 170, 0)
        },
        'alexa': {                           # Need to tell Alexa to set a Full Color bulb 'to the color cadet blue'
            'is_rgb': True,
            'color_values': (95, 158, 160),
            'tsl_brt_100': 15700,
            'tcs_color_100': (18, 32, 37),
            'lux_coeff': (1600, 170, 0)
        }
    },
    {
        'name': 'chartreuse',
        'google': {
            'is_rgb': True,
            'color_values': (223, 255, 0),
            'tsl_brt_100': 16200,
            'tcs_color_100': (53, 23, 7),
            'lux_coeff': (1450, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 0),
            'tsl_brt_100': 15800,
            'tcs_color_100': (32, 33, 7),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'chocolate',
        'google': {
            'is_rgb': True,
            'color_values': (123, 63, 0),
            'tsl_brt_100': 16600,
            'tcs_color_100': (109, 9, 5),
            'lux_coeff': (1150, 190, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (210, 105, 30),
            'tsl_brt_100': 17200,
            'tcs_color_100': (132, 5, 4),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'cool',                # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': '',
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': False,
            'color_values': 7000,  # might be 6800
            'tsl_brt_100': 75100,
            'tcs_color_100': 5335,
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'cool white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 4000,
            'tsl_brt_100': 67600,
            'tcs_color_100': 3350,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 7000,
            'tsl_brt_100': 74800,
            'tcs_color_100': 5335,
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'coral',
        'google': {
            'is_rgb': True,
            'color_values': (255, 127, 80),  # need to recheck color_values
            'tsl_brt_100': 16700,
            'tcs_color_100': (120, 7, 7),
            'lux_coeff': (1000, 190, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 127, 80),  # need to recheck color_values
            'tsl_brt_100': 17000,
            'tcs_color_100': (127, 5, 6),
            'lux_coeff': (1000, 190, 0)
        }
    },
    {
        'name': 'cornflower',
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237),
            'tsl_brt_100': 15900,
            'tcs_color_100': (10, 28, 77),
            'lux_coeff': (1600, 165, 0)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # }
    },
    {
        'name': 'cornflower blue',           # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237),
            'tsl_brt_100': 15900,
            'tcs_color_100': (12, 29, 77),
            'lux_coeff': (1600, 165, 0)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # }
    },
    {
        'name': 'cornsilk',
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': 6500,
        #     'tsl_brt_100': None
        #     'tcs_value': 4850,
        #     'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 248, 220),
            'tsl_brt_100': 16400,
            'tcs_color_100': (29, 20, 40),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'crimson',
        'google': {
            'is_rgb': True,
            'color_values': (220, 20, 60),
            'tsl_brt_100': 17500,
            'tcs_color_100': (193, 1, 5),
            'lux_coeff': (900, 195, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (220, 20, 60),
            'tsl_brt_100': 17500,
            'tcs_color_100': (193, 1, 5),
            'lux_coeff': (900, 195, 0)
        }
    },
    {
        'name': 'cyan',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tsl_brt_100': 15200,
            'tcs_color_100': (0, 57, 90),
            'lux_coeff': (2623, 144.95, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tsl_brt_100': 15200,
            'tcs_color_100': (0, 57, 90),  # (0, 60, 90)
            'lux_coeff': (2623, 144.95, 0)
        }
    },
    {
        'name': 'dark blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 139),
            'tsl_brt_100': 15600,
            'tcs_color_100': (0, 30, 215),
            'lux_coeff': (2000, 155, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 139),
            'tsl_brt_100': 15600,
            'tcs_color_100': (0, 30, 214),
            'lux_coeff': (2000, 155, 0)
        }
    },
    {
        'name': 'dark cyan',
        'google': {
            'is_rgb': True,
            'color_values': (0, 139, 139),
            'tsl_brt_100': 15200,
            'tcs_color_100': (0, 57, 90),
            'lux_coeff': (2623, 144.95, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 139, 139),
            'tsl_brt_100': 15200,
            'tcs_color_100': (0, 57, 90),
            'lux_coeff': (2623, 144.95, 0)
        }
    },
    {
        'name': 'dark goldenrod',
        'google': {
            'is_rgb': True,
            'color_values': (184, 134, 11),
            'tsl_brt_100': 16500,
            'tcs_color_100': (83, 14, 6),
            'lux_coeff': (1250, 185, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (184, 134, 11),
            'tsl_brt_100': 17000,
            'tcs_color_100': (92, 11, 6),
            'lux_coeff': (1250, 185, 0)
        }
    },
    {
        'name': 'dark gray',
        'google': {
            'is_rgb': True,
            'color_values': (169, 169, 169),
            'tsl_brt_100': 16200,
            'tcs_color_100': (34, 22, 29),
            'lux_coeff': (1450, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (169, 169, 169),
            'tsl_brt_100': 16200,
            'tcs_color_100': (35, 20, 27),
            'lux_coeff': (1450, 175, 0)
        }
    },
    {
        'name': 'dark green',
        'google': {
            'is_rgb': True,
            'color_values': (1, 50, 32),
            'tsl_brt_100': 15200,
            'tcs_color_100': (12, 44, 27),
            'lux_coeff': (1750, 160, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 100, 0),
            'tsl_brt_100': 14000,
            'tcs_color_100': (0, 93, 10),
            'lux_coeff': (1750, 160, 0)
        }
    },
    {
        'name': 'dark khaki',
        'google': {
            'is_rgb': True,
            'color_values': (189, 183, 107),
            'tsl_brt_100': 16100,
            'tcs_color_100': (48, 22, 14),
            'lux_coeff': (1350, 180, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (189, 183, 107),
            'tsl_brt_100': 16500,
            'tcs_color_100': (52, 20, 12),
            'lux_coeff': (1350, 180, 0)
        }
    },
    {
        'name': 'dark magenta',
        'google': {
            'is_rgb': True,
            'color_values': (139, 0, 139),
            'tsl_brt_100': 16800,
            'tcs_color_100': (61, 8, 60),
            'lux_coeff': (1290, 185, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 0, 139),
            'tsl_brt_100': 16800,
            'tcs_color_100': (57, 7, 55),
            'lux_coeff': (1290, 185, 0)
        }
    },
    {
        'name': 'dark olive green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (86, 103, 51),
            'tsl_brt_100': 16000,
            'tcs_color_100': (39, 25, 11),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'dark orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 140, 0),
            'tsl_brt_100': 16700,
            'tcs_color_100': (103, 10, 5),
            'lux_coeff': (1150, 185, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 140, 0),
            'tsl_brt_100': 17000,
            'tcs_color_100': (109, 8, 5),
            'lux_coeff': (1150, 185, 0)
        }
    },
    {
        'name': 'dark orchid',
        'google': {
            'is_rgb': True,
            'color_values': (153, 50, 204),
            'tsl_brt_100': 16400,
            'tcs_color_100': (30, 13, 85),
            'lux_coeff': (1400, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (153, 50, 204),
            'tsl_brt_100': 16400,
            'tcs_color_100': (27, 11, 84),
            'lux_coeff': (1400, 175, 0)
        }
    },
    {
        'name': 'dark red',
        'google': {
            'is_rgb': True,
            'color_values': (139, 0, 0),
            'tsl_brt_100': 17000,
            'tcs_color_100': (245, 0, 3),
            'lux_coeff': (800, 200, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 0, 0),
            'tsl_brt_100': 17000,
            'tcs_color_100': (242, 0, 3),
            'lux_coeff': (800, 200, 0)
        }
    },
    {
        'name': 'dark salmon',
        'google': {
            'is_rgb': True,
            'color_values': (233, 150, 122),
            'tsl_brt_100': 16600,
            'tcs_color_100': (80, 11, 14),
            'lux_coeff': (1200, 185, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (233, 150, 122),
            'tsl_brt_100': 17000,
            'tcs_color_100': (84, 10, 12),
            'lux_coeff': (1200, 185, 0)
        }
    },
    {
        'name': 'dark sea green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (143, 188, 143),
            'tsl_brt_100': 16000,
            'tcs_color_100': (29, 27, 21),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'dark slate blue',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (72, 61, 139),
            'tsl_brt_100': 16500,
            'tcs_color_100': (13, 19, 89),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'dark slate gray',
        'google': {
            'is_rgb': True,
            'color_values': (47, 79, 79),
            'tsl_brt_100': 15800,
            'tcs_color_100': (19, 31, 36),
            'lux_coeff': (1600, 165, 0)
        },
        'alexa': {                            # Need to tell Alexa to set a Full Color bulb 'to the color dark slate gray'
            'is_rgb': True,
            'color_values': (47, 79, 79),
            'tsl_brt_100': 16100,
            'tcs_color_100': (19, 29, 36),
            'lux_coeff': (1600, 165, 0)
        }
    },
    {
        'name': 'dark turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (0, 206, 209),
            'tsl_brt_100': 14900,
            'tcs_color_100': (0, 55, 90),
            'lux_coeff': (1950, 150, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 210, 210),
            'tsl_brt_100': 15000,
            'tcs_color_100': (0, 54, 92),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'dark violet',
        'google': {
            'is_rgb': True,
            'color_values': (148, 0, 211),
            'tsl_brt_100': 16500,
            'tcs_color_100': (22, 12, 98),
            'lux_coeff': (1600, 170, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (148, 0, 211),
            'tsl_brt_100': 17000,
            'tcs_color_100': (22, 12, 98),
            'lux_coeff': (1600, 170, 0)
        }
    },
    {
        'name': 'daylight',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tsl_brt_100': 71400,
            'tcs_color_100': 4150,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 5500,
            'tsl_brt_100': 72800,
            'tcs_color_100': 4336,
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'deep pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 20, 147),
            'tsl_brt_100': 17100,
            'tcs_color_100': (138, 3, 17),
            'lux_coeff': (1000, 195, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 20, 147),
            'tsl_brt_100': 17700,
            'tcs_color_100': (137, 2, 15),
            'lux_coeff': (1000, 195, 0)
        }
    },
    {
        'name': 'deep sky blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 191, 255),
            'tsl_brt_100': 15000,
            'tcs_color_100': (0, 57, 105),
            'lux_coeff': (1000, 155, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 191, 255),
            'tsl_brt_100': 15000,
            'tcs_color_100': (0, 53, 105),
            'lux_coeff': (1000, 155, 0)
        }
    },
    {
        'name': 'dim gray',
        'google': {
            'is_rgb': True,
            'color_values': (105, 105, 105),
            'tsl_brt_100': 16000,
            'tcs_color_100': (34, 24, 29),
            'lux_coeff': (1450, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (105, 105, 105),
            'tsl_brt_100': 16400,
            'tcs_color_100': (36, 20, 28),
            'lux_coeff': (1450, 175, 0)
        }
    },
    {
        'name': 'dodger blue',
        'google': {
            'is_rgb': True,
            'color_values': (30, 144, 255),
            'tsl_brt_100': 15700,
            'tcs_color_100': (5, 31, 103),
            'lux_coeff': (1650, 165, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (30, 144, 255),
            'tsl_brt_100': 15900,
            'tcs_color_100': (5, 31, 103),
            'lux_coeff': (1650, 165, 0)
        }
    },
    {
        'name': 'firebrick',
        'google': {
            'is_rgb': True,
            'color_values': (178, 34, 34),
            'tsl_brt_100': 17100,
            'tcs_color_100': (186, 2, 5),
            'lux_coeff': (900, 195, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 34, 34),
            'tsl_brt_100': 17800,
            'tcs_color_100': (188, 2, 3),
            'lux_coeff': (900, 195, 0)
        }
    },
    {
        'name': 'floral white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': 71000,
            'tcs_color_100': 4640,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 240),
            'tsl_brt_100': 17700,
            'tcs_color_100': (26, 21, 43),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'forest green',
        'google': {
            'is_rgb': True,
            'color_values': (34, 139, 34),
            'tsl_brt_100': 15100,
            'tcs_color_100': (17, 46, 10),
            'lux_coeff': (1750, 160, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (34, 139, 34),
            'tsl_brt_100': 15400,
            'tcs_color_100': (20, 42, 9),
            'lux_coeff': (1750, 160, 0)
        }
    },
    {
        'name': 'fuchsia',
        'google': {
            'is_rgb': True,
            'color_values': (193, 84, 193),
            'tsl_brt_100': 16500,
            'tcs_color_100': (50, 11, 49),
            'lux_coeff': (1300, 180, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tsl_brt_100': 17400,
            'tcs_color_100': (57, 6, 55),
            'lux_coeff': (1300, 180, 0)
        }
    },
    # {
    #     'name': 'gainsboro',         # Google uses cct for this color
    #     # 'google': {
    #     #     'is_rgb': True,
    #     #     'color_values': (220, 220, 220),
    #     #     'tsl_brt_100': 17000,
    #     #     'tcs_color_100': (34, 24, 29),
    #     #     'lux_coeff': (1450, 175, 0)
    #     # },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (220, 220, 220),
    #         'tsl_brt_100': 16500,
    #         'tcs_color_100': (36, 20, 28),
    #         'lux_coeff': (1450, 175, 0)
    #     }
    # },
    # {
    #     'name': 'garnet',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'ghost white',       # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 7000,
            'tsl_brt_100': 72900,
            'tcs_color_100': 5335,
            'lux_coeff': (None, None, None)
        },
        'alexa': {                   # Need to tell Alexa to set a Full Color bulb 'to the color dark slate gray'
            'is_rgb': True,
            'color_values': (248, 248, 255),
            'tsl_brt_100': 16300,
            'tcs_color_100': (24, 23, 27),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'gold',
        'google': {
            'is_rgb': True,
            'color_values': (165, 124, 0),
            'tsl_brt_100': 16300,
            'tcs_color_100': (73, 17, 6),
            'lux_coeff': (1300, 185, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 215, 0),
            'tsl_brt_100': 16800,
            'tcs_color_100': (82, 13, 5),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'goldenrod',
        'google': {
            'is_rgb': True,
            'color_values': (218, 165, 32),
            'tsl_brt_100': 16500,
            'tcs_color_100': (78, 15, 6),
            'lux_coeff': (1250, 185, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (218, 165, 32),
            'tsl_brt_100': 16900,
            'tcs_color_100': (87, 11, 5),
            'lux_coeff': (1250, 185, 0)
        }
    },
    {
        'name': 'gray',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tsl_brt_100': 16000,
            'tcs_color_100': (34, 24, 29),
            'lux_coeff': (1450, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tsl_brt_100': 16400,
            'tcs_color_100': (35, 21, 28),
            'lux_coeff': (1450, 175, 0)
        }
    },
    {
        'name': 'green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 0),
            'tsl_brt_100': 13500,
            'tcs_color_100': (0, 93, 10),
            'lux_coeff': (2250, 135, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 0),
            'tsl_brt_100': 13600,
            'tcs_color_100': (0, 93, 10),
            'lux_coeff': (2250, 135, 0)
        }
    },
    {
        'name': 'green yellow',
        'google': {
            'is_rgb': True,
            'color_values': (173, 255, 47),
            'tsl_brt_100': 15600,
            'tcs_color_100': (33, 31, 8),
            'lux_coeff': (1600, 170, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (173, 255, 47),
            'tsl_brt_100': 15900,
            'tcs_color_100': (36, 29, 6),
            'lux_coeff': (1600, 170, 0)
        }
    },
    {
        'name': 'honeydew',
        'google': {
            'is_rgb': True,
            'color_values': (240, 255, 240),
            'tsl_brt_100': 15900,
            'tcs_color_100': (32, 24, 28),
            'lux_coeff': (1500, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 255, 240),
            'tsl_brt_100': 16400,
            'tcs_color_100': (34, 22, 26),
            'lux_coeff': (1500, 175, 0)
        }
    },
    {
        'name': 'hot pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 105, 180),
            'tsl_brt_100': 16700,
            'tcs_color_100': (87, 7, 24),
            'lux_coeff': (1140, 190, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 105, 180),
            'tsl_brt_100': 17200,
            'tcs_color_100': (87, 6, 22),
            'lux_coeff': (1140, 190, 0)
        }
    },
    {
        'name': 'incandescent',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 2700,
            'tsl_brt_100': 73000,
            'tcs_color_100': 2630,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2700,
            'tsl_brt_100': None,
            'tcs_color_100': 2630,
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'indian red',
        'google': {
            'is_rgb': True,
            'color_values': (205, 92, 92),
            'tsl_brt_100': 16900,
            'tcs_color_100': (114, 6, 11),
            'lux_coeff': (1000, 190, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (200, 100, 100),
            'tsl_brt_100': 17400,
            'tcs_color_100': (119, 5, 10),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'indigo',
        'google': {
            'is_rgb': True,
            'color_values': (75, 0, 130),
            'tsl_brt_100': 16200,
            'tcs_color_100': (16, 17, 120),
            'lux_coeff': (1450, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (75, 0, 130),
            'tsl_brt_100': 16500,
            'tcs_color_100': (14, 14, 117),
            'lux_coeff': (1450, 175, 0)
        }
    },
    {
        'name': 'ivory',               # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': 72800,
            'tcs_color_100': 4640,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 240),
            'tsl_brt_100': 16500,
            'tcs_color_100': (26, 21, 42),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'khaki',
        'google': {
            'is_rgb': True,
            'color_values': (195, 176, 145),
            'tsl_brt_100': 16200,
            'tcs_color_100': (46, 21, 21),
            'lux_coeff': (1400, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 230, 140),
            'tsl_brt_100': 16500,
            'tcs_color_100': (53, 18, 12),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'lavender',
        'google': {
            'is_rgb': True,
            'color_values': (181, 126, 220),
            'tsl_brt_100': 16500,
            'tcs_color_100': (31, 17, 55),
            'lux_coeff': (1400, 175, 0)
        },
        'alexa': {                          # These are custom values to match what Alexa chose for lavender
            'is_rgb': True,
            'color_values':(150, 127, 255),
            'tsl_brt_100': 16700,
            'tcs_color_100': (17, 18, 78),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'lavender blush',
        'google': {
            'is_rgb': True,
            'color_values': (255, 240, 245),
            'tsl_brt_100': 16200,
            'tcs_color_100': (26, 22, 46),
            'lux_coeff': (1500, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 240, 245),
            'tsl_brt_100': 16500,
            'tcs_color_100': (27, 22, 45),
            'lux_coeff': (1500, 175, 0)
        }
    },
    {
        'name': 'lawn green',
        'google': {
            'is_rgb': True,
            'color_values': (124, 252, 0),
            'tsl_brt_100': 15500,
            'tcs_color_100': (28, 37, 8),
            'lux_coeff': (1650, 165, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (124, 252, 0),
            'tsl_brt_100': 15800,
            'tcs_color_100': (32, 33, 6),
            'lux_coeff': (1650, 165, 0)
        }
    },
    {
        'name': 'lemon chiffon',
        'google': {
            'is_rgb': True,
            'color_values': (255, 250, 205),
            'tsl_brt_100': 16200,
            'tcs_color_100': (29, 23, 39),
            'lux_coeff': (1400, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 205),
            'tsl_brt_100': 16500,
            'tcs_color_100': (30, 20, 38),
            'lux_coeff': (1400, 175, 0)
        }
    },
    {
        'name': 'light blue',
        'google': {
            'is_rgb': True,
            'color_values': (173, 216, 230),
            'tsl_brt_100': 15800,
            'tcs_color_100': (23, 29, 37),
            'lux_coeff': (1550, 170, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (191, 239, 255),
            'tsl_brt_100': 16300,
            'tcs_color_100': (24, 26, 36),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'light coral',          # The rgb values shown here come from "hey google turn the lights to the color light coral.'
        'google': {                     # Google results vary using 'light coral' and 'the color light coral'
            'is_rgb': True,
            'color_values': (240, 128, 128),
            'tsl_brt_100': 16600,
            'tcs_color_100': (93, 9, 15),
            'lux_coeff': (1200, 185, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 128, 128),
            'tsl_brt_100': 17200,
            'tcs_color_100': (98, 7, 13),
            'lux_coeff': (1200, 185, 0)
        }
    },
    {
        'name': 'light cyan',           # The rgb values shown here come from "hey google turn the lights to the color light cyan.'
        'google': {                     # Google results vary using 'light cyan' and 'the color light cyan'
            'is_rgb': True,
            'color_values': (224, 255, 255),
            'tsl_brt_100': 15800,
            'tcs_color_100': (28, 26, 31),
            'lux_coeff': (1950, 150, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (224, 255, 255),
            'tsl_brt_100': 16200,
            'tcs_color_100': (29, 23, 31),
            'lux_coeff': (1950, 150, 0)
        }
    },
    {
        'name': 'light goldenrod',      # The rgb values shown here come from "hey google turn the lights to the color light goldenrod.'
        'google': {                     # Google results vary using 'light goldenrod' and 'the color light goldenrod'
            'is_rgb': True,
            'color_values': (255, 236, 139),
            'tsl_brt_100': 16000,
            'tcs_color_100': (44, 23, 18),
            'lux_coeff': (1450, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 250, 210),
            'tsl_brt_100': 16400,
            'tcs_color_100': (29, 21, 38),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'light gray',           # The rgb values shown here come from "hey google turn the lights to the color light gray.'
        'google': {                     # Google results vary using 'light gray' and 'the color light gray'
            'is_rgb': True,
            'color_values': (211, 211, 211),
            'tsl_brt_100': 16200,
            'tcs_color_100': (34, 24, 29),
            'lux_coeff': (1450, 175, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (211, 211, 211),
            'tsl_brt_100': 16400,
            'tcs_color_100': (36, 20, 27),
            'lux_coeff': (1450, 175, 0)
        }
    },
    {
        'name': 'light green',          # The rgb values shown here come from "hey google turn the lights to the color light green.'
        'google': {                     # Google results vary using 'light green' and 'the color light green'
            'is_rgb': True,
            'color_values': (144, 238, 144),
            'tsl_brt_100': 15500,
            'tcs_color_100': (23, 37, 18),
            'lux_coeff': (1650, 165, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (144, 238, 144),
            'tsl_brt_100': 15900,
            'tcs_color_100': (26, 31, 16),
            'lux_coeff': (1650, 175, 0)
        }
    },
    {
        'name': 'light pink',           # The rgb values shown here come from "hey google turn the lights to the color light pink.'
        'google': {                     # Google results vary using 'light pink' and 'the color light pink'
            'is_rgb': True,
            'color_values': (255, 182, 193),
            'tsl_brt_100': 16500,
            'tcs_color_100': (57, 14, 22),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 182, 193),
            'tsl_brt_100': 16900,
            'tcs_color_100': (61, 12, 21),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'light salmon',         # The rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light pink' and 'the color light salmon'
            'is_rgb': True,
            'color_values': (255, 160, 122),
            'tsl_brt_100': 16500,
            'tcs_color_100': (87, 10, 11),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 160, 122),
            'tsl_brt_100': 16900,
            'tcs_color_100': (92, 9, 10),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'light sea green',      # The rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light sea green'
            'is_rgb': True,
            'color_values': (32, 178, 170),
            'tsl_brt_100': 15500,
            'tcs_color_100': (11, 41, 39),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (46, 196, 182),
            'tsl_brt_100': 15700,
            'tcs_color_100': (12, 37, 39),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'light sky blue',       # The rgb values shown here come from "hey google turn the lights to the color light sky blue.'
        'google': {                     # Google results vary using 'light sea sky blue' and 'the color light sea ky blue'
            'is_rgb': True,
            'color_values': (135, 206, 250),
            'tsl_brt_100': 15400,
            'tcs_color_100': (15, 31, 50),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (135, 206, 250),
            'tsl_brt_100': 16300,
            'tcs_color_100': (15, 29, 50),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'light slate gray',     # The rgb values shown here come from "hey google turn the lights to the color light slate gray.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light slate gray'
            'is_rgb': True,
            'color_values': (119, 136, 153),
            'tsl_brt_100': 15900,
            'tcs_color_100': (25, 25, 37),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (119, 136, 153),
            'tsl_brt_100': 16300,
            'tcs_color_100': (26, 23, 37),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'light steel blue',     # The rgb values shown here come from "hey google turn the lights to the color light steel blue.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light steel blue'
            'is_rgb': True,
            'color_values': (176, 196, 222),
            'tsl_brt_100': 15700,
            'tcs_color_100': (13, 34, 49),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (174, 194, 223),
            'tsl_brt_100': 16200,
            'tcs_color_100': (26, 23, 37),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'light turquoise',      # The rgb values shown here come from "hey google turn the lights to the color light turquoise.'
        'google': {                     # Google results vary using 'light turquoise' and 'the color light turquoise'
            'is_rgb': True,
            'color_values': (175, 228, 222),
            'tsl_brt_100': 15800,
            'tcs_color_100': (22, 29, 34),
            'lux_coeff': (None, None, None)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
        #     'lux_coeff': (None, None, None)
        # }
    },
    {
        'name': 'light yellow',         # The rgb values shown here come from "hey google turn the lights to the color light yellow.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light yellow'
            'is_rgb': True,
            'color_values': (255, 255, 224),
            'tsl_brt_100': 16100,
            'tcs_color_100': (26, 23, 42),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 224),  # -bVal could be 237
            'tsl_brt_100': 16400,
            'tcs_color_100': (27, 21, 41),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'lime',
        'google': {
            'is_rgb': True,
            'color_values': (191, 255, 0),
            'tsl_brt_100': 15700,
            'tcs_color_100': (48, 25, 6),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (166, 214, 40),
            'tsl_brt_100': 15900,
            'tcs_color_100': (42, 27, 6),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'lime green',
        'google': {
            'is_rgb': True,
            'color_values': (50, 205, 50),
            'tsl_brt_100': 14900,
            'tcs_color_100': (17, 46, 9),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (50, 205, 50),
            'tsl_brt_100': 15200,
            'tcs_color_100': (19, 42, 8),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'linen',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': 70500,
            'tcs_color_100': 4640,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 240, 230),
            'tsl_brt_100': 16400,
            'tcs_color_100': (28, 20, 42),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'magenta',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tsl_brt_100': 16700,
            'tcs_color_100': (59, 7, 59),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tsl_brt_100': 17100,
            'tcs_color_100': (57, 6, 55),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'maroon',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 0),
            'tsl_brt_100': 17000,
            'tcs_color_100': (245, 0, 2),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 48, 96),
            'tsl_brt_100': 17400,
            'tcs_color_100': (120, 3, 14),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (102, 221, 170),  # -gVal could be 205
            'tsl_brt_100': 15400,
            'tcs_color_100': (17, 37, 28),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (97, 210, 180),
            'tsl_brt_100': 15900,
            'tcs_color_100': (18, 34, 28),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 205),
            'tsl_brt_100': 15500,
            'tcs_color_100': (0, 33, 219),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 205),
            'tsl_brt_100': 15700,
            'tcs_color_100': (0, 29, 212),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium orchid',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (186, 85, 211),
            'tsl_brt_100': 17100,
            'tcs_color_100': (38, 10, 56),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium purple',
        'google': {
            'is_rgb': True,
            'color_values': (147, 112, 219),
            'tsl_brt_100': 16300,
            'tcs_color_100': (21, 19, 71),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (147, 112, 219),
            'tsl_brt_100': 16600,
            'tcs_color_100': (21, 16, 69),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium sea green',
        'google': {
            'is_rgb': True,
            'color_values': (60, 179, 113),
            'tsl_brt_100': 15300,
            'tcs_color_100': (16, 42, 21),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (60, 179, 113),
            'tsl_brt_100': 15700,
            'tcs_color_100': (18, 38, 20),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium slate blue',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (123, 104, 238),
            'tsl_brt_100': 16500,
            'tcs_color_100': (11, 19, 96),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 250, 154),
            'tsl_brt_100': 14500,
            'tcs_color_100': (0, 66, 63),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 250, 154),
            'tsl_brt_100': 14700,
            'tcs_color_100': (0, 62, 65),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (72, 209, 204),
            'tsl_brt_100': 15500,
            'tcs_color_100': (12, 39, 39),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (72, 209, 204),
            'tsl_brt_100': 15700,
            'tcs_color_100': (13, 35, 40),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'medium violet red',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (199, 21, 133),
            'tsl_brt_100': 17700,
            'tcs_color_100': (111, 3, 22),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'midnight blue',
        'google': {
            'is_rgb': True,
            'color_values': (25, 25, 112),
            'tsl_brt_100': 15800,
            'tcs_color_100': (4, 24, 156),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (25, 25, 112),
            'tsl_brt_100': 16300,
            'tcs_color_100': (3, 21, 155),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'mint cream',
        'google': {
            'is_rgb': True,
            'color_values': (245, 255, 250),
            'tsl_brt_100': 16000,
            'tcs_color_100': (23, 25, 46),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 255, 250),
            'tsl_brt_100': 16400,
            'tcs_color_100': (24, 22, 44),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'misty rose',
        'google': {
            'is_rgb': True,
            'color_values': (255, 228, 225),
            'tsl_brt_100': 16200,
            'tcs_color_100': (28, 22, 42),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 228, 225),
            'tsl_brt_100': 16700,
            'tcs_color_100': (29, 20, 42),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'moccasin',
    #     # 'google': {
    #     #     'is_rgb': True,
    #     #     'color_values': (0, 0, 0),
    #     #     'tsl_brt_100': None,
    #     #     'tcs_color_100': None,
    #         # 'lux_coeff': (None, None, None)
    #     # },
    #     'alexa': {                   # Need to tell Alexa to set bulb 'to the color moccasin'
    #         'is_rgb': True,
    #         'color_values': (255, 228, 181),
    #         'tsl_brt_100': 16700,
    #         'tcs_color_100': (52, 17, 17),
    #         'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'navajo white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tsl_brt_100': 70700,
            'tcs_color_100': 4150,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 222, 173),
            'tsl_brt_100': 16800,
            'tcs_color_100': (55, 16, 16),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'navy blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 128),
            'tsl_brt_100': 15500,
            'tcs_color_100': (0, 33, 219),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 128),
            'tsl_brt_100': 15900,
            'tcs_color_100': (0, 29, 212),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'old lace',          # Google uses cct for this color
    #     # 'google': {
    #     #     'is_rgb': False,
    #     #     'color_values': 6100,
    #     #     'tsl_brt_100': 70600,
    #     #     'tcs_color_100': 4640,
    #     #     'lux_coeff': (None, None, None)
    #     # },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (253, 245, 230),
    #         'tsl_brt_100': 16600,
    #         'tcs_color_100': (27, 21, 42),
    #         'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'olive',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 0),
            'tsl_brt_100': 16100,
            'tcs_color_100': (63, 19, 6),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 0),
            'tsl_brt_100': 16600,
            'tcs_color_100': (68, 16, 5),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'olive drab',
        'google': {                  # Need to tell Google, set the bulb 'to the color olive drab'
            'is_rgb': True,
            'color_values': (107, 142, 35),
            'tsl_brt_100': 15700,
            'tcs_color_100': (36, 31, 9),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (107, 142, 35),
            'tsl_brt_100': 16000,
            'tcs_color_100': (38, 28, 8),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'olive green',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 102, 0),
            'tsl_brt_100': 16500,
            'tcs_color_100': (112, 8, 5),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 165, 0),
            'tsl_brt_100': 17200,
            'tcs_color_100': (99, 10, 4),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'orange red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 75, 0),
            'tsl_brt_100': 16700,
            'tcs_color_100': (156, 3, 4),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 75, 0),
            'tsl_brt_100': 17700,
            'tcs_color_100': (162, 3, 3),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'orchid',
        'google': {
            'is_rgb': True,
            'color_values': (218, 112, 214),
            'tsl_brt_100': 16400,
            'tcs_color_100': (49, 11, 43),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (218, 112, 214),
            'tsl_brt_100': 17000,
            'tcs_color_100': (50, 10, 42),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'pale goldenrod',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (238, 232, 170),
            'tsl_brt_100': 16600,
            'tcs_color_100': (47, 19, 16),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'pale green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (152, 251, 152),
            'tsl_brt_100': 15800,
            'tcs_color_100': (26, 32, 16),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'pale turquoise',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (180, 255, 255),
            'tsl_brt_100': 16200,
            'tcs_color_100': (23, 27, 34),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'pale violet red',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (219, 112, 147),
            'tsl_brt_100': 17200,
            'tcs_color_100': (83, 7, 19),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'papaya whip',
        'google': {
            'is_rgb': True,
            'color_values': (255, 239, 213),
            'tsl_brt_100': 16000,
            'tcs_color_100': (29, 22, 40),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 239, 213),
            'tsl_brt_100': 16700,
            'tcs_color_100': (30, 19, 39),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'peach puff',
        'google': {
            'is_rgb': True,
            'color_values': (255, 218, 185),
            'tsl_brt_100': 16200,
            'tcs_color_100': (52, 18, 18),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 218, 185),
            'tsl_brt_100': 16700,
            'tcs_color_100': (54, 15, 18),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'peru',
        'google': {
            'is_rgb': True,
            'color_values': (205, 133, 63),
            'tsl_brt_100': 16500,
            'tcs_color_100': (92, 10, 7),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (205, 133, 63),
            'tsl_brt_100': 16800,
            'tcs_color_100': (98, 9, 6),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 192, 203),
            'tsl_brt_100': 16400,
            'tcs_color_100': (33, 19, 41),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 185, 204),  # (250, 185, 203)
            'tsl_brt_100': 17000,
            'tcs_color_100': (55, 14, 22),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'plum',
        'google': {
            'is_rgb': True,
            'color_values': (142, 69, 133),
            'tsl_brt_100': 16600,
            'tcs_color_100': (52, 11, 40),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (221, 160, 221),
            'tsl_brt_100': 16900,
            'tcs_color_100': (42, 14, 36),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'powder blue',
        'google': {
            'is_rgb': True,
            'color_values': (176, 224, 230),
            'tsl_brt_100': 15800,
            'tcs_color_100': (23, 29, 34),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (174, 224, 221),
            'tsl_brt_100': 16400,
            'tcs_color_100': (25, 25, 34),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'pumpkin',                    # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (255, 117, 24),
            'tsl_brt_100': 16900,
            'tcs_color_100': (142, 5, 4),
            'lux_coeff': (None, None, None)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # }
    },
    {
        'name': 'purple',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 128),
            'tsl_brt_100': 16700,
            'tcs_color_100': (60, 7, 59),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (160, 32, 240),
            'tsl_brt_100': 17800,
            'tcs_color_100': (20, 13, 103),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'rebecca purple',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (102, 51, 153),
            'tsl_brt_100': 16800,
            'tcs_color_100': (21, 14, 82),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 0),
            'tsl_brt_100': 17300,
            'tcs_color_100': (245, 0, 3),
            'lux_coeff': (800, 200, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 0),
            'tsl_brt_100': 18000,
            'tcs_color_100': (245, 0, 3),
            'lux_coeff': (800, 200, 0)
        }
    },
    {
        'name': 'rosy brown',
        'google': {
            'is_rgb': True,
            'color_values': (188, 143, 143),
            'tsl_brt_100': 16400,
            'tcs_color_100': (52, 16, 22),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (188, 143, 143),
            'tsl_brt_100': 17000,
            'tcs_color_100': (57, 14, 21),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'royal blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 5, 102),
            'tsl_brt_100': 15300,
            'tcs_color_100': (0, 45, 147),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (65, 105, 225),
            'tsl_brt_100': 16200,
            'tcs_color_100': (5, 25, 117),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'saddle brown',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 69, 19),
            'tsl_brt_100': 17500,
            'tcs_color_100': (128, 5, 4),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'salmon',
        'google': {
            'is_rgb': True,
            'color_values': (250, 128, 114),
            'tsl_brt_100': 16800,
            'tcs_color_100': (105, 7, 11),
            'lux_coeff': (None, None, None)
        },
        'alexa': {                            # Alexa uses the 'light salmon' rgb values for salmon
            'is_rgb': True,
            'color_values': (255, 160, 125),
            'tsl_brt_100': 17200,
            'tcs_color_100': (91, 9, 11),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'sandy brown',
        'google': {
            'is_rgb': True,
            'color_values': (244, 164, 96),
            'tsl_brt_100': 16700,
            'tcs_color_100': (85, 11, 9),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (244, 164, 96),
            'tsl_brt_100': 17000,
            'tcs_color_100': (91, 10, 8),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'sea green',
        'google': {
            'is_rgb': True,
            'color_values': (46, 139, 87),
            'tsl_brt_100': 15400,
            'tcs_color_100': (17, 38, 21),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (46, 139, 87),
            'tsl_brt_100': 15600,
            'tcs_color_100': (18, 37, 20),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'seashell',          # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': 70400,
            'tcs_color_100': 4640,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 245, 238),
            'tsl_brt_100': 16500,
            'tcs_color_100': (27, 20, 42),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'sienna',
        'google': {
            'is_rgb': True,
            'color_values': (136, 45, 23),
            'tsl_brt_100': 16800,
            'tcs_color_100': (153, 3, 5),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (160, 82, 45),
            'tsl_brt_100': 17300,
            'tcs_color_100': (119, 6, 6),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'silver',
        'google': {
            'is_rgb': True,
            'color_values': (192, 192, 192),
            'tsl_brt_100': 16100,
            'tcs_color_100': (34, 23, 29),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (192, 192, 192),
            'tsl_brt_100': 16400,
            'tcs_color_100': (35, 23, 28),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'sky',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'sky blue',
        'google': {
            'is_rgb': True,
            'color_values': (135, 206, 235),
            'tsl_brt_100': 17100,
            'tcs_color_100': (15, 31, 47),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (135, 206, 235),
            'tsl_brt_100': 16100,
            'tcs_color_100': (17, 29, 45),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'slate',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'slate blue',
        'google': {
            'is_rgb': True,
            'color_values': (106, 90, 205),
            'tsl_brt_100': 17000,
            'tcs_color_100': (12, 23, 98),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (106, 90, 205),
            'tsl_brt_100': 16500,
            'tcs_color_100': (12, 19, 93),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'slate gray',
        'google': {
            'is_rgb': True,
            'color_values': (112, 128, 144),
            'tsl_brt_100': 17000,
            'tcs_color_100': (25, 27, 39),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (112, 128, 144),
            'tsl_brt_100': 16400,
            'tcs_color_100': (27, 23, 37),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'smitten',
        'google': {
            'is_rgb': True,
            'color_values': (200, 65, 134),
            'tsl_brt_100': 18000,
            'tcs_color_100': (96, 6, 23),
            'lux_coeff': (None, None, None)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # }
    },
    {
        'name': 'snow',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6500,
            'tsl_brt_100': 70100,
            'tcs_color_100': 4850,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 250),
            'tsl_brt_100': 16500,
            'tcs_color_100': (26, 21, 44),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'soft white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 3000,
            'tsl_brt_100': 72600,
            'tcs_color_100': 2830,
            'lux_coeff': (55.35, 844.17, -1.1178)
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2700,
            'tsl_brt_100': None,
            'tcs_color_100': 2630,
            'lux_coeff': (66.6, 874.62, -1.1867)
        }
    },
    {
        'name': 'spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 127),
            'tsl_brt_100': 15000,
            'tcs_color_100': (0, 72, 53),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 127),
            'tsl_brt_100': 14500,
            'tcs_color_100': (0, 65, 55),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'steel blue',
        'google': {
            'is_rgb': True,
            'color_values': (70, 130, 180),
            'tsl_brt_100': 16400,
            'tcs_color_100': (11, 30, 65),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (70, 130, 180),
            'tsl_brt_100': 16200,
            'tcs_color_100': (11, 29, 65),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'tan',
    #     # 'google': {
    #     #     'is_rgb': True,
    #     #     'color_values': (210, 180, 140),
    #     #     'tsl_brt_100': 17000,
    #     #     'tcs_color_100': (52, 19, 17),
    #     #     'lux_coeff': (None, None, None)
    #     # },
    #     'alexa': {                           # Need to tell Alexa turn bulb 'to the color tan'
    #         'is_rgb': True,
    #         'color_values': (210, 180, 140),
    #         'tsl_brt_100': 17000,
    #         'tcs_color_100': (52, 19, 17),
    #         'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'teal',
        'google': {
            'is_rgb': True,
            'color_values': (0, 128, 128),
            'tsl_brt_100': 15200,
            'tcs_color_100': (0, 55, 90),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 128, 128),
            'tsl_brt_100': 15000,
            'tcs_color_100': (0, 54, 91),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'thistle',
        'google': {
            'is_rgb': True,
            'color_values': (216, 191, 216),
            'tsl_brt_100': 16800,
            'tcs_color_100': (37, 20, 32),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (216, 191, 216),
            'tsl_brt_100': 16900,
            'tcs_color_100': (38, 18, 31),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'tomato',
        'google': {
            'is_rgb': True,
            'color_values': (255, 99, 71),
            'tsl_brt_100': 17600,
            'tcs_color_100': (145, 4, 6),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 99, 71),
            'tsl_brt_100': 17600,
            'tcs_color_100': (149, 3, 5),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (64, 224, 208),
            'tsl_brt_100': 15700,
            'tcs_color_100': (12, 39, 37),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (64, 224, 208),
            'tsl_brt_100': 15800,
            'tcs_color_100': (13, 37, 37),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'ultramarine',               # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (18, 10, 143),
            'tsl_brt_100': 15700,
            'tcs_color_100': (2, 26, 186),
            'lux_coeff': (None, None, None)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # }
    },
    {
        'name': 'vermillion',                # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (217, 56, 30),
            'tsl_brt_100': 17000,
            'tcs_color_100': (168, 2, 5),
            'lux_coeff': (None, None, None)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # }
    },
    {
        'name': 'violet',
        'google': {
            'is_rgb': True,
            'color_values': (127, 0, 255),
            'tsl_brt_100': 16100,
            'tcs_color_100': (8, 19, 144),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (238, 130, 238),
            'tsl_brt_100': 17200,
            'tcs_color_100': (48, 10, 40),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'warm',                # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': '',
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tsl_brt_100': None,
            'tcs_color_100': 2320,
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'warm white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 3000,
            'tsl_brt_100': 72800,
            'tcs_color_100': 2830,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tsl_brt_100': None,
            'tcs_color_100': 2320,
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'web gray',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tsl_brt_100': 16600,
            'tcs_color_100': (36, 20, 27),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'web green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
            # 'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 128, 0),
            'tsl_brt_100': 13500,
            'tcs_color_100': (0, 92, 9),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'web maroon',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 0),
            'tsl_brt_100': 17200,
            'tcs_color_100': (245, 0, 2),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 48, 96),
            'tsl_brt_100': 17400,
            'tcs_color_100': (119, 3, 15),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'web purple',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (128, 0, 128),
        #     'tsl_brt_100': None,
        #     'tcs_color_100': None,
        #     'lux_coeff': (None, None, None)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 0, 128),
            'tsl_brt_100': 16700,
            'tcs_color_100': (20, 12, 102),
            'lux_coeff': (None, None, None)
        }
    },
    # {
    #     'name': 'wheat',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (245, 222, 179),
    #         'tsl_brt_100': 16200,
    #         'tcs_color_100': (48, 19, 18),
    #         'lux_coeff': (None, None, None)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (245, 222, 179),
    #         'tsl_brt_100': 16700,
    #         'tcs_color_100': (51, 17, 17),
    #         'lux_coeff': (None, None, None)
    #     }
    # },
    {
        'name': 'white',                   # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tsl_brt_100': 71300,
            'tcs_color_100': 4150,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 4000,
            'tsl_brt_100': None,
            'tcs_color_100': 3350,
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'white smoke',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 7000,
            'tsl_brt_100': 72800,
            'tcs_color_100': 5335,
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 245, 245),
            'tsl_brt_100': 16500,
            'tcs_color_100': (25, 21, 45),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'yellow',
        'google': {
            'is_rgb': True,
            'color_values': (255, 255, 0),
            'tsl_brt_100': 16300,
            'tcs_color_100': (64, 19, 6),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 0),
            'tsl_brt_100': 16600,
            'tcs_color_100': (68, 16, 5),
            'lux_coeff': (None, None, None)
        }
    },
    {
        'name': 'yellow green',
        'google': {
            'is_rgb': True,
            'color_values': (154, 205, 50),
            'tsl_brt_100': 15800,
            'tcs_color_100': (36, 30, 8),
            'lux_coeff': (None, None, None)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (154, 205, 50),
            'tsl_brt_100': 15900,
            'tcs_color_100': (40, 27, 7),
            'lux_coeff': (None, None, None)
        }
    }
]


if __name__ == '__main__':
#     for color in supported_colors_list:
#         try:
#             if not color['alexa']['is_rgb']:
#                 print(color['name'])
#         except Exception as ex:
#             pass

    voice_agent = 'google'
    color_list = []
    for color in supported_colors_list:
        if color.get(voice_agent):
            if color.get(voice_agent).get('is_rgb'):
                color_list.append(color)

    # for color in supported_colors_list:
    #     if color.get(voice_agent):
    #         if color.get(voice_agent).get('color_values'):
    #             print(color['name'], color[voice_agent]['color_values'])
        # print(color['name'], color[voice_agent]['color_values'])

    print('color_list length: ', len(color_list))

else:
    print('Successfully imported supported colors.py')
