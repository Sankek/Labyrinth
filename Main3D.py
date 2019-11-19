"""
It's like the pseudo 3D.

Press 'a', 'w', 's', 'd' to move in 4-directions
Press 'z', 'x', 'c', 'v' to start rotating like in 3D
"""

from tkinter import *
from Matrix import *
from time import time, sleep
import math

root = Tk()
fr = Frame(root)
root.geometry('800x600')
root.resizable(False, False)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class Object:
    """
    This class describes 3D-objects methods to transform
    """
    def __init__(self, crds, x=400, y=300, z=0):
        self.center = Matrix(3, 1, [[x], [y], [z]])
        self.crds = [Matrix(3, 1, [[x], [y], [z]]) for x, y, z in crds]
        self.abscrds = [matr+self.center for matr in self.crds]

    def set_coords(self):
        canv.coords(self.id, *crds_to_row(self.abscrds))

    def transform(self, func, *args, **kwargs):
        self.crds = [func(*args, **kwargs)*matr for matr in self.crds]
        self.abscrds = [matr+self.center for matr in self.crds]

    def rotate(self, angle):
        self.transform(M_rot, angle)


class Line(Object):
    def __init__(self, crds, x=400, y=300, z=0, color='black', width=0):
        super().__init__(crds, x, y, z)
        self.id = canv.create_line(*crds_to_row(self.abscrds), fill=color, width=width)


class Point(Object):
    def __init__(self, crd, x=400, y=300, z=0, color='red', size=2):
        super().__init__(crd, x, y, z)
        self.sizeMatr = Matrix(3, 1, [[size], [size], [size]])
        self.id = canv.create_oval(*(self.abscrds[0]-self.sizeMatr).col(0)[:2],
                                   *(self.abscrds[0]+self.sizeMatr).col(0)[:2], fill=color, width=0)

    def set_coords(self):
        canv.coords(self.id, *(self.abscrds[0]-self.sizeMatr).col(0)[:2],
                             *(self.abscrds[0]+self.sizeMatr).col(0)[:2])


class Basis3D:
    def __init__(self, x=400, y=300, z=0, length=40):
        self.center = Matrix(3, 1, [[x], [y], [z]])
        self.x = Line([(0, 0, 0), (length, 0, 0)], x, y, z, color='red')
        self.y = Line([(0, 0, 0), (0, length, 0)], x, y, z, color='green')
        self.z = Line([(0, 0, 0), (0, 0, length)], x, y, z, color='blue')
        self.x.center = self.y.center = self.z.center = self.center

    def set_coords(self):
        self.x.set_coords()
        self.y.set_coords()
        self.z.set_coords()
        self.x.center = self.y.center = self.z.center = self.center

    def transform(self, func, *args, **kwargs):
        self.x.transform(func, *args, **kwargs)
        self.y.transform(func, *args, **kwargs)
        self.z.transform(func, *args, **kwargs)
        self.x.center = self.y.center = self.z.center = self.center

    def rotate(self, angle):
        self.x.rotate(angle)
        self.y.rotate(angle)
        self.z.rotate(angle)


class Polygon(Object):
    def __init__(self, crds, x=400, y=300, z=0, color='black'):
        super().__init__(crds, x, y, z)
        self.id = canv.create_polygon(*crds_to_row(self.abscrds), fill=color)


class Rectangle(Polygon):
    def __init__(self, x=400, y=300, z=0, a=200, b=100):
        crds = [(-a/2, -b/2, 0), (a/2, -b/2, 0), (a/2, b/2, 0), (-a/2, b/2, 0)]
        super().__init__(crds, x, y, z)


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

    def add_to_center(self, matr):
        for obj in self.objects:
            obj.center += matr
            if isinstance(obj, Basis3D):
                obj.x.abscrds = [matr+obj.x.center for matr in obj.x.crds]
                obj.y.abscrds = [matr+obj.y.center for matr in obj.y.crds]
                obj.z.abscrds = [matr+obj.z.center for matr in obj.z.crds]
            else:
                obj.abscrds = [matr+obj.center for matr in obj.crds]
        self.set_coords()


def crds_to_row(crds):
    """this function converts a list of matrices with coordinates to a row which can be used for tkinter methods."""
    row = []
    for matr in crds:
        row += matr[0] + matr[1]
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
def rot_Mx(a):
    m = Matrix(3, 3)
    m.set([[1, 0, 0],
           [0, math.cos(a), -math.sin(a)],
           [0, math.sin(a), math.cos(a)]])
    return m


