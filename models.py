""" This module contains models of objects that can be imported to the game """

poly_1 = (10, 10, 10), (20, 20, 0), (-20, 20, 0), (-10, 10, 10)
poly_2 = (-10, 10, 10), (-20, 20, 0), (-20, -20, 0), (-10, -10, 10)
poly_3 = (-10, -10, 10), (-20, -20, 0), (20, -20, 0), (10, -10, 10)
poly_4 = (10, -10, 10), (20, -20, 0), (20, 20, 0), (10, 10, 10)
poly_5 = (10, 10, 10), (-10, 10, 10), (-10, -10, 10), (10, -10, 10)
poly_6 = (20, 20, 0), (-20, 20, 0), (-20, -20, 0), (20, -20, 0)

# Truncated Square Pyramid, sides are parallel to the coordinate axes.
pyramid_model = [{'crds': poly_1, 'color': 'green', 'outline': 'black', 'width': 2},
                 {'crds': poly_2, 'color': 'green', 'outline': 'black', 'width': 2},
                 {'crds': poly_3, 'color': 'green', 'outline': 'black', 'width': 2},
                 {'crds': poly_4, 'color': 'green', 'outline': 'black', 'width': 2},
                 {'crds': poly_5, 'color': 'green', 'outline': 'black', 'width': 2},
                 {'crds': poly_6, 'color': 'green', 'outline': 'black', 'width': 2},
                 ]
