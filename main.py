
"""
This is a basic example of using KekGL
Use 'a', 'w', 's', 'd' to move, arrows to rotate
"""

from tkinter import *
from KekGL import *
from models import pyramid_model, corner_model
from math import cos, sin, pi
from time import time

root = Tk()

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

root.attributes('-fullscreen', True)
root.config(cursor="none")
# root.geometry(str(SCREEN_WIDTH)+'x'+str(SCREEN_HEIGHT))
# root.resizable(False, False)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

transform_1 = Matrix(4, 4, [
    [2, 0, 0, 0],
    [0, 0, -2, 0],
    [0, -2, 0, 0],
    [20, 25, -70, 1]
])

transform_corner_start = Matrix(4, 4, [
    [2, 0, 0, 0],
    [0, 0, -2, 0],
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

ang = 0.04

transform_rot_up = Matrix(4, 4, [
    [1, 0,       0,      0],
    [0, cos(-ang),  sin(-ang), 0],
    [0, -sin(-ang), cos(-ang), 0],
    [0, 0,       0,      1]
])

transform_rot_down = Matrix(4, 4, [
    [1, 0,        0,       0],
    [0, cos(ang),  sin(ang), 0],
    [0, -sin(ang), cos(ang), 0],
    [0, 0,        0,       1]
])


def transform_rot_y(angle):
    return Matrix(4, 4, [
        [1, 0, 0, 0],
        [0, cos(angle), sin(angle), 0],
        [0, -sin(angle), cos(angle), 0],
        [0, 0, 0, 1]
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


def tr_rot_left(phi):
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


def transform_rot_x(angle, deviation_angle):
    c = cos(angle)
    s = -sin(angle)
    anc = cos(deviation_angle)
    ans = sin(deviation_angle)
    return Matrix(4, 4, [
        [c, s*ans, -s*anc, 0],
        [-s*ans, anc**2*(1-c)+c, anc*ans*(1-c), 0],
        [s*anc, anc*ans*(1-c), ans**2*(1-c)+c, 0],
        [0, 0, 0, 1]
    ])


transform_rot_left = Matrix(4, 4, [
    [cos(ang), 0, -sin(ang), 0],
    [0,       1, 0,        0],
    [sin(ang), 0, cos(ang),  0],
    [0,       0, 0,        1]
])

transform_rot_right = Matrix(4, 4, [
    [cos(-ang), 0, -sin(-ang), 0],
    [0,      1, 0,       0],
    [sin(-ang), 0, cos(-ang),  0],
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
l, t, r, b = -SCREEN_WIDTH/20, SCREEN_HEIGHT/20, SCREEN_WIDTH/20, -SCREEN_HEIGHT/20
n, f = 70, 100


proj_matrix = Matrix(4, 4, [
    [2*n/(r-l),   0,           0,             0],
    [0,           2*n/(t-b),   0,             0],
    [(r+l)/(r-l), (t+b)/(t-b), -(f+n)/(f-n), -1],
    [0,           0,           -2*f*n/(f-n),  0]
])

a, w, s, d, q, e = False, False, False, False, False, False
rot_up, rot_down, rot_left, rot_right = False, False, False, False
deviation_angle = 0.0
previous_mouse_position = root.winfo_pointerx()-root.winfo_rootx(), root.winfo_pointery()-root.winfo_rooty()


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


pyramid = Object(pyramid_model)
pyramid.toWorld(transform_1)

corner = Object(corner_model)
corner.toWorld(transform_corner_start)

corlist = []
for i in range(10):
    corlist += [Object(corner_model)]
    corlist[i].toWorld(Matrix(4, 4, [
    [2, 0, 0, 0],
    [0, 0, -2, 0],
    [0, -2, 0, 0],
    [20, 25, -70+100*i, 1]
]))

player = Player()
Labirinth = World(player, corner, *corlist)
Labirinth.canv_draw = lambda prim: \
    canv.create_polygon(*toCanv(prim), outline=prim.outline, width=prim.width, fill=prim.color)
Labirinth.projection_matrix = proj_matrix
Labirinth.set_screen_resolution(SCREEN_WIDTH, SCREEN_HEIGHT)

Labirinth.BSP_create()
Labirinth.update()
Labirinth.draw()


fps = 0
fps_time_start = 0
counter = 0


def loop():
    global a, w, s, d, q, e, rot_up, rot_down, rot_left, rot_right, deviation_angle, previous_mouse_position
    global fps, fps_time_start, counter
    start_time = time()

    allowed_directions = Labirinth.get_allowed_directions()     # get some restrictions to moving

    motion_x, motion_y = 0, 0
    if root == root.focus_get():
        x, y = root.winfo_pointerx()-root.winfo_rootx(), root.winfo_pointery()-root.winfo_rooty()
        #print([x, y], previous_mouse_position)
        motion_x, motion_y = x-previous_mouse_position[0], y-previous_mouse_position[1]
        previous_mouse_position = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        canv.event_generate('<Motion>', warp=True, x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    if w:
        if len(allowed_directions) == 0:
            player.move_along_z(player.speed, deviation_angle)  # if there are no restrictions
        else:
            move = True
            move_x = (player.matrix[1][0]*sin(deviation_angle) - player.matrix[2][0]*cos(deviation_angle))*player.speed     # coords of mooving
            move_y = (player.matrix[1][1]*sin(deviation_angle) - player.matrix[2][1]*cos(deviation_angle))*player.speed
            move_z = (player.matrix[1][2]*sin(deviation_angle) - player.matrix[2][2]*cos(deviation_angle))*player.speed

            for direct in allowed_directions:
                if direct[0]*move_x + direct[1]*move_y + direct[2]*move_z < 0:      # give a permission to move if True by checking a direction of moving
                    move = False
            if move:
                player.move_along_z(player.speed, deviation_angle)



    if a:
        if len(allowed_directions) == 0:
            player.move_along_x(-player.speed)
        else:
            move = True
            move_x = player.matrix[0][0]*(-player.speed)
            move_y = player.matrix[0][1]*(-player.speed)
            move_z = player.matrix[0][2]*(-player.speed)
            

            for direct in allowed_directions:
                if direct[0]*move_x + direct[1]*move_y + direct[2]*move_z < 0:
                    move = False
            if move:
                player.move_along_x(-player.speed)


    if s:
        if len(allowed_directions) == 0:
            player.move_along_z(-player.speed, deviation_angle)
        else:
            move = True
            move_x = (player.matrix[1][0]*sin(deviation_angle) - player.matrix[2][0]*cos(deviation_angle))*(-player.speed)
            move_y = (player.matrix[1][1]*sin(deviation_angle) - player.matrix[2][1]*cos(deviation_angle))*(-player.speed)
            move_z = (player.matrix[1][2]*sin(deviation_angle) - player.matrix[2][2]*cos(deviation_angle))*(-player.speed)

            for direct in allowed_directions:
                if direct[0]*move_x + direct[1]*move_y + direct[2]*move_z < 0:
                    move = False
            if move:
                player.move_along_z(-player.speed, deviation_angle)

    if d:
        if len(allowed_directions) == 0:
            player.move_along_x(player.speed)
        else:
            move = True
            move_x = player.matrix[0][0]*(player.speed)
            move_y = player.matrix[0][1]*(player.speed)
            move_z = player.matrix[0][2]*(player.speed)
            

            for direct in allowed_directions:
                if direct[0]*move_x + direct[1]*move_y + direct[2]*move_z < 0:
                    move = False
            if move:
                player.move_along_x(player.speed)

    if q:
        if len(allowed_directions) == 0:
            player.move_along_y(player.speed)
        else:
            move = True
            move_x = player.matrix[1][0]*(player.speed)
            move_y = player.matrix[1][1]*(player.speed)
            move_z = player.matrix[1][2]*(player.speed)
            

            for direct in allowed_directions:
                if direct[0]*move_x + direct[1]*move_y + direct[2]*move_z < 0:
                    move = False
            if move:
                player.move_along_y(player.speed)


    if e:
        if len(allowed_directions) == 0:
            player.move_along_y(-player.speed)
        else:
            move = True
            move_x = player.matrix[1][0]*(-player.speed)
            move_y = player.matrix[1][1]*(-player.speed)
            move_z = player.matrix[1][2]*(-player.speed)
            

            for direct in allowed_directions:
                if direct[0]*move_x + direct[1]*move_y + direct[2]*move_z < 0:
                    move = False
            if move:
                player.move_along_y(-player.speed)

    if rot_up and deviation_angle <= 1.5:
        deviation_angle += 0.04
        player.move(transform_rot_up)

    if rot_left:
        player.move(tr_rot_left(deviation_angle))

    if rot_down and deviation_angle >= -1.5:
        deviation_angle -= 0.04
        player.move(transform_rot_down)

    if rot_right:
        player.move(tr_rot_right(deviation_angle))

    if motion_x != 0:
        player.move(transform_rot_x(motion_x/400, deviation_angle))

    if motion_y > 0 and deviation_angle >= -1.5:
        mot_y = motion_y
        deviation_angle -= mot_y/400
        player.move(transform_rot_y(mot_y/400))

    if motion_y < 0 and deviation_angle <= 1.5:
        mot_y = motion_y
        deviation_angle += -mot_y/400
        player.move(transform_rot_y(mot_y/400))

    canv.delete(ALL)

    Labirinth.update()
    Labirinth.draw()

    canv.create_text(300, 300, text='fps: ' + str(fps))
    canv.create_text(300, 500, text='player_crds: ' + str(player.matrix[3]))

    canv.update()

    counter += 1
    if counter == 10:
        fps = 10/(time()-fps_time_start)
        fps_time_start = time()
        counter = 1

    dt = int((time()-start_time)*1000)
    canv.create_text(300, 400, text='dt: ' + str(dt))

    if dt >= 34:
        root.after(0, loop)
    else:
        root.after(34-dt, loop)



loop()

mainloop()
