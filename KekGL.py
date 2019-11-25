"""
KekGL is like OtherGLs but Kek.

Note that in KekGl row-major matrix order is used.
"""

from matrix import *


class Prim:
    """ Class to define operations with primitives
    Coordinates of their points stored as a concatenated rows of homogeneous coordinates
    """
    def __init__(self, crds, color='black', outline='black', width=1):
        self.color = color
        self.outline = outline
        self.width = width
        self.num_of_vertices = len(crds)
        self.w_crds = Matrix(len(crds), 4)
        for i in range(len(crds)):
            self.w_crds.set_row(i, list(crds[i])+[1])
        self.c_crds = self.w_crds*1
        self.p_crds = None
        self.s_crds = None

    # Setting position and direction of the primitive in the world
    def toWorld(self, matrix, *args, **kwargs):
        self.w_crds *= matrix

    # Setting position and direction relative to the camera (input matrix should be inverse camera matrix)
    def toCamera(self, matrix, *args, **kwargs):
        self.c_crds = self.w_crds*matrix

    # Getting projected coordinates using projection matrix
    def toProjection(self, matrix, *args, **kwargs):
        self.p_crds = self.c_crds*matrix

    # NDC is normalized device coordinates
    def toNDC(self):
        for i in range(self.num_of_vertices):
            self.p_crds.set_row(i, [a/self.p_crds[i][3] for a in self.p_crds[i]])

    def toScreen(self):
        self.s_crds = Matrix(self.num_of_vertices, 2)
        for i in range(self.num_of_vertices):  # TODO: common case for width and height
            self.s_crds.set_row(i, [400*(self.p_crds[i][0]+1), 300*(self.p_crds[i][1]+1)])

    def isInFront(self):
        for i in range(self.num_of_vertices):
            if self.c_crds[i][2] >= -20:
                return False

        return True

    # should be inited after self.toNDC()
    def isVisible(self):
        if self.isInFront():
            for i in range(self.num_of_vertices):
                # comparing coordinates with far plane sides coordinates
                if abs(self.p_crds[i][0]) >= 1 or abs(self.p_crds[i][1]) >= 1:
                    return False
            return True
        else:
            return False


class Object:
    """ Class that makes primitives from a model
    Operations with Object are the same as for Prim
    """
    def __init__(self, model):
        self.prims = []
        for poly in model:
            self.prims += [Prim(crds=poly['crds'], color=poly['color'],
                                outline=poly['outline'], width=poly['width'])]
        self.center = [0]*4

    def toWorld(self, matrix, *args, **kwargs):
        for prim in self.prims:
            prim.toWorld(matrix, *args, **kwargs)

    def toCamera(self, matrix, *args, **kwargs):
        for prim in self.prims:
            prim.toCamera(matrix, *args, **kwargs)

    def toProjection(self, matrix, *args, **kwargs):
        for prim in self.prims:
            prim.toProjection(matrix, *args, **kwargs)

    def toNDC(self):
        for prim in self.prims:
            prim.toNDC()

    def toScreen(self):
        for prim in self.prims:
            prim.toScreen()

    def isInFront(self):
        for prim in self.prims:
            if not prim.isInFront():
                return False

        return True

    def isVisible(self):
        for prim in self.prims:
            if not prim.isVisible():
                return False

        return True


class Player:
    pass


class World:
    def __init__(self, player, *objects):
        pass


class Main:
    def __init__(self, world):
        pass

    def update(self):
        pass
