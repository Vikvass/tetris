from tkinter import *
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

create_ugolok(400,300,100)
c.pack()
window.mainloop()


