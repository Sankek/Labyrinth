"""
KekGL is like OtherGLs but Kek.

Note that in KekGl row-major matrix order is used.
"""

from matrix import *
from copy import deepcopy


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
    def toWorld(self, matrix, **kwargs):
        self.w_crds *= matrix

    # Setting position and direction relative to the camera (input matrix should be inverse camera matrix)
    def toCamera(self, matrix, *args, **kwargs):
        self.c_crds = self.w_crds*matrix

    # Getting projected coordinates using projection matrix
    def toProjection(self, matrix, *args, **kwargs):
        self.p_crds = self._algorithm(1)*matrix
        # self.p_crds = self.c_crds*matrix
        self.test_crds = self._algorithm(1)*1

    # NDC is normalized device coordinates
    def toNDC(self):
        for i in range(self.p_crds.rows):
            self.p_crds.set_row(i, [a/self.p_crds[i][3] for a in self.p_crds[i]])

    def toScreen(self):
        self.s_crds = Matrix(self.p_crds.rows, 2)
        for i in range(self.p_crds.rows):  # TODO: common case for width and height
            self.s_crds.set_row(i, [400*(self.p_crds[i][0]+1), 300*(self.p_crds[i][1]+1)])

    @staticmethod
    # finds intersection of line p1p2 with plane z+dx=0
    def _intersec(x, y, dx):
        p1 = deepcopy(x)
        p2 = deepcopy(y)
        t = -(p1[2]+dx)/(p2[2]-p1[2])
        return [[p1[0]+(p2[0]-p1[0])*t, p1[1]+(p2[1]-p1[1])*t, -dx, 1]]

    def _algorithm(self, dx):
        crds_list = []
        p_start = None

        for i in range(self.c_crds.rows):
            if self.c_crds[i][2] < 0:
                p_start = deepcopy(self.c_crds[i])
                # crds_list += deepcopy([p_start])
                try:
                    p_curr = deepcopy(self.c_crds[i+1])
                    i_curr = i+1
                except IndexError:
                    p_curr = deepcopy(self.c_crds[0])
                    i_curr = 0
                p_prev = deepcopy(p_start)
                prev = 1
                break

        if p_start is None:
            return Matrix(2, 4, [[10, 0, 1, 1], [10, 0, 1, 1]])  # making a point which will be invisible

        counter = 0
        while counter != self.c_crds.rows:
            if p_curr[2] < 0:
                curr = 1
            elif p_curr[2] == 0:
                curr = 0
            else:
                curr = -1

            while True:
                if curr == -1 and prev == 1:
                    crds_list += deepcopy(self._intersec(p_curr, p_prev, dx))
                    break
                if curr == 0 and prev == 1:
                    crds_list += deepcopy(self._intersec(p_curr, p_prev, dx))
                    break
                if curr == 1 and prev == 1:
                    crds_list += deepcopy([p_curr])
                    break
                if curr == -1 and prev == -1:
                    break
                if curr == 0 and prev == -1:
                    break
                if curr == 1 and prev == -1:
                    crds_list += deepcopy(self._intersec(p_curr, p_prev, dx))
                    crds_list += deepcopy([p_curr])
                    break
                if curr == -1 and prev == 0:
                    break
                if curr == 0 and prev == 0:
                    break
                if curr == 1 and prev == 0:
                    crds_list += deepcopy(self._intersec(p_curr, p_prev, dx))
                    crds_list += deepcopy([p_curr])
                    break

            p_prev = deepcopy(p_curr)
            prev = curr
            i_curr += 1
            counter += 1
            try:
                p_curr = deepcopy(self.c_crds[i_curr])
            except IndexError:
                p_curr = deepcopy(self.c_crds[0])
                i_curr = 0


        return Matrix(len(crds_list), 4, crds_list)

        # if self.c_crds[0][2] < 0:
        #     crds_list += self.c_crds[0]
        #
        #     if self.c_crds[0+1][2] > 0:
        #         crds_list += self._intersec(self.c_crds[0], self.c_crds[0+1], dx)
        #
        #         if self.c_crds[0+2][2] > 0:
        #             pass
        #
        #         if self.c_crds[0+2][2] == 0:
        #
        #     return Matrix(len(crds_list), 4, crds_list)
        #
        # return Matrix(2, 4, [[0, 0, 1, 1], [0, 0, 1, 1]])  # making a point which will be invisible

    def isInFront(self):
        # for i in range(self.num_of_vertices):
        #     if self.c_crds[i][2] >= 0:
        #         return False

        return True

    # should be inited after self.toNDC()
    def isVisible(self):
        # if self.isInFront():
        #     for i in range(self.num_of_vertices):
        #         # comparing coordinates with far plane sides coordinates
        #         if abs(self.p_crds[i][0]) >= 1 or abs(self.p_crds[i][1]) >= 1:
        #             return False
        #     return True
        # else:
        #     return False

        return True


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
