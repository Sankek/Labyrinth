"""
It's a base for a future 3D game.

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


def crds_to_row(crds):
    row = []
    for matr in crds:
        row += matr.transpose()[0]
    return row


class Basis2D:
    def __init__(self, x=400, y=300):
        self.center = Matrix(2, 1, [[x], [y]])
        self.crds_x = [None]*2
        for i in range(2):
            self.crds_x[i] = Matrix(2, 1)
        self.crds_x[0].set_col(0, [0, 0])
        self.crds_x[1].set_col(0, [20, 0])
        
        self.crds_y = [None]*2
        for i in range(2):
            self.crds_y[i] = Matrix(2, 1)
        self.crds_y[0].set_col(0, [0, 0])
        self.crds_y[1].set_col(0, [0, 20])

        self.abscrds_x = [None]*2
        for i in range(2):
            self.abscrds_x[i] = self.crds_x[i] + self.center

        self.abscrds_y = [None]*2
        for i in range(2):
            self.abscrds_y[i] = self.crds_y[i] + self.center

        self.id_x = canv.create_line(*crds_to_row(self.abscrds_x), fill='red')
        self.id_y = canv.create_line(*crds_to_row(self.abscrds_y), fill='green')
        self.center.print()

    def set_coords(self):
        for i in range(2):
            self.abscrds_x[i] = self.crds_x[i]+self.center
        for i in range(2):
            self.abscrds_y[i] = self.crds_y[i]+self.center
        canv.coords(self.id_x, *crds_to_row(self.abscrds_x), *crds_to_row(self.abscrds_x))
        canv.coords(self.id_y, *crds_to_row(self.abscrds_y), *crds_to_row(self.abscrds_y))

    def transform(self, func, *args, **kwargs):
        for i in range(2):
            self.crds_x[i] = func(*args, **kwargs)*self.crds_x[i]
            self.crds_y[i] = func(*args, **kwargs)*self.crds_y[i]

    def rotate(self, angle):
        self.transform(M_rot, angle)


class Rectangle:
    def __init__(self, x=400, y=300, a=200, b=100, angle=0.0):
        self.center = Matrix(2, 1, [[x], [y]])
        self.side_a = a
        self.side_b = b

        self.crds = [None]*4
        for i in range(4):
            self.crds[i] = Matrix(2, 1)
        self.crds[0].set_col(0, [-a/2, -b/2])
        self.crds[1].set_col(0, [a/2, -b/2])
        self.crds[2].set_col(0, [a/2, b/2])
        self.crds[3].set_col(0, [-a/2, b/2])

        self.rotate(angle)

        self.abscrds = [None]*4
        for i in range(4):
            self.abscrds[i] = self.crds[i] + self.center

        self.id = canv.create_polygon(*crds_to_row(self.abscrds),  fill='black')

    def set_coords(self):
        for i in range(4):
            self.abscrds[i] = self.crds[i]
            self.abscrds[i] += self.center
        canv.coords(self.id, *crds_to_row(self.abscrds))

    def transform(self, func, *args, **kwargs):
        for i in range(4):
            self.crds[i] = func(*args, **kwargs)*self.crds[i]

    def rotate(self, angle):
        self.transform(M_rot, angle)


def M_rot(a):
    new_matr = Matrix(2, 2, [[math.cos(a), math.sin(a)], [-math.sin(a), math.cos(a)]])
    return new_matr


def transform_1():
    new_matr = Matrix(2, 2, [[2, 0], [0, 1]])
    return new_matr


def transform_2():
    new_matr = Matrix(2, 2, [[1, 1], [0, 1]])
    return new_matr


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
#
#
# C = rot_Mx(math.pi / 2) * rot_My(math.pi / 2) * rot_Mz(math.pi / 2)
# C.print()
# print('-----')
# coords = Matrix(3, 1)
# coords.set_col(0, [1, 0, 0])
# coords.print()
# print('---')
# new_coords = C * coords
# new_coords.print()


stopped, rt, lt = None, None, None


def loop():
    def stop(event):
        global stopped
        stopped = True

    def left(event):
        global lt, rt
        lt = True
        rt = False

    def right(event):
        global rt, lt
        rt = True
        lt = False

    canv.bind_all('s', stop)
    canv.bind_all('a', left)
    canv.bind_all('d', right)

    canv.update()
    time.sleep(1)

    rect.transform(transform_1)
    rect.set_coords()
    basis.transform(transform_1)
    basis.set_coords()

    canv.update()
    time.sleep(1)

    rect.transform(transform_2)
    rect.set_coords()
    basis.transform(transform_2)
    basis.set_coords()

    canv.update()
    time.sleep(1)

    while stopped is not True:
        rect.set_coords()
        basis.set_coords()

        if rt is True:
            rect.rotate(-math.pi/180)
            basis.rotate(-math.pi/180)
        if lt is True:
            rect.rotate(math.pi/180)
            basis.rotate(math.pi/180)

        canv.update()
        time.sleep(0.02)


rect = Rectangle()
basis = Basis2D()
loop()

mainloop()
