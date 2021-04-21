from tkinter import *
window = Tk()
c = Canvas(window, width=200, height=200, bg='#18FFFD')
c.pack()

def create_ugolok(x,y,side):
    figure=[
     c.create_rectangle(x, y, x-side, y+side,
                       fill = 'yellow',
                       outline = 'green',
                       width = 3,
                       activedash = (5, 4)),
    c.create_rectangle(x, y+side, x, y-side,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4)),
    c.create_rectangle(x, y+2*side, x-side, y+side,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4)),
    c.create_rectangle(x+side, y, x+side, y-side,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4))
    ]
    return figure



