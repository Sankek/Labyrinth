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
        self.c_crds = None
        self.p_crds = None
        self.ndc_crds = None
        self.s_crds = None

    # Setting position and direction of the primitive in the world
    def toWorld(self, matrix):
        self.w_crds *= matrix

    # Setting position and direction relative to the camera (input matrix should be inverse camera matrix)
    def toCamera(self, matrix):
        self.c_crds = self.w_crds*matrix

    # Getting projected coordinates using projection matrix
    def toProjection(self, matrix):
        self.p_crds = self._rear_clipping_algorithm(1)*matrix
        self.test_crds = self._rear_clipping_algorithm(1)

    # NDC is normalized device coordinates
    def toNDC(self):
        self.ndc_crds = self.p_crds*1
        for i in range(self.p_crds.rows):
            self.ndc_crds.set_row(i, [a/self.p_crds[i][3] for a in self.p_crds[i]])

    def toScreen(self, width, height):
        self.s_crds = Matrix(self.p_crds.rows, 2)
        for i in range(self.p_crds.rows):
            self.s_crds.set_row(i, [width/2*(self.ndc_crds[i][0]+1), height/2*(self.ndc_crds[i][1]+1)])

    @staticmethod
    # finds intersection of line p1p2 with plane z+dz=0
    def _intersec(p1, p2, dz):
        t = -(p1[2]+dz)/(p2[2]-p1[2])
        return [p1[0]+(p2[0]-p1[0])*t, p1[1]+(p2[1]-p1[1])*t, -dz, 1]

    def _rear_clipping_algorithm(self, dz):
        """ Clips polygons with plane z=0 and returns new polygon's matrix

        It checks every two points starting from the visible one. Depending on the sign
        of their z-coordinate a new point added or not to the new list of coordinates.
        Clipping points have z = -dx coordinate to project correctly.
        Too big or too small values of dz can produce glitches. dz = 1 seems to be fine"""
        crds_list = []
        p_prev = None

        for i in range(self.c_crds.rows):
            if self.c_crds[i][2] < 0:
                try:
                    p_curr = [*self.c_crds[i+1]]
                    i_curr = i+1
                except IndexError:
                    p_curr = [*self.c_crds[0]]
                    i_curr = 0
                p_prev = [*self.c_crds[i]]
                prev = 1
                break

        if p_prev is None:
            return Matrix(2, 4, [[10, 0, 1, 1], [10, 0, 1, 1]])  # returns invisible polygon

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
                    crds_list += [self._intersec(p_curr, p_prev, dz)]
                    break
                if curr == 0 and prev == 1:
                    crds_list += [self._intersec(p_curr, p_prev, dz)]
                    break
                if curr == 1 and prev == 1:
                    crds_list += [p_curr]
                    break
                if curr == -1 and prev == -1:
                    break
                if curr == 0 and prev == -1:
                    break
                if curr == 1 and prev == -1:
                    crds_list += [self._intersec(p_curr, p_prev, dz)]
                    crds_list += [p_curr]
                    break
                if curr == -1 and prev == 0:
                    break
                if curr == 0 and prev == 0:
                    break
                if curr == 1 and prev == 0:
                    crds_list += [self._intersec(p_curr, p_prev, dz)]
                    crds_list += [p_curr]
                    break

            p_prev = p_curr
            prev = curr
            i_curr += 1
            counter += 1
            try:
                p_curr = [*self.c_crds[i_curr]]
            except IndexError:
                p_curr = [*self.c_crds[0]]
                i_curr = 0

        return Matrix(len(crds_list), 4, crds_list)

    def isInFront(self):
        for i in range(self.num_of_vertices):
            if self.c_crds[i][2] >= 0:
                return False

        return True

    # should be inited after self.toNDC()
    def isFullyVisible(self):
        if self.isInFront():
            for i in range(self.num_of_vertices):
                if abs(self.ndc_crds[i][0]) >= 1 or abs(self.ndc_crds[i][1]) >= 1:
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

    def toWorld(self, matrix):
        for prim in self.prims:
            prim.toWorld(matrix)

    def toCamera(self, matrix):
        for prim in self.prims:
            prim.toCamera(matrix)

    def toProjection(self, matrix):
        for prim in self.prims:
            prim.toProjection(matrix)

    def toNDC(self):
        for prim in self.prims:
            prim.toNDC()

    def toScreen(self, width, height):
        for prim in self.prims:
            prim.toScreen(width, height)

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
