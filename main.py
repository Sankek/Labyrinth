"""
This is a basic example of using KekGL
Use 'a', 'w', 's', 'd', 'q', 'e' to move
"""


from tkinter import *
from KekGL import *
from models import pyramid_model

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
    [0, 1, 0, 1]
])

transform_a = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1]
])

transform_s = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, -1, 0, 1]
])

transform_d = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [-1, 0, 0, 1]
])

transform_q = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1]
])

transform_e = Matrix(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, -1, 1]
])

# coordinates of the view pyramid's vertices
l, t, r, b = -40, 30, 40, -30
n, f = 20, 100

proj_matrix = Matrix(4, 4, [
    [2*n/(r-l), 0, 0, 0],
    [0, 2*n/(t-b), 0, 0],
    [(r+l)/(r-l), (t+b)/(t-b), -(f+n)/(f-n), -1],
    [0, 0, -2*f*n/(f-n), 0]
])

pyramid = Object(pyramid_model)
pyramid.toWorld(transform_1)
pyramid.toCamera(matr_E(4))
pyramid.toProjection(proj_matrix)
pyramid.toNDC()
pyramid.toScreen()

a, w, s, d, q, e = False, False, False, False, False, False


def bindings():
    global a, w, s, d, q, e

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

    root.bind('w', move_w)
    root.bind('s', move_s)
    root.bind('a', move_a)
    root.bind('d', move_d)
    root.bind('q', move_q)
    root.bind('e', move_e)
    root.bind('<KeyRelease-w>', stop_w)
    root.bind('<KeyRelease-s>', stop_s)
    root.bind('<KeyRelease-a>', stop_a)
    root.bind('<KeyRelease-d>', stop_d)
    root.bind('<KeyRelease-q>', stop_q)
    root.bind('<KeyRelease-e>', stop_e)


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


# p6 = canv.create_polygon(*pyramid.prims[5].s_crds[0], *pyramid.prims[5].s_crds[1],
#                     *pyramid.prims[5].s_crds[2], *pyramid.prims[5].s_crds[3], outline='green', width=2)


def loop():
    global a, w, s, d, q, e
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

    pyramid.toCamera(matr_E(4))
    pyramid.toProjection(proj_matrix)
    pyramid.toNDC()
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
    root.after(10, loop)


loop()

mainloop()
