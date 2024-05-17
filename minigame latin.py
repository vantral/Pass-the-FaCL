from tkinter import *
from random import randint
from math import sqrt
import time


def move(event):
    if event.keysym == 'Up':
        c.move(hand, 0, -10)
    elif event.keysym == 'Down':
        c.move(hand, 0, 10)
    elif event.keysym == 'Right':
        c.move(hand, 10, 0)
    elif event.keysym == 'Left':
        c.move(hand, -10, 10)


def create_book():
    x = WIDTH + 100
    y = randint(0, HEIGHT)
    book = c.create_text(x, y, text='Хэндаут')
    books.append(book)
    books_speed.append(randint(1, 15))


def fly():
    for i in range(len(books)):
        c.move(books[i], -books_speed[i], 0)


def find(i):
    position = c.coords(i)
    x = position[0]/ 2
    y = position[1] / 2
    return x, y


def kill(i):
    del books_speed[i]
    c.delete(books[i])
    del books[i]


def distance(h, b):
    x1, y1 = find(h)
    x2, y2 = find(b)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def win():
    now = 0
    for book in range(len(books) - 1, -1, -1):
        if distance(hand, books[book]) < 30:
            now += 1
            kill(book)
    return now


def score(points):
    c.itemconfig(s, text=str(points))


def remain_time(seconds):
    c.itemconfig(t, text=str(seconds))


window = Tk()
WIDTH = 800
HEIGHT = 500
window.title('Экзамен по Латыни')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='lightblue')
c.pack()
hand = c.create_polygon(5, 5, 5, 25, 30, 15, fill='black')
mid_x = WIDTH / 2
mid_y = HEIGHT / 2
c.move(hand, mid_x, mid_y)
c.bind_all('<Key>', move)
c.create_text(50, 30, text="ВРЕМЯ", fill='black')
c.create_text(150, 30, text="СЧЕТ", fill='black')
t = c.create_text(50, 50, fill='black')
s = c.create_text(150, 50, fill='black')
timelimit = 30
end = time.time() + timelimit
books = list()
books_speed = list()
scores = 0
while time.time() < end:
    if randint(1, 20) == 1:
        create_book()
    fly()
    scores += win()
    score(scores)
    remain_time(int(end - time.time()))
    window.update()
    time.sleep(0.01)
c.create_text(mid_x, mid_y, text='GAME OVER', fill='red')
c.create_text(mid_x, mid_y + 40, text='Score:' + str(scores), fill='red')
mainloop()
