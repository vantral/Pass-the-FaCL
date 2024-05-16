from random import randint
from tkinter import *


def action1():
    choice = 1
    window.destroy()
    print('Ваш выбор ', choice)
    prize = randint(1, 3)
    if choice == prize:
        print('Ура, автомат!')
    else:
        print('О нет!')


def action2():
    choice = 2
    window.destroy()
    print('Ваш выбор ', choice)
    prize = randint(1, 3)
    if choice == prize:
        print('Ура, автомат!')
    else:
        print('О нет!')


def action3():
    choice = 3
    window.destroy()
    print('Ваш выбор ', choice)
    prize = randint(1, 3)
    if choice == prize:
        print('Ура, автомат!')
    else:
        print('О нет!')


WIDTH = 800
HEIGHT = 500
window = Tk()
window.title('Выбери Лифт')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='beige')
c.pack()
el1 = c.create_polygon(50, 50, 50, 450, 250, 450, 250, 50, fill='grey', outline='black')
el2 = c.create_polygon(300, 50, 300, 450, 500, 450, 500, 50, fill='grey', outline='black')
el3 = c.create_polygon(550, 50, 550, 450, 750, 450, 750, 50, fill='grey', outline='black')
button1 = Button(window, text="Кнопка 1", command=action1)
button1.pack()
button2 = Button(window, text="Кнопка 2", command=action2)
button2.pack()
button3 = Button(window, text="Кнопка 3", command=action3)
button3.pack()
window.mainloop()
