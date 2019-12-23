""" This module contains models of objects that can be imported to the game """
import random

poly_1 = (10, 10, 10), (20, 20, 0), (-20, 20, 0), (-10, 10, 10)
poly_2 = (-10, 10, 10), (-20, 20, 0), (-20, -20, 0), (-10, -10, 10)
poly_3 = (-10, -10, 10), (-20, -20, 0), (20, -20, 0), (10, -10, 10)
poly_4 = (10, -10, 10), (20, -20, 0), (20, 20, 0), (10, 10, 10)
poly_5 = (10, 10, 10), (-10, 10, 10), (-10, -10, 10), (10, -10, 10)
poly_6 = (20, 20, 0), (-20, 20, 0), (-20, -20, 0), (20, -20, 0)

# Truncated Square Pyramid, sides are parallel to the coordinate axes.
pyramid_model = [{'crds': poly_1, 'color': 'red', 'outline': 'black', 'width': 2},
                 {'crds': poly_2, 'color': 'green', 'outline': 'black', 'width': 2},
                 {'crds': poly_3, 'color': 'blue', 'outline': 'black', 'width': 2},
                 {'crds': poly_4, 'color': 'black', 'outline': 'black', 'width': 2},
                 {'crds': poly_5, 'color': 'grey', 'outline': 'black', 'width': 2},
                 {'crds': poly_6, 'color': 'orange', 'outline': 'black', 'width': 2},
                 ]

# wall_1 = (-10, 0, 0), (-10, 40, 0), (50, 40, 0), (50, 0, 0)
# wall_2 = (-10, 0, 0), (-10, 40, 0), (-10, 40, 20), (-10, 0, 20)
# wall_3 = (10, 0, 0), (10, 20, 0), (10, 20, 20), (10, 0, 20)
# wall_4 = (-10, 40, 0), (50, 40, 0), (50, 40, 20), (-10, 40, 20)
# wall_5 = (10, 20, 0), (50, 20, 0), (50, 20, 20), (10, 20, 20)

colors = ['green', 'blue', 'grey', 'orange', 'pink', 'violet', 'yellow']

