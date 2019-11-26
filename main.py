"""
This is a basic example of using KekGL
Use 'a', 'w', 's', 'd' to move, arrows to rotate
"""


from tkinter import *
from KekGL import *
from models import pyramid_model, corner_model
from math import cos, sin, pi

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

root = Tk()
fr = Frame(root)
root.geometry(str(SCREEN_WIDTH)+'x'+str(SCREEN_HEIGHT))
root.resizable(False, False)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


transform_1 = Matrix(4, 4, [
    [2, 0, 0, 0],
    [0, 0, 2, 0],
    [0, -2, 0, 0],
    [0, 25, -80, 1]
])

transform_corner_start = Matrix(4, 4, [
    [2, 0, 0, 0],
    [0, 0, 2, 0],
    [0, -2, 0, 0],
    [0, 25, -400, 1]
])

transform_along_y1 = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 4, 0, 1]
])

transform_along_y2 = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, -4, 0, 1]
])

transform_d = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [-4, 0, 0, 1]
])

transform_a = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [4, 0, 0, 1]
])

transform_q = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 4, 1]
])

transform_e = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, -4, 1]
])

ang = 0.1

transform_rot_up = Matrix(4, 4, [
    [1, 0,       0,      0],
    [0, cos(ang),  sin(ang), 0],
    [0, -sin(ang), cos(ang), 0],
    [0, 0,       0,      1]
])

transform_rot_down = Matrix(4, 4, [
    [1, 0,        0,       0],
    [0, cos(-ang),  sin(-ang), 0],
    [0, -sin(-ang), cos(-ang), 0],
    [0, 0,        0,       1]
])


# these two matrices move camera along world's horizontal axis
def transform_w(phi):
    return Matrix(4, 4, [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, -2*sin(phi), 2*cos(phi), 1]
    ])


def transform_s(phi):
    return Matrix(4, 4, [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 2*sin(phi), -2*cos(phi), 1]
    ])


# these two matrices rotate camera relative to the world vertical axis
def tr_rot_right(phi):
    global ang
    c = cos(ang)
    s = sin(ang)
    anc = cos(phi)
    ans = sin(phi)
    return Matrix(4, 4, [
        [c,      s*ans,          -s*anc,         0],
        [-s*ans, anc**2*(1-c)+c, anc*ans*(1-c),  0],
        [s*anc,  anc*ans*(1-c),  ans**2*(1-c)+c, 0],
        [0,      0,              0,              1]
    ])


def tr_rot_left(phi):
    global ang
    c = cos(-ang)
    s = sin(-ang)
    anc = cos(phi)
    ans = sin(phi)
    return Matrix(4, 4, [
        [c,      s*ans,          -s*anc,         0],
        [-s*ans, anc**2*(1-c)+c, anc*ans*(1-c),  0],
        [s*anc,  anc*ans*(1-c),  ans**2*(1-c)+c, 0],
        [0,      0,              0,              1]
    ])


transform_rot_left = Matrix(4, 4, [
    [cos(-ang), 0, -sin(-ang), 0],
    [0,       1, 0,        0],
    [sin(-ang), 0, cos(-ang),  0],
    [0,       0, 0,        1]
])

transform_rot_right = Matrix(4, 4, [
    [cos(ang), 0, -sin(ang), 0],
    [0,      1, 0,       0],
    [sin(ang), 0, cos(ang),  0],
    [0,      0, 0,       1]
])

transform_rot_z1 = Matrix(4, 4, [
    [cos(ang),  sin(ang), 0, 0],
    [-sin(ang), cos(ang), 0, 0],
    [0,       0,      1, 0],
    [0,       0,      0, 1]
])

transform_rot_z2 = Matrix(4, 4, [
    [cos(ang),  sin(ang), 0, 0],
    [-sin(ang), cos(ang), 0, 0],
    [0,       0,      1, 0],
    [0,       0,      0, 1]
])


# coordinates of the view pyramid's vertices
l, t, r, b = -40, 30, 40, -30
n, f = 20, 100

proj_matrix = Matrix(4, 4, [
    [2*n/(r-l),   0,           0,             0],
    [0,           2*n/(t-b),   0,             0],
    [(r+l)/(r-l), (t+b)/(t-b), -(f+n)/(f-n), -1],
    [0,           0,           -2*f*n/(f-n),  0]
])

pyramid = Object(pyramid_model)
pyramid.toWorld(transform_1)
pyramid.toCamera(matr_E(4))
pyramid.toProjection(proj_matrix)
pyramid.toNDC()
pyramid.toScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
corner = Object(corner_model)
corner.toWorld(transform_corner_start)
corner.toCamera(matr_E(4))
corner.toProjection(proj_matrix)
corner.toNDC()
corner.toScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

a, w, s, d, q, e = False, False, False, False, False, False
rot_up, rot_down, rot_left, rot_right = False, False, False, False
angle = 0.0


