""" This module contains models of objects that can be imported to the game """

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

wall_1 = (-10, 0, 0), (-10, 40, 0), (50, 40, 0), (50, 0, 0)
wall_2 = (-10, 0, 0), (-10, 40, 0), (-10, 40, 20), (-10, 0, 20)
wall_3 = (10, 0, 0), (10, 20, 0), (10, 20, 20), (10, 0, 20)
wall_4 = (-10, 40, 0), (50, 40, 0), (50, 40, 20), (-10, 40, 20)
wall_5 = (10, 20, 0), (50, 20, 0), (50, 20, 20), (10, 20, 20)

corner_model = [{'crds': wall_1, 'color': 'red', 'outline': 'black', 'width': 0},
                {'crds': wall_2, 'color': 'green', 'outline': 'black', 'width': 0},
                {'crds': wall_3, 'color': 'green', 'outline': 'black', 'width': 0},
                {'crds': wall_4, 'color': 'green', 'outline': 'black', 'width': 0},
                {'crds': wall_5, 'color': 'green', 'outline': 'black', 'width': 0},
                ]
