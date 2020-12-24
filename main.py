from tkinter import *

window = Tk()

def clear():
    global fon,btn,bttn,description,uslovie,uslovie1
    fon.destroy()
    btn.destroy()
    bttn.destroy()
    description.destroy()
    uslovie.destroy()
    uslovie1.destroy()

def vtoroepole():
    global description
    description = Label(window, text="123", font=("Calibri bold", 30,), background="#0210A1",fg="white")
    description.place(x='100', y="75")

def begin():
    global fon, btn, description, uslovie, bttn, uslovie1
    window.geometry('600x600')
    fon = Frame(window, bg='#18FFFD')
    fon.place(x=0, y=0, relwidth=1, relheight=1)
    btn = Button(window, bg="#42AAFF", text="ВПЕРЕД!", command=clear,activebackground='#18FFA2')
    btn.place(x=15, y=485, width=100, height=100)
    bttn = Button(window, bg="#42AAFF", text="Инструкция", command=clear, activebackground='#18FFA2',font=("Calibri bold", 14,))
    bttn.place(x=485, y=485, width=100, height=100)
    window.title("Добро пожаловать в ТеТрИс")
    uslovie = Label(window, text="Как же все таки играть в ТеТрИс!?\nТвоя задача опускать в ряд фигуры,\nТак чтобы весь ряд был закрыт\nКогда весь ряд будет закрыт\nУ тебя исчезнет этот ряд\nИ за это тебе дадут очки!\nИгра закончится если ряды не будут исчезать,\nИ все поле будет занято:((",font=("Calibri", 20,), background="#18FFFD",justify="left")
    uslovie.place(x='30', y="170")
    description = Label(window, text="Начни игру Т Е Т Р И С!", font=("Calibri bold", 30,), background="#0210A1",fg="white" )
    description.place(x='100', y="75")
    fon = Frame(window,bg='#18FFA2')

begin()

window.mainloop()
