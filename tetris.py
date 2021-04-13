from tkinter import *

window = Tk()

def clear():
    global fon, btnnow, btnins, description, uslovie1
    fon.destroy()
    btnnow.destroy()
    btnins.destroy()
    description.destroy()

def instruksia():
    global description, btnnachal,uslovie
    clear()
    description = Label(window, text="Инструкция", font=("Calibri bold", 30,), background="#0210A1",fg="white")
    description.place(x='100', y="75")
    btnnachal = Button(window, bg ="#42AAFF",text="Вернуться в начало", command=begin, activebackground='#18FFA2')
    btnnachal.place(x=15, y=485, width=100, height=100)  # кнопка, которая ведет в начало игры после инструкции
    uslovie = Label(
        window,
        text="Как же все таки играть в ТеТрИс!?\nТвоя задача опускать в ряд фигуры,"
             "\nТак чтобы весь ряд был закрыт\nКогда весь ряд будет закрыт"
             "\nУ тебя исчезнет этот ряд\nИ за это тебе дадут очки!"
             "\nИгра закончится если ряды не будут исчезать,"
             "\nИ все поле будет занято:((",font=("Calibri", 20,), background="#18FFFD",justify="left")
    uslovie.place(x='30', y="170")


def vtoroepole():
    global btnnachall,uslovie
    clear()
    btnnachall = Button(window, bg="#42AAFF", text="Вернуться в начало", command=begin, activebackground='#18FFA2')
    btnnachall.place(x=15, y=485, width=100, height=100)

def begin():
    global fon, btnnow, description, btnins
    window.geometry('600x600')
    fon = Frame(window, bg='#18FFFD')
    fon.place(x=0, y=0, relwidth=1, relheight=1)
    btnnow = Button(window, bg="#42AAFF", text="ВПЕРЕД!", command=vtoroepole, activebackground='#18FFA2') #кнопка, которая ведет в игру
    btnnow.place(x=15, y=485, width=100, height=100)
    btnins = Button(                          #кнопка, которая ведет в инструкцию
        window,
        bg="#42AAFF",
        text="Инструкция",
        command=instruksia,
        activebackground='#18FFA2',
        font=("Calibri bold", 14,)
    )
    btnins.place(x=485, y=485, width=100, height=100)
    window.title("Добро пожаловать в ТеТрИс")
    description = Label(
        window,
        text="Начни игру в ТеТрИс!",
        font=("Calibri bold", 30,),
        background="#0210A1",
        fg="white")
    description.place(x='100', y="75")
    fon = Frame(window, bg='#18FFA2')
    c = Canvas(window, width=200, height=200, bg='#18FFFD')
    c.pack()

    c.create_rectangle(60, 60, 40, 130,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4))
    c.create_rectangle(80, 110, 60, 130,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4))
    c.create_rectangle(80, 110, 40, 130,
                       fill='yellow',
                       outline='green',
                       width=3,
                       activedash=(5, 4))
    c.create_line(60, 110, 60, 130,
                  width=3)
    c.create_line(40, 87, 60, 87,
                  width=3)


begin()
window.mainloop()