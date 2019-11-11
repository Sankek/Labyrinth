"""
It's an example of using transformation matrices in the 2D space, which in future may be expanded to the 3D space.

Press 'd' to rotate clockwise
Press 'a' to rotate counterclockwise
Press 's' to stop.
"""

from tkinter import *
from Matrix import *
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
root.resizable(False, False)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class Object:
    """
    This class describes 2D-objects methods to transform
    """
    def __init__(self, crds, x=400, y=300):
        self.center = Matrix(2, 1, [[x], [y]])
        self.crds = [Matrix(2, 1, [[x], [y]]) for x, y in crds]
        self.abscrds = [matr+self.center for matr in self.crds]

    def set_coords(self):
        canv.coords(self.id, *crds_to_row(self.abscrds))

    def transform(self, func, *args, **kwargs):
        self.crds = [func(*args, **kwargs)*matr for matr in self.crds]
        self.abscrds = [matr+self.center for matr in self.crds]

    def rotate(self, angle):
        self.transform(M_rot, angle)


class Line(Object):
    def __init__(self, crds, x=400, y=300, color='black'):
        super().__init__(crds, x, y)
        self.id = canv.create_line(*crds_to_row(self.abscrds), fill=color)


class Point(Object):
    def __init__(self, crd, x=400, y=300, color='red', size=2):
        super().__init__(crd, x, y)
        self.sizeMatr = Matrix(2, 1, [[size], [size]])
        self.id = canv.create_oval(*(self.abscrds[0]-self.sizeMatr).col(0),
                                   *(self.abscrds[0]+self.sizeMatr).col(0), fill=color, width=0)
        print(self.abscrds[0].col(0), (self.abscrds[0]-self.sizeMatr).col(0), (self.abscrds[0]+self.sizeMatr).col(0))
        print((self.abscrds[0]-self.sizeMatr).col(0))

    def set_coords(self):
        canv.coords(self.id, *(self.abscrds[0]-self.sizeMatr).col(0),
                             *(self.abscrds[0]+self.sizeMatr).col(0))


class Basis2D:
    def __init__(self, x=400, y=300, length=40):
        self.x = Line([(0, 0), (length, 0)], x, y, color='red')
        self.y = Line([(0, 0), (0, length)], x, y, color='green')

    def set_coords(self):
        self.x.set_coords()
        self.y.set_coords()

    def transform(self, func, *args, **kwargs):
        self.x.transform(func, *args, **kwargs)
        self.y.transform(func, *args, **kwargs)

    def rotate(self, angle):
        self.x.rotate(angle)
        self.y.rotate(angle)


class Polygon(Object):
    def __init__(self, crds, x=400, y=300):
        super().__init__(crds, x, y)
        self.id = canv.create_polygon(*crds_to_row(self.abscrds), fill='black')


class Rectangle(Polygon):
    def __init__(self, x=400, y=300, a=200, b=100):
        crds = [(-a/2, -b/2), (a/2, -b/2), (a/2, b/2), (-a/2, b/2)]
        super().__init__(crds, x, y)


class Link:
    """ This class allows you to 'link' objects, so you haven't to write the same methods for every object"""
    def __init__(self, *args):
        self.objects = args

    def set_coords(self):
        for obj in self.objects:
            obj.set_coords()

    def transform(self, func, *args, **kwargs):
        for obj in self.objects:
            obj.transform(func, *args, **kwargs)

    def rotate(self, angle):
        self.transform(M_rot, angle)


def crds_to_row(crds):
    """this function converts a list of matrices with coordinates to a row which can be used for tkinter methods."""
    row = []
    for matr in crds:
        row += matr.col(0)
    return row


'''These are transformation matrices. 
The columns of each matrix are coordinates of basis vectors after the transformation in the old system'''


def M_rot(a):
    new_matr = Matrix(2, 2, [[math.cos(a), math.sin(a)], [-math.sin(a), math.cos(a)]])
    return new_matr


def transform_1():  # increase x-size by two
    new_matr = Matrix(2, 2, [[2, 0], [0, 1]])
    return new_matr


def transform_2():  # shift y-coordinates to the x-axis direction
    new_matr = Matrix(2, 2, [[1, 1], [0, 1]])
    return new_matr


def transform_3(k):  # increase in size by k
    new_matr = Matrix(2, 2, [[k, 0], [0, k]])
    return new_matr


#  Rotation matrices for the 3D case.
# def rot_Mx(a):
#     m = Matrix(3, 3)
#     m.set([[1, 0, 0],
#            [0, math.cos(a), -math.sin(a)],
#            [0, math.sin(a), math.cos(a)]])
#     return m
#
#
# def rot_My(a):
#     m = Matrix(3, 3)
#     m.set([[math.cos(a), 0, math.sin(a)],
#            [0, 1, 0],
#            [-math.sin(a), 0, math.cos(a)]])
#     return m
#
#
# def rot_Mz(a):
#     m = Matrix(3, 3)
#     m.set([[math.cos(a), -math.sin(a), 0],
#            [math.sin(a), math.cos(a), 0],
#            [0, 0, 1]])
#     return m


stopped, rt, lt = None, True, None


def loop():
    def stop(event):
        global stopped
        stopped = True

    def left(event):
        global lt, rt, stopped
        lt, rt, stopped = True, False, False

    def right(event):
        global rt, lt, stopped
        rt, lt, stopped = True, False, False

    canv.bind_all('s', stop)
    canv.bind_all('a', left)
    canv.bind_all('d', right)

    canv.update()
    time.sleep(1)

    def main_transforms():
        polygon.transform(transform_3, 10)
        polygon.set_coords()

        rect.transform(transform_1)
        rect.set_coords()

        canv.update()
        time.sleep(1)

        polygon.rotate(math.pi/2)
        polygon.set_coords()

        rect.transform(transform_2)
        rect.set_coords()

        canv.update()
        time.sleep(1)

    def loop_rotation():
        if stopped is not True:
            rect.set_coords()

            if rt is True:
                rect.rotate(-math.pi/180)
            if lt is True:
                rect.rotate(math.pi/180)

            canv.update()
        root.after(5, loop_rotation)

    main_transforms()
    loop_rotation()


window_basis = Basis2D(5, 5)

polygon_crds = [(0, 20), (3, 17), (5, 5), (10, 0), (17, -5), (15, -6), (5, -5), (3, -2), (0, 0), (-4, 1), (-2, 10)]
polygon_obj = Polygon(polygon_crds, 100, 200)
polygon_basis = Basis2D(100, 200, length=2)
points_list = [Point([crd], 100, 200) for crd in polygon_crds]
polygon = Link(polygon_basis, polygon_obj, *points_list)

rect_obj = Rectangle()
basis = Basis2D()
rect = Link(rect_obj, basis)

loop()

mainloop()
