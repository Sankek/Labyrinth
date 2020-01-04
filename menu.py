import mp3play
from tkinter import*

filename_1 = 'sounds/bentley.mp3'
clip_1 = mp3play.load(filename_1)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

root = Tk()
fr = Frame(root)
root.geometry(str(SCREEN_WIDTH)+'x'+str(SCREEN_HEIGHT))
root.resizable(False, False)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

game_is_on, sound, contin, esc, mlg = True, False, False, False, False




def common_music_on(event):
    clip_1.play()

def common_music_off(event):
    clip_1.stop()

def Contining(event):
    esc = False
    game_is_on = True
    return esc, game_is_on



def Escaping(event):
    quit()
def MLG(event):
    pass
def Pause():


    Label_pause = Label(width=20, height=2, bg = 'grey', text = 'PAUSE', font = '30')
    Label_pause.place(x=SCREEN_WIDTH/5*2, y=SCREEN_HEIGHT/20)

    Button_music_on = Button(root, command=lambda: print('Mute On'), text = 'Sound ON')
    Button_music_on.place(x=SCREEN_WIDTH/10, y=SCREEN_HEIGHT/5)
    Button_music_on.bind("<Button-1>", common_music_on)

    Button_music_off = Button(root, command=lambda: print('Mute Off'), text = 'Sound OFF')
    Button_music_off.place(x=SCREEN_WIDTH/10, y=SCREEN_HEIGHT/4)
    Button_music_off.bind("<Button-1>", common_music_off)

    Contin = Button(root, command=lambda: print('Continue'), text = 'FLEX BUTTON.')
    Contin.place(x=SCREEN_WIDTH/1.25, y=SCREEN_HEIGHT/5)
    Contin.bind("<Button-1>", Contining)

    Escape = Button(root, command=lambda: print('Escape'), text = 'Quit')
    Escape.place(x=SCREEN_WIDTH/1.25, y=SCREEN_HEIGHT/4)
    Escape.bind("<Button-1>", Escaping)

    Mlg = Button(root, command=lambda: print('click'))
    Mlg.place(x=300, y=600)
    Mlg.bind("<Button-1>", MLG)