floor = (-800, -800, 0), (-800, 1800, 0), (2800, 1800, 0), (2800, -800, 0)
wall_1 = (-200, -200, 0), (-200, -200, 120), (-200, 300, 120), (-200, 300, 0)
wall_2 = (-200, -200, 0), (-200, -200, 120), (300, -200, 120), (300, -200, 0)
wall_3 = (300, -200, 0), (300, -200, 120), (300, 300, 120), (300, 300, 0)
wall_4 = (300, 300, 0), (300, 300, 120), (100, 300, 120), (100, 300, 0)
wall_5 = (-200, 300, 0), (-200, 300, 120), (0, 300, 120), (0, 300, 0)
wall_6 = (0, 300, 0), (0, 300, 120), (0, 600, 120), (0, 600, 0)
wall_7 = (100, 300, 0), (100, 300, 120), (100, 600, 120), (100, 600, 0)
wall_8 = (0, 600, 0), (0, 600, 120), (-100, 800, 120), (-100, 800, 0)
wall_9 = (-100, 800, 0), (-100, 800, 120), (-100, 1100, 120), (-100, 1100, 0)
wall_10 = (0, 800, 0), (0, 800, 120), (0, 1000, 120), (0, 1000, 0)
wall_11 = (-100, 1100, 0), (-100, 1100, 120), (600, 1100, 120), (600, 1100, 0)
wall_12 = (0, 1000, 0), (0, 1000, 120), (500, 1000, 120), (500, 1000, 0)
wall_13 = (500, 1000, 0), (500, 1000, 120), (500, 800, 120), (500, 800, 0)
wall_14 = (600, 1100, 0), (600, 1100, 120), (600, 700, 120), (600, 700, 0)
wall_15 = (600, 700, 0), (600, 700, 120), (200, 700, 120), (200, 700, 0)
wall_16 = (500, 800, 0), (500, 800, 120), (0, 800, 120), (0, 800, 0)
wall_17 = (100, 600, 0), (100, 600, 120), (400, 300, 120), (400, 300, 0)
wall_18 = (200, 700, 0), (200, 700, 120), (500, 400, 120), (500, 400, 0)
wall_18 = (400, -300, 0), (400, -300, 120), (400, 300, 120), (400, 300, 0)
wall_19 = (500, 0, 0), (500, 0, 120), (500, 300, 120), (500, 300, 0)
wall_20 = (500, 300, 0), (500, 300, 120), (700, 300, 120), (700, 300, 0)
wall_21 = (500, 400, 0), (500, 400, 120), (1200, 400, 120), (1200, 400, 0)
wall_22 = (500, 0, 0), (500, 0, 120), (700, 0, 120), (700, 0, 0)
wall_23 = (700, 0, 0), (700, 0, 120), (700, 300, 120), (700, 300, 0)
wall_24 = (500, -100, 0), (500, -100, 120), (800, -100, 120), (800, -100, 0)
wall_25 = (800, -100, 0), (800, -100, 120), (800, 300, 120), (800, 300, 0)
wall_26 = (500, -100, 0), (500, -100, 120), (500, -200, 120), (500, -200, 0)
wall_27 = (500, -200, 0), (500, -200, 120), (900, -200, 120), (900, -200, 0)
wall_28 = (900, -200, 0), (900, -200, 120), (900, 300, 120), (900, 300, 0)
wall_29 = (1000, 100, 0), (1000, 100, 120), (1000, 200, 120), (1000, 200, 0)
wall_30 = (1000, 100, 0), (1000, 100, 120), (1100, 100, 120), (1100, 100 ,0)
wall_31 = (1000, 200, 0), (1000, 200, 120), (1100, 200, 120), (1100, 200, 0)
wall_32 = (1100, 100, 0), (1100, 100, 120), (1100, 200, 120), (1100, 200, 0)
wall_33 = (1100, 0, 0), (1100, 0, 120), (1200, 0, 120), (1200, 0, 0)
wall_34 = (1100, 0, 0), (1100, 0, 120), (1100, -100, 120), (1100, -100, 0)
wall_35 = (1100, -100, 0), (1100, -100, 120), (1200, -100, 120), (1200, -100, 0)
wall_36 = (1200, -100, 0), (1200, -100, 120), (1200, 0 ,120), (1200, 0, 0)
wall_37 = (200, 700, 0), (200, 700, 120), (500, 400, 120), (500, 400, 0)
wall_38 = (1200, 100, 0), (1200, 100, 120), (1200, 200, 120), (1200, 200, 0)
wall_39 = (1200, 200, 0), (1200, 200, 120), (1300, 200, 120), (1300, 200, 0)
wall_40 = (1200, 100, 0), (1200, 100, 120), (1300, 100, 120), (1300, 100, 0)
wall_41 = (1300, 100, 0), (1300, 100, 120), (1300, 200, 120), (1300, 200, 0)
wall_42 = (400, -300, 0), (400, -300, 120), (1400, -300, 120), (1400, -300, 0)
wall_43 = (1400, -300, 0), (1400, -300, 120), (1400, 0, 120), (1400, 0, 0)
wall_44 = (1400, 0 , 0), (1400, 0, 120), (1500, 0 ,120), (1500, 0, 0)
wall_45 = (1400, 100 , 0), (1400, 100, 120), (1600, 100 ,120), (1600, 100, 0)
wall_46 = (1500, 0, 0), (1500, 0 ,120), (1500, -300, 120), (1500, -300, 0)
wall_47 = (1600, 100, 0), (1600, 100, 120), (1600, -200, 120), (1600, -200, 0)
wall_48 = (1600, -200, 0), (1600, -200, 120), (1700, -200, 120), (1700, -200, 0)
wall_49 = (1500, -300, 0), (1500, -300, 120), (1800, -300, 120), (1800, -300, 0)
wall_50 = (1700, -200, 0), (1700, -200, 120), (1700, 0, 120), (1700, 0, 0)
wall_51 = (1800, -300, 0), (1800, -300, 120), (1800, -100, 120), (1800, -100, 0)
wall_52 = (1700, 0, 0), (1700, 0, 120), (2000, 0, 120), (2000, 0, 0)
wall_53 = (1800, -100, 0), (1800, -100, 120), (2100, -100, 120), (2100, -100, 0)
wall_54 = (2000, 0, 0), (2000, 0, 120), (2000, 200, 120), (2000, 200, 0)
wall_55 = (2100, -100, 0), (2100, -100, 120), (2100, 500, 120), (2100, 500, 0)
wall_56 = (1400, 100, 0), (1400, 100, 120), (1400, 200, 120), (1400, 200, 0)
wall_57 = (1400, 200, 0), (1400, 200, 120), (2000, 200, 120), (2000, 200, 0)
wall_58 = (1400, 300, 0), (1400, 300, 120), (2000, 300, 120), (2000, 300, 0)
wall_59 = (2000, 300, 0), (2000, 300, 120), (2000, 400, 120), (2000, 400, 0)
wall_60 = (2000, 400, 0), (2000, 400, 120), (1500, 400, 120), (1500, 400, 0)
wall_61 = (2100, 500, 0), (2100, 500, 120), (1600, 500, 120), (1600, 500, 0)
wall_62 = (1400, 300, 0), (1400, 300, 120), (1500, 400, 120), (1500, 400, 0)
wall_63 = (1600, 500, 0), (1600, 500, 120), (1600, 600, 120), (1600, 600, 0)
wall_64 = (1600, 600, 0), (1600, 600, 120), (800, 600, 120), (800, 600, 0)
wall_65 = (1200, 400, 0), (1200, 400, 120), (1200, 500, 120), (1200, 500, 0)
wall_66 = (1200, 500, 0), (1200, 500, 120), (700, 500, 120), (700, 500, 0)
wall_67 = (700, 500, 0), (700, 500, 120), (700, 800, 120), (700, 800, 0)
wall_68 = (800, 600, 0), (800, 600, 120), (800, 700, 120), (800, 700, 0)
wall_69 = (800, 700, 0), (800, 700, 120), (1200, 700, 120), (1200, 700, 0)
wall_70 = (700, 800, 0), (700, 800, 120), (900, 800, 120), (900, 800, 0)
wall_71 = (900, 800, 0), (900, 800, 120), (900, 1000, 120), (900, 1000, 0)
wall_72 = (900, 1000, 0), (900, 1000, 120), (1200, 1000, 120), (1200, 1000, 0)
wall_73 = (1200, 1000, 0), (1200, 1000, 120), (1200, 700, 120), (1200, 700, 0)
wall_74 = (0, 0, 0), (0, 100, 0), (100, 100, 0), (100, 0, 0)
wall_75 = (1000, 800, 0), (1100, 800, 0), (1100, 900, 0), (1000, 900, 0)

corner_model = [{'crds': floor, 'color': '#17fbaf', 'outline': 'black', 'width': 0},
                {'crds': wall_1, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_2, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_3, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_4, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_5, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_6, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_7, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_8, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_9, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_10, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_11, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_12, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_13, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_14, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_15, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_16, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_17, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_18, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_19, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_20, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_21, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_22, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_23, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_24, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_25, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_26, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_27, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_28, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_29, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_30, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_31, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_32, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_33, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_34, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_35, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_36, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_37, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_38, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_39, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_40, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_41, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_42, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_43, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_44, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_45, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_46, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_47, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_48, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_49, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_50, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_51, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_52, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_53, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_54, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_55, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_56, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_57, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_58, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_59, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_60, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_61, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_62, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_63, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_64, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_65, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_66, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_67, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_68, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_69, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_70, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_71, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_72, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_73, 'color': random.choice(colors), 'outline': 'black', 'width': 0},
                {'crds': wall_74, 'color': 'red', 'outline': 'black', 'width': 0},
                {'crds': wall_75, 'color': 'red', 'outline': 'black', 'width': 0},
                ]