def rot_My(a):
    m = Matrix(3, 3)
    m.set([[math.cos(a), 0, math.sin(a)],
           [0, 1, 0],
           [-math.sin(a), 0, math.cos(a)]])
    return m


def rot_Mz(a):
    m = Matrix(3, 3)
    m.set([[math.cos(a), -math.sin(a), 0],
           [math.sin(a), math.cos(a), 0],
           [0, 0, 1]])
    return m


def rot_M_general(a, x, y, z):  # Rotation matrix relative to the axis with vector (x, y, z)
    m = Matrix(3, 3)
    m.set([[math.cos(a)+(1-math.cos(a))*x**2, (1-math.cos(a))*x*y-math.sin(a)*z, (1-math.cos(a))*x*z+math.sin(a)*y],
           [(1-math.cos(a))*x*y+math.sin(a)*z, math.cos(a)+(1-math.cos(a))*y**2, (1-math.cos(a))*z*y-math.sin(a)*x],
           [(1-math.cos(a))*x*z-math.sin(a)*y, (1-math.cos(a))*z*y+math.sin(a)*x, math.cos(a)+(1-math.cos(a))*z**2]])
    # m[0] = [math.cos(a)+(1-math.cos(a))*x**2, (1-math.cos(a))*x*y-math.sin(a)*z, (1-math.cos(a))*x*z+math.sin(a)*y]
    # m[1] = [(1-math.cos(a))*x*y+math.sin(a)*z, math.cos(a)+(1-math.cos(a))*y**2, (1-math.cos(a))*z*y-math.sin(a)*x]
    # m[2] = [(1-math.cos(a))*x*z-math.sin(a)*y, (1-math.cos(a))*z*y+math.sin(a)*x, math.cos(a)+(1-math.cos(a))*z**2]

    return m


def bindings():
    def b_trans1(event):
        global trans1
        trans1 = True

    def bs_trans1(event):
        global trans1
        trans1 = False

    def b_trans2(event):
        global trans2
        trans2 = True

    def bs_trans2(event):
        global trans2
        trans2 = False

    def b_trans3(event):
        global trans3
        trans3 = True

    def bs_trans3(event):
        global trans3
        trans3 = False
        
    def b_trans4(event):
        global trans4
        trans4 = True

    def bs_trans4(event):
        global trans4
        trans4 = False

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
    canv.bind_all('v', b_trans4)
    canv.bind_all('<KeyRelease-v>', bs_trans4)


rt, lt, up, dn, trans1, trans2, trans3, trans4 = False, False, False, False, False, False, False, False
bindings()


def loop():
    global k
    canv.update()
    sleep(1)

    def main_transforms():
        pass

    k=0

    def loop_rotation():
        global k
        start_time = time()
        if rt or lt or up or dn or trans1 or trans2 or trans3 or trans4 is True:


            if trans1 is True:
                new_poly.transform(rot_Mx, math.pi/180*5)
                new_poly_1.transform(rot_Mx, math.pi/180*5)
                new_poly_2.transform(rot_Mx, math.pi/180*5)
                new_poly_3.transform(rot_Mx, math.pi/180*5)
            if trans2 is True:
                new_poly.transform(rot_My, math.pi/180*25)
                new_poly_1.transform(rot_My, math.pi/180*5)
                new_poly_2.transform(rot_My, math.pi/180*5)
                new_poly_3.transform(rot_My, math.pi/180*5)
            if trans3 is True:
                new_poly.transform(rot_Mz, math.pi/180*5)
                new_poly_1.transform(rot_Mz, math.pi/180*5)
                new_poly_2.transform(rot_Mz, math.pi/180*5)
                new_poly_3.transform(rot_Mz, math.pi/180*5)
            if trans4 is True:
                new_poly.transform(rot_M_general, math.pi/180, new_basis.y.crds[1][0][0], new_basis.y.crds[1][1][0], new_basis.y.crds[1][2][0])
                # new_poly.transform(rot_M_general, 0.01, 2, 4, 3)
            if up is True:
                new_poly.add_to_center(Matrix(3, 1, [[0], [-1], [0]]))
            if dn is True:
                new_poly.add_to_center(Matrix(3, 1, [[0], [1], [0]]))
            if lt is True:
                new_poly.add_to_center(Matrix(3, 1, [[-1], [0], [0]]))
            if rt is True:
                new_poly.add_to_center(Matrix(3, 1, [[1], [0], [0]]))


            new_poly.set_coords()
            new_poly_1.set_coords()
            new_poly_2.set_coords()
            new_poly_3.set_coords()
            # canv.update()  # without it animation also works but it's less laggy
        print(round((time()-start_time)*1000, 1), 'ms')
        root.after(20, loop_rotation)

    main_transforms()

    loop_rotation()



