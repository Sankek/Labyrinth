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
    def __init__(self, crds, x=400, y=300, color='black', width=0):
        super().__init__(crds, x, y)
        self.id = canv.create_line(*crds_to_row(self.abscrds), fill=color, width=width)


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
    def __init__(self, x=400, y=300, length=40, width=0):
        self.x = Line([(0, 0), (length, 0)], x, y, color='red', width=width)
        self.y = Line([(0, 0), (0, length)], x, y, color='green', width=width)

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


def transform_4():
    new_matr = Matrix(2, 2, [[-1, 0], [0, 1]])
    return new_matr


def transform_5(k):
    new_matr = Matrix(2, 2, [[-0.5, 0], [0, 0.5]])
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

def bindings():
    def b_trans1(event):
        global trans1
        trans1 = True

        def smooth(k):
            for i in range(50):
                grid.transform(transform_3, k/100)
                grid.set_coords()
                canv.update()
                time.sleep(0.02)

            grid.transform(transform_4)
            grid.set_coords()
            canv.update()
            time.sleep(0.02)

            for i in range(50):
                grid.transform(transform_3, 100/k)
                grid.set_coords()
                canv.update()
                time.sleep(0.02)

        smooth(90)

    def bs_trans1(event):
        global trans1
        trans1 = False

    def b_trans2(event):
        global trans2
        trans2 = True

        def smooth(k):
            for i in range(50):
                new_basis.transform(transform_3, k/100)
                new_basis.set_coords()
                canv.update()
                time.sleep(0.02)

            new_basis.transform(transform_4)
            new_basis.set_coords()
            canv.update()
            time.sleep(0.02)

            for i in range(50):
                new_basis.transform(transform_3, 100/k)
                new_basis.set_coords()
                canv.update()
                time.sleep(0.02)

        smooth(95)

    def bs_trans2(event):
        global trans2
        trans2 = False

    def b_trans3(event):
        global trans3
        trans3 = True

    def bs_trans3(event):
        global trans3
        trans3 = False

    def b_left(event):
        global lt
        lt = True

    def bs_left(event):
        global lt
        lt = False

    def b_right(event):
        global rt
        rt = True

    def bs_right(event):
        global rt
        rt = False

    def b_up(event):
        global up
        up = True

    def bs_up(event):
        global up
        up = False

    def b_down(event):
        global dn
        dn = True

    def bs_down(event):
        global dn
        dn = False

    canv.bind_all('a', b_left)
    canv.bind_all('<KeyRelease-a>', bs_left)
    canv.bind_all('d', b_right)
    canv.bind_all('<KeyRelease-d>', bs_right)
    canv.bind_all('w', b_up)
    canv.bind_all('<KeyRelease-w>', bs_up)
    canv.bind_all('s', b_down)
    canv.bind_all('<KeyRelease-s>', bs_down)
    canv.bind_all('z', b_trans1)
    canv.bind_all('<KeyRelease-z>', bs_trans1)
    canv.bind_all('x', b_trans2)
    canv.bind_all('<KeyRelease-x>', bs_trans2)
    canv.bind_all('c', b_trans3)
    canv.bind_all('<KeyRelease-c>', bs_trans3)


rt, lt, up, dn, trans1, trans2, trans3 = False, False, False, False, False, False, False
bindings()


def loop():
    canv.update()
    time.sleep(1)

    def main_transforms():
        pass

    def loop_rotation():
        canv.update()
        root.after(5, loop_rotation)

    main_transforms()
    loop_rotation()


window_basis = Basis2D(5, 5)


vert_list = [(-400, -280), (400, -280), (-400, -240), (400, -240), (-400, -200), (400, -200), (-400, -160), (400, -160), (-400, -120), (400, -120), (-400, -80), (400, -80), (-400, -40), (400, -40), (-400, 0), (400, 0), (-400, 40), (400, 40), (-400, 80), (400, 80), (-400, 120), (400, 120), (-400, 160), (400, 160), (-400, 200), (400, 200), (-400, 240), (400, 240), (-400, 280), (400, 280)]
hor_list = [(-360, -300), (-360, 300), (-320, -300), (-320, 300), (-280, -300), (-280, 300), (-240, -300), (-240, 300), (-200, -300), (-200, 300), (-160, -300), (-160, 300), (-120, -300), (-120, 300), (-80, -300), (-80, 300), (-40, -300), (-40, 300), (0, -300), (0, 300), (40, -300), (40, 300), (80, -300), (80, 300), (120, -300), (120, 300), (160, -300), (160, 300), (200, -300), (200, 300), (240, -300), (240, 300), (280, -300), (280, 300), (320, -300), (320, 300), (360, -300), (360, 300)]


hor_lines = [Line([x, y]) for x, y in zip(hor_list[::2], hor_list[1::2])]
vert_lines = [Line([x, y]) for x, y in zip(vert_list[::2], vert_list[1::2])]
basis = Basis2D(width=2)

point = Point([(40, 80)])
grid = Link(basis, *hor_lines, *vert_lines, point)

new_basis = Basis2D(width=4, length=20)


loop()

mainloop()
