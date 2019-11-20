"""
a,w,s,d to move
"""

from tkinter import *
from tkinter import _flatten

root = Tk()
fr = Frame(root)
root.geometry('800x600')
root.resizable(False, False)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

canv.create_line(400, 0, 400, 600)
canv.create_line(0, 300, 800, 300)

crds_1 = [[20, 100, 100], [40, 100, 100], [40, 100, -100], [20, 100, -100]]
crds_2 = [[20, -100, 100], [40, -100, 100], [40, -100, -100], [20, -100, -100]]


def proj(k, crds_l):
    ncrd = []
    for i in range(len(crds_l)):
        y = k*crds_l[i][1]/(crds_l[i][0]+k)
        z = k*crds_l[i][2]/(crds_l[i][0]+k)
        ncrd += [[y, z]]
    return ncrd


k = 5
ncrd_1 = proj(k, crds_1)
ncrd_2 = proj(k, crds_2)
print(*ncrd_1)


def tocanv(crd):
    l = [[k for k in i] for i in crd]
    for i in range(len(l)):
        l[i][0] += 400
        l[i][1] += 300
    return l


obj_1 = canv.create_polygon(*tocanv(ncrd_1), fill='green', outline='black', width=3)
obj_2 = canv.create_polygon(*tocanv(ncrd_2), fill='blue', outline='black', width=5)

a, w, s, d = False, False, False, False


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


root.bind('w', move_w)
root.bind('s', move_s)
root.bind('a', move_a)
root.bind('d', move_d)
root.bind('<KeyRelease-w>', stop_w)
root.bind('<KeyRelease-s>', stop_s)
root.bind('<KeyRelease-a>', stop_a)
root.bind('<KeyRelease-d>', stop_d)


def loop():
    global ncrd_1, ncrd_2, a, w, s, d
    if w:
        for i in range(len(crds_1)):
            crds_1[i][0] -= 0.3
            ncrd_1 = proj(k, crds_1)
            crds_2[i][0] -= 0.3
            ncrd_2 = proj(k, crds_2)

    if s:
        for i in range(len(crds_1)):
            crds_1[i][0] += 0.3
            ncrd_1 = proj(k, crds_1)
            crds_2[i][0] += 0.3
            ncrd_2 = proj(k, crds_2)

    if a:
        for i in range(len(crds_1)):
            crds_1[i][1] += 8
            ncrd_1 = proj(k, crds_1)
            crds_2[i][1] += 8
            ncrd_2 = proj(k, crds_2)

    if d:
        for i in range(len(crds_1)):
            crds_1[i][1] -= 8
            ncrd_1 = proj(k, crds_1)
            crds_2[i][1] -= 8
            ncrd_2 = proj(k, crds_2)

    canv.coords(obj_1, _flatten(tocanv(ncrd_1)))
    canv.coords(obj_2, _flatten(tocanv(ncrd_2)))
    canv.update()
    root.after(20, loop)


loop()
canv.update()
mainloop()