window_basis = Basis3D(5, 5)

# polygon_crds = [(0, 20), (3, 17), (5, 5), (10, 0), (17, -5), (15, -6), (5, -5), (3, -2), (0, 0), (-4, 1), (-2, 10)]
# polygon_obj = Polygon(polygon_crds, 100, 200)
# polygon_basis = Basis2D(100, 200, length=2)
# points_list = [Point([crd], 100, 200) for crd in polygon_crds]
# polygon = Link(polygon_basis, polygon_obj, *points_list)

# rect_obj = Rectangle()
# basis = Basis2D()
# rect = Link(rect_obj, basis)

new_crds = [(40, 40, 0), (-40, 40, 0), (-40, -40, 0), (40, -40, 0)]
new_new_crds = [(40, 40, 80), (-40, 40, 80), (-40, -40, 80), (40, -40, 80)]
line_crds = [(40, 40, 0), (40, 40, 80), (-40, 40, 0), (-40, 40, 80),
             (-40, -40, 0), (-40, -40, 80), (40, -40, 0), (40, -40, 80)]

points_list = [Point([crd]) for crd in new_crds]
points_new_plane_list = [Point([crd]) for crd in new_new_crds]
new_poly_obj = Polygon(new_crds, color='grey')
new_poly_new_plane_obj = Polygon(new_new_crds)
lines = [Line([x, y], width=3) for x, y in zip(line_crds[::2], line_crds[1::2])]
new_basis = Basis3D()
new_poly = Link(new_basis, new_poly_obj, *points_list, new_poly_new_plane_obj, *points_new_plane_list, *lines)

points_list_1 = [Point([crd], 100, 100) for crd in new_crds]
points_new_plane_list_1 = [Point([crd], 100, 100) for crd in new_new_crds]
new_poly_obj_1 = Polygon(new_crds, 100, 100, color='grey')
new_poly_new_plane_obj_1 = Polygon(new_new_crds, 100, 100)
lines_1 = [Line([x, y], 100, 100, width=3) for x, y in zip(line_crds[::2], line_crds[1::2])]
new_basis_1 = Basis3D(100, 100)
new_poly_1 = Link(new_basis_1, new_poly_obj_1, *points_list_1, new_poly_new_plane_obj_1, *points_new_plane_list_1, *lines_1)

points_list_2 = [Point([crd], 100, 300) for crd in new_crds]
points_new_plane_list_2 = [Point([crd], 100, 300) for crd in new_new_crds]
new_poly_obj_2 = Polygon(new_crds, 100, 300, color='grey')
new_poly_new_plane_obj_2 = Polygon(new_new_crds, 100, 300)
lines_2 = [Line([x, y], 100, 300, width=3) for x, y in zip(line_crds[::2], line_crds[1::2])]
new_basis_2 = Basis3D(100, 300)
new_poly_2 = Link(new_basis_2, new_poly_obj_2, *points_list_2, new_poly_new_plane_obj_2, *points_new_plane_list_2, *lines_2)

points_list_3 = [Point([crd], 300, 100) for crd in new_crds]
points_new_plane_list_3 = [Point([crd], 300, 100) for crd in new_new_crds]
new_poly_obj_3 = Polygon(new_crds, 300, 100, color='grey')
new_poly_new_plane_obj_3 = Polygon(new_new_crds, 300, 100)
lines_3 = [Line([x, y], 300, 100, width=3) for x, y in zip(line_crds[::2], line_crds[1::2])]
new_basis_3 = Basis3D(300, 100)
new_poly_3 = Link(new_basis_3, new_poly_obj_3, *points_list_3, new_poly_new_plane_obj_3, *points_new_plane_list_3, *lines_3)

loop()

mainloop()
