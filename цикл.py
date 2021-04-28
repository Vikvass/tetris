from tkinter import *
import time
window = Tk()
c = Canvas(window, width=600, height=600, bg='#18FFFD')
c.pack()

def create_ugolok(x,y,side):
    figure=[
     c.create_rectangle(x, y, x - side, y + side,
                       fill='yellow',
                       outline='green',
                       width = 3,
                       activedash = (5, 4)),
    c.create_rectangle(x, y, x - side, y-side,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4)),
    c.create_rectangle(x, y - side, x-side, y- 2 *side,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4)),
    c.create_rectangle(x, y, x+side, y + side,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4))
    ]
    return figure


x = 100
y = 100
speed = 10
side = 50
while (x != 600) and (y != 600):
    create_ugolok(x, y, side)
    y = y + speed
    x = x + speed
    time.sleep(1)
    c.pack()
    window.mainloop()

