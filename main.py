"""
This is a basic example of using KekGL
Use 'a', 'w', 's', 'd' to move, arrows to rotate
"""


from tkinter import *
from KekGL import *
from models import pyramid_model
from math import cos, sin, pi

root = Tk()
fr = Frame(root)
root.geometry('800x600')
root.resizable(False, False)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


transform_1 = Matrix(4, 4, [
    [2, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 2, 0],
    [0, 0, -60, 1]
])

transform_w = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 4, 0, 1]
])

transform_a = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [4, 0, 0, 1]
])

transform_s = Matrix(4, 4, [
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


# this two matrices rotate camera relative to the world vertical axis
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
pyramid.toScreen()

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


p1 = canv.create_polygon(*pyramid.prims[0].s_crds[0], *pyramid.prims[0].s_crds[1],
                         *pyramid.prims[0].s_crds[2], *pyramid.prims[0].s_crds[3], outline='blue', width=2)
p2 = canv.create_polygon(*pyramid.prims[1].s_crds[0], *pyramid.prims[1].s_crds[1],
                         *pyramid.prims[1].s_crds[2], *pyramid.prims[1].s_crds[3], outline='green', width=2)
p3 = canv.create_polygon(*pyramid.prims[2].s_crds[0], *pyramid.prims[2].s_crds[1],
                         *pyramid.prims[2].s_crds[2], *pyramid.prims[2].s_crds[3], outline='blue', width=2)
p4 = canv.create_polygon(*pyramid.prims[3].s_crds[0], *pyramid.prims[3].s_crds[1],
                         *pyramid.prims[3].s_crds[2], *pyramid.prims[3].s_crds[3], outline='green', width=2)
p5 = canv.create_polygon(*pyramid.prims[4].s_crds[0], *pyramid.prims[4].s_crds[1],
                         *pyramid.prims[4].s_crds[2], *pyramid.prims[4].s_crds[3], outline='blue', width=2, fill='red')

prims_list = [p1, p2, p3, p4, p5]


# p6 = canv.create_polygon(*pyramid.prims[5].s_crds[0], *pyramid.prims[5].s_crds[1],
#                     *pyramid.prims[5].s_crds[2], *pyramid.prims[5].s_crds[3], outline='green', width=2)

def loop():
    global a, w, s, d, q, e, rot_up, rot_down, rot_left, rot_right, prims_list, angle
    # This will only work properly if the initial position of the camera was left the same!!!
    if w:
        pyramid.toWorld(transform_w)

    if a:
        pyramid.toWorld(transform_a)

    if s:
        pyramid.toWorld(transform_s)

    if d:
        pyramid.toWorld(transform_d)

    if q:
        pyramid.toWorld(transform_q)

    if e:
        pyramid.toWorld(transform_e)

    if rot_up and angle <= 1.5:
        angle += 0.1
        pyramid.toWorld(transform_rot_up)

    if rot_left:
        pyramid.toWorld(tr_rot_left(angle))

    if rot_down and angle >= -1.5:
        angle -= 0.1
        pyramid.toWorld(transform_rot_down)

    if rot_right:
        pyramid.toWorld(tr_rot_right(angle))

    pyramid.toCamera(matr_E(4))
    pyramid.toProjection(proj_matrix)
    pyramid.toNDC()

    if pyramid.isVisible():
        for i in range(5):
            canv.itemconfigure(prims_list[i], state='normal')
    else:
        for i in range(5):
            canv.itemconfigure(prims_list[i], state='hidden')

    pyramid.toScreen()

    canv.coords(p1, *pyramid.prims[0].s_crds[0], *pyramid.prims[0].s_crds[1],
                *pyramid.prims[0].s_crds[2], *pyramid.prims[0].s_crds[3], )
    canv.coords(p2, *pyramid.prims[1].s_crds[0], *pyramid.prims[1].s_crds[1],
                *pyramid.prims[1].s_crds[2], *pyramid.prims[1].s_crds[3], )
    canv.coords(p3, *pyramid.prims[2].s_crds[0], *pyramid.prims[2].s_crds[1],
                *pyramid.prims[2].s_crds[2], *pyramid.prims[2].s_crds[3], )
    canv.coords(p4, *pyramid.prims[3].s_crds[0], *pyramid.prims[3].s_crds[1],
                *pyramid.prims[3].s_crds[2], *pyramid.prims[3].s_crds[3], )
    canv.coords(p5, *pyramid.prims[4].s_crds[0], *pyramid.prims[4].s_crds[1],
                *pyramid.prims[4].s_crds[2], *pyramid.prims[4].s_crds[3], )
    # canv.coords(p6, *pyramid.prims[5].s_crds[0], *pyramid.prims[5].s_crds[1],
    #                     *pyramid.prims[5].s_crds[2], *pyramid.prims[5].s_crds[3],)

    canv.update()
    root.after(20, loop)


loop()

mainloop()