def bindings():
    global a, w, s, d, q, e, rot_up, rot_down, rot_left, rot_right

    def move_w(event):
        global w
        if not w:
            w = True

    def move_s(event):
        global s
        if not s:
            s = True

    def move_a(event):
        global a
        if not a:
            a = True

    def move_d(event):
        global d
        if not d:
            d = True

    def move_q(event):
        global q
        if not q:
            q = True

    def move_e(event):
        global e
        if not e:
            e = True
            
    def move_rot_up(event):
        global rot_up
        if not rot_up:
            rot_up = True
    
    def move_rot_down(event):
        global rot_down
        if not rot_down:
            rot_down = True
            
    def move_rot_left(event):
        global rot_left
        if not rot_left:
            rot_left = True
            
    def move_rot_right(event):
        global rot_right
        if not rot_right:
            rot_right = True

    def stop_w(event):
        global w
        w = False

    def stop_s(event):
        global s
        s = False

    def stop_a(event):
        global a
        a = False

    def stop_d(event):
        global d
        d = False

    def stop_q(event):
        global q
        q = False

    def stop_e(event):
        global e
        e = False

    def stop_rot_up(event):
        global rot_up
        rot_up = False
        
    def stop_rot_down(event):
        global rot_down
        rot_down = False
        
    def stop_rot_left(event):
        global rot_left
        rot_left = False
        
    def stop_rot_right(event):
        global rot_right
        rot_right = False

    root.bind('w', move_w)
    root.bind('s', move_s)
    root.bind('a', move_a)
    root.bind('d', move_d)
    root.bind('q', move_q)
    root.bind('e', move_e)
    root.bind('<Up>', move_rot_up)
    root.bind('<Down>', move_rot_down)
    root.bind('<Left>', move_rot_left)
    root.bind('<Right>', move_rot_right)
    root.bind('<KeyRelease-w>', stop_w)
    root.bind('<KeyRelease-s>', stop_s)
    root.bind('<KeyRelease-a>', stop_a)
    root.bind('<KeyRelease-d>', stop_d)
    root.bind('<KeyRelease-q>', stop_q)
    root.bind('<KeyRelease-e>', stop_e)
    root.bind('<KeyRelease-Up>', stop_rot_up)
    root.bind('<KeyRelease-Down>', stop_rot_down)
    root.bind('<KeyRelease-Left>', stop_rot_left)
    root.bind('<KeyRelease-Right>', stop_rot_right)


bindings()


def toCanv(prim):
    crds_row = []
    for i in range(prim.s_crds.rows):
        crds_row += prim.s_crds[i]
    return crds_row


p1 = canv.create_polygon(*toCanv(pyramid.prims[0]), outline='blue', width=2, fill='green')
p2 = canv.create_polygon(*toCanv(pyramid.prims[1]), outline='green', width=2)
p3 = canv.create_polygon(*toCanv(pyramid.prims[2]), outline='blue', width=2)
p4 = canv.create_polygon(*toCanv(pyramid.prims[3]), outline='green', width=2)
p5 = canv.create_polygon(*toCanv(pyramid.prims[4]), outline='blue', width=2, fill='red')

c1 = canv.create_polygon(*toCanv(corner.prims[0]), outline='blue', width=2, fill='yellow')
c2 = canv.create_polygon(*toCanv(corner.prims[1]), outline='green', width=2)
c3 = canv.create_polygon(*toCanv(corner.prims[2]), outline='blue', width=2)
c4 = canv.create_polygon(*toCanv(corner.prims[3]), outline='green', width=2)

prims_list = [p1, p2, p3, p4, p5]
prims_corner_list = [c1, c2, c3, c4]


# p6 = canv.create_polygon(*pyramid.prims[5].s_crds[0], *pyramid.prims[5].s_crds[1],
#                     *pyramid.prims[5].s_crds[2], *pyramid.prims[5].s_crds[3], outline='green', width=2)


def loop():
    global a, w, s, d, q, e, rot_up, rot_down, rot_left, rot_right, prims_list, angle
    # This will only work properly if the initial position of the camera was left the same!!!
    if w:
        pyramid.toWorld(transform_w(angle))
        corner.toWorld(transform_w(angle))

    if a:
        pyramid.toWorld(transform_a)
        corner.toWorld(transform_a)

    if s:
        pyramid.toWorld(transform_s(angle))
        corner.toWorld(transform_s(angle))

    if d:
        pyramid.toWorld(transform_d)
        corner.toWorld(transform_d)

    if q:
        pyramid.toWorld(transform_q)
        corner.toWorld(transform_q)

    if e:
        pyramid.toWorld(transform_e)
        corner.toWorld(transform_e)

    if rot_up and angle <= 1.5:
        angle += 0.1
        pyramid.toWorld(transform_rot_up)
        corner.toWorld(transform_rot_up)

    if rot_left:
        pyramid.toWorld(tr_rot_left(angle))
        corner.toWorld(tr_rot_left(angle))

    if rot_down and angle >= -1.5:
        angle -= 0.1
        pyramid.toWorld(transform_rot_down)
        corner.toWorld(transform_rot_down)

    if rot_right:
        pyramid.toWorld(tr_rot_right(angle))
        corner.toWorld(tr_rot_right(angle))

    pyramid.toCamera(matr_E(4))
    pyramid.toProjection(proj_matrix)
    pyramid.toNDC()
    corner.toCamera(matr_E(4))
    corner.toProjection(proj_matrix)
    corner.toNDC()

    pyramid.toScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
    corner.toScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
    canv.coords(p1, *toCanv(pyramid.prims[0]))
    canv.coords(p2, *toCanv(pyramid.prims[1]))
    canv.coords(p3, *toCanv(pyramid.prims[2]))
    canv.coords(p4, *toCanv(pyramid.prims[3]))
    canv.coords(p5, *toCanv(pyramid.prims[4]))
    # canv.coords(p6, *toCanv(pyramid.prims[5]))

    canv.coords(c1, *toCanv(corner.prims[0]))
    canv.coords(c2, *toCanv(corner.prims[1]))
    canv.coords(c3, *toCanv(corner.prims[2]))
    canv.coords(c4, *toCanv(corner.prims[3]))

    canv.update()
    root.after(20, loop)


loop()

mainloop()
