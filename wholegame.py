from tkinter import *
import random
from math import sqrt
import time
import pygame


def latin(timelimit):
    window = Tk()
    global c, t, s, books, books_speed, hand, WIDTH, HEIGHT
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
    end = time.time() + timelimit
    books = list()
    books_speed = list()
    scores = 0
    while time.time() < end:
        if random.randint(1, 20) == 1:
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
    return int(scores / 3)


def move(event):
    if event.keysym == 'Up':
        c.move(hand, 0, -10)
    elif event.keysym == 'Down':
        c.move(hand, 0, 10)
    elif event.keysym == 'Right':
        c.move(hand, 10, 0)
    elif event.keysym == 'Left':
        c.move(hand, -10, 0)


def create_book():
    x = WIDTH + 100
    y = random.randint(0, HEIGHT)
    book = c.create_text(x, y, text='Хэндаут')
    books.append(book)
    books_speed.append(random.randint(1, 15))


def fly():
    for i in range(len(books)):
        c.move(books[i], -books_speed[i], 0)


def find(i):
    position = c.coords(i)
    x = position[0] / 2
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


def action1():
    global automat
    choice = 1
    print('Ваш выбор ', choice)
    prize = random.randint(1, 3)
    if choice == prize:
        automat = True
    window.destroy()


def action2():
    global automat
    choice = 2
    print('Ваш выбор ', choice)
    prize = random.randint(1, 3)
    if choice == prize:
        automat = True
    window.destroy()


def action3():
    global automat
    choice = 3
    print('Ваш выбор ', choice)
    prize = random.randint(1, 3)
    if choice == prize:
        automat = True
    window.destroy()


def yari():
    # Окно игры
    screen_width = 1000
    screen_height = 500
    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Экзамен по ЯРам")
    res = game()
    return res


def display_text(text, x, y, font_size=30, color='black'):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


questions = [
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': 'audio.lang/водский.MP3',
        'ответы': ['A) Английский', 'B) Водский', 'C) Коми-пермяцкий', 'D) Аварский'],
        'правильный_ответ': 'B) Водский'
    },
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': 'audio.lang/лакский.MP3',
        'ответы': ['A) Лакский', 'B) Мокшанский', 'C) Агульский', 'D) Русский'],
        'правильный_ответ': 'A) Лакский'
    },
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': 'audio.lang/нанайский.MP3',
        'ответы': ['A) Нанайский', 'B) Татарский', 'C) Испанский', 'D) Табасаранский'],
        'правильный_ответ': 'A) Нанайский'
    },
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': 'audio.lang/чеченский.MP3',
        'ответы': ['A) Калмыцкий', 'B) Французский', 'C) Чеченский', 'D) Эвенкийский'],
        'правильный_ответ': 'C) Чеченский'
    },
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': 'audio.lang/эвенкийский.MP3',
        'ответы': ['A) Удмуртский', 'B) Эвенкийский', 'C) Абазинский', 'D) Немецкий'],
        'правильный_ответ': 'B) Эвенкийский'
    }
]


# Воспроизведение мелодии
def play_melody(melody_file):
    pygame.mixer.music.load(melody_file)
    pygame.mixer.music.play()


# Сама игра
def game():
    score = 0
    for question_data in questions:
        screen.fill('white')
        display_text(question_data['вопрос'], 50, 50)

        # Воспроизведение мелодии и вывод вариантов ответов
        play_melody(question_data['мелодия'])
        y_offset = 150
        for answer in question_data['ответы']:
            display_text(answer, 100, y_offset)
            y_offset += 50

        pygame.display.flip()

        # Ожидание ответа игрока
        answered = False
        while not answered:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player_answer = question_data['ответы'][0]
                        answered = True
                    elif event.key == pygame.K_b:
                        player_answer = question_data['ответы'][1]
                        answered = True
                    elif event.key == pygame.K_c:
                        player_answer = question_data['ответы'][2]
                        answered = True
                    elif event.key == pygame.K_d:
                        player_answer = question_data['ответы'][3]
                        answered = True
        pygame.mixer.music.stop()
        # Проверка ответа игрока и увеличение счета при правильном ответе
        if player_answer == question_data['правильный_ответ']:
            score += 1
    # Результат игры
    grade = score * 2
    screen.fill('white')
    display_text("Игра окончена!", 300, 50)
    display_text(f"Ваша оценка: {grade}", 300, 100)
    pygame.display.flip()
    time.sleep(3)
    return grade


def printing(words):
    for i in words:
        print(i)
        time.sleep(1)


def main():
    welcome = ['Ты должен отгадывать слова по буквам, пока не закончатся попытки и тебя не повесят.',
               'Поехали!'
               ]

    for line in welcome:
        print(line, sep='\n')

    points = 0
    count = 0

    play_again = True

    while play_again:

        words = ["аорист", "плюсквамперфект", "палатализация", "мена", "торт", "гиперкоррекция", "аблаут", "дифтонг",
                 "реконструкция", "чередование"
            , "редукция", "имперфект", "склонение", "полногласие", "спряжение", "отвердение", "сингармонизм",
                 "евангелие", "основа", "глаголица", "неполногласие", "ять", "падение", "титло", "презенс"]

        chosen_word = random.choice(words).lower()
        player_guess = None
        guessed_letters = []
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-")
        joined_word = None

        HANGMAN = (
            """
            -----
            |   |
            |
            |
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            |
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            |  -+-
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | | 
            |  | | 
            |
            --------
            """)

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1

        while (attempts != 0 and "-" in word_guessed):
            print(("\nОсталось {} попыток").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nВведи любую букву А-Я" + "\n> ")).lower()
            except:  # check valid input
                print("Неверный ввод. Попробуй ещё раз.")
                continue
            else:
                if not player_guess.isalpha():  # check the input is a letter. Also checks an input has been made.
                    print("Это не буква. Попробуй ещё раз.")
                    continue
                elif len(player_guess) > 1:  # check the input is only one letter
                    print("Это не 1 буква. Попробуй ещё раз.")
                    continue
                elif player_guess in guessed_letters:  # check it letter hasn't been guessed already
                    print("Эта буква уже была. Попробуй ещё раз.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[
                        letter] = player_guess  # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed:  # no blanks remaining
            print(("\nПоздравляем! {} - загаданное слово").format(chosen_word))
            points += 2
            print("ٔТвой счет: ", points)
        else:  # loop must have ended because attempts reached 0
            print(("\nОчень жаль! Загаданное слово - {}.").format(chosen_word))
            count += 1
            print("ٔТвой счет: ", points)
        if points >= 10:
            print("Поздравляем, ты набрал 10 очков!")
            return points
        if count == 3:
            print("Игра окончена!")
            return points


f = open('start.txt', 'r')
energy = 50
res = 0
for i in f.readlines():
    print(i)
    time.sleep(1)
day1 = ['День1', 'Дорогой друг, поздравляем с началом сессии!',
        'Сегодня тебе предстоит написать экзамен по латинскому языку.', 'Желаем удачи!',
        'За завтраком ты увлекся повторением материала, поэтому вышел из дома позже запланированного.',
        'Что ж, пока еще не опаздываешь, но поторопиться стоит!']
printing(day1)
print('!Внимание, выбор осуществляется с помощью клавиш!')
time.sleep(1)
print('Если вы хотите пойти по лестнице, напечатайте 1')
print('Для того, чтобы поехать на лифте, напечатайте 2')
try:
    choice = int(input())
except Exception:
    choice = int(input())
if choice == 1:
    printing(['Да ты тот еще спортсмен!', 'Сильные ноги точно не дадут опоздать на экзамен. ',
              'Но подняться на 5 этаж - испытание не из легких'])
    energy -= 10
    timer = 30
    print('Внимание! Значение энергии изменилось. Текущее значение:', energy)
else:
    printing(['Да, подниматься по лестнице совсем неохота.', 'Но как же долго ждать лифт!'])
    print('Вы потеряли время на прохождение игры')
    timer = 15
printing(['Фух, вроде бы успел на экзамен!', 'Теперь главное - успокоиться и собраться с мыслями.', 'Вдох-выдох!'])
printing(['Как же здорово, что на экзамене по латыни можно пользоваться дополнительными материалами!', 'Ой..',
          'Похоже, что во время утренней спешки ты забыл все свои хэндауты.',
          'Что ж, неприятно, конечно, но поправимо, ведь Файер всегда одолжит парочку.'])
printing(['Твоя задача поймать все хэндауты и словари, передвигая курсор стрелками на клавиатуре',
          'Чем больше поймаешь, тем выше оценку получишь'])
reslatin = latin(timer)
res += reslatin
printing(['Экзамен подошел к концу,', 'сейчас посмотрим,', 'как ты с ним справился'])
printing(['Сердце бьется чаще, как ты заходишь в Гугл-таблицы,', 'чтоб взглянуть на табель оценок.',
          'Ищешь свою фамилию глазами...'])
print('Твой результат:', reslatin)
if reslatin > 6:
    printing(['Хороший результат!', ' Первый экзамен позади, но расслабляться пока рано.', 'Или все-таки..'])
    printing(['готовиться к завтрашнему экзамену - 1', 'лечь спать - 2'])
    a = int(input())
    if a == 1:
        energy -= 20
        nakop = 4
        print('Внимание! Значение энергии изменилось. Текущее значение:', energy)
        print('Внимание! Вы получили накоп = 4!')
    else:
        print('Ну ладно, утро вечера мудреннее')
        energy += 10
        nakop = 0
        print('Внимание! Значение энергии изменилось. Текущее значение:', energy)
else:
    printing(['Эх, ты плохо справился', 'Видимо нужно было лучше готовиться'])
    printing(['готовиться к завтрашнему экзамену - 1', 'лечь спать - 2'])
    a = int(input())
    if a == 1:
        printing(['Да, стоит учесть ошибки прошлого и ответственней подойти  к подготовке.',
                  'Следующий экзамен уже завтра, но впереди целая ночь, что-то явно успеешь повторить.'])
        energy -= 20
        nakop = 4
        print('Внимание! Значение энергии изменилось. Текущее значение:', energy)
        print('Внимание! Вы получили накоп =', nakop, '!')
    else:
        printing(['Да, это был непростой день', 'лучше отдохнуть перед завтрашним экзаменом.'])
        energy += 10
        nakop = 0
        print('Внимание! Значение энергии изменилось. Текущее значение:', energy)
print('День 2')
time.sleep(1)
printing(['Ты выдержал первый день сессии, поздравляем! ', 'Впереди ещё 3 экзамена, справишься? ',
          'Отлично, тогда настраивайся на экзамен по старославянскому языку', '(прощай, древность!)'])
if a == 1:
    printing(['О нет, ты готовился к экзамену всю ночь и не услышал ни один из 5 будильников!',
              'Теперь ты опаздываешь на экзамен', 'а ведь на подготовку к ответу даётся всего 10 минут.'])
    printing(['До начала твоего времени остаётся всего несколько минут', 'надо торопиться!'])
    printing(['По пути в кабинет ты вдруг встречаешь Костю Филатова.', 'Завтра же экзамен по ЯРам!',
              'Может быть, попытаться выпытать у него задания?'])
    printing(['Остановиться и поговорить с Костей - 1', 'Поспешить на экзамен - 2'])
    b = int(input())
    if b == 1:
        printing(['Не зря ты такой общительный.', 'Тебе удалось узнать семью языка, по которому составлены задания.',
                  'Мелочь, а приятно (и полезно!)'])
        nakop_yari = 2
        print('+2 балла к оценке за экзамен по ЯРам')
        printing(['Ты заболтался с Костей и всё-таки опоздал на экзамен', 'на подготовку совсем не осталось времени.'])
        print('Ваш накоп уменьшился на 1 балл')
        nakop -= 1
    elif b == 2:
        nakop_yari = 0
        print('Молодец, ты подошёл точно к своему времени!')
elif a == 2:
    printing(['Ты хорошо выспался и перед экаменом решил поготовиться в коворкинге.',
              'Успеешь ли ты повторить все палатализации и типы склонения?', 'Посмотрим'])
    nakop += 2
    print('Вы получили накоп - 2')
    nakop_yari = 0
printing(['Для сдачи экзамена по старославянскому языку тебе предстоит пройти игру "Виселица"',
          'Заинтриговали? Вот правила игры: ты должен будешь отгадать загаданное нами слово на старославянскую тематику, называя буквы.',
          'Всего ты можешь назвать 5 неверных букв - когда попытки закончатся, человечек повесится.',
          'За каждое отгаданное слово ты получаешь 2 балла.',
          'Количество раундов не ограничено, но, если человечек повесится 3 раза, игра закончится.',
          'Цель: набрать 10 баллов.',
          'Игра продолжается до тех пор, пока игрок не наберет 10 баллов ИЛИ до 3 проигрышей.'])
printing(['Всё понятно? Тогда вперёд!'])
print("\nДобро пожаловать на Экзамен!\n")
name = input("Введи свое имя: ")
print("Привет, " + name + "! Желаем удачи!")
time.sleep(1)
if __name__ == "__main__":
    resstar = main()
resstar += nakop
if resstar > 10:
    resstar = 10
elif resstar < 0:
    resstar = 0
print('Экзамен окончен. Твоя оценка -', resstar)
res += resstar
print('Общий счет = ', res)
if resstar > 7:
    printing(
        ['Ты очень доволен своей оценкой', 'Не хочешь отметить экватор сессии в баре с друзьями?', 'Поехать в бар - 1',
         'Поехать домой готовиться - 2'])
    a = int(input())
    if a == 1:
        printing(['Отлично повеселились!', 'Теперь придётся идти на завтрашний экзамен уставшим и невыспавшимся.'])
        energy -= 20
        print('Внимание! Значение энергии изменилось. Текущее значение:', energy)
        if energy == 0:
            printing(['О нет!', 'Ты потратил все свои силы, а ведь сессия еще даже не закончилась.',
                      'Придется отчисляться и начинать с начала...'])
            flag = False
        else:
            printing(['Это определённо правильный выбор.', 'В бар сходить и после сессии можно, правда?',
                      'Зато к ЯРам нормально подготовишься.'])
            flag = True
    else:
        flag = True
else:
    printing(['Ура, прошла уже половина сессии, осталось совсем немного.', 'А теперь отдыхай, до завтра!'])
    flag = True
if flag:
    print('День 3')
    printing(['Половина пути позади, но впереди еще столько же!',
              'Сегодня тебя ждёт третий день сессии, а, значит, настало время экзамена по Языкам России.',
              'Желаем удачи!'])
    printing(['Впервые за сессию у тебя получилось проснуться заранее и приехать на экзамен вовремя.', 'Это успех!',
              'Перед экзаменом ты встречаешь своих любимых добрых преподавателей по ЯРам.',
              'Они предлагают тебе конфеты.', 'Что же это: жест доброй воли или очередной подвох?', 'взять конфету - 1',
              'отказаться от конфеты - 2'])
    a = int(input())
    if a == 1:
        energy += 20
        if energy > 100:
            energy = 100
        print('Внимание! Значение энергии изменилось. Текущее значение:', energy)
        printing([' Какой ты сладкоежка!',
                  'Благодаря вкусной конфетке ты получаешь заряд позитива и энергии на весь экзамен.'])
    printing(['Пришло время сдать экзамен по ЯРам.', 'Для этого тебе предстоит пройти игру "Угадай язык".',
              'Правила игры: необходимо прослушать отрывки речи на разных языках и выбрать правильный вариант ответа.',
              'Всего  будет предложено 10 вопросов, в каждом из которых по 4 варианта ответа.',
              'За каждый правильный ответ ты получаешь 1 балл. Максимум: 10 баллов.'])
    pygame.init()
    resyari = yari()
    pygame.quit()
    resyari += nakop_yari
    if resyari > 10:
        resyari = 10
    printing(['Поздравляем!', 'Экзамен по Языкам России позади.',
              'Надеемся, погружение в лингвистику прошло для тебя безболезненно.'])
    print('Твой результат:', resyari)
    res += resyari
    print('Общий счет = ', res)
    printing([
        'Ты так устал на экзамене, что на свой страх и риск ты решил спуститься к выходу на одном из лифтов корпуса А.',
        ' Лишь бы не застрял в очередной раз.', ' Одновременно к тебе приехали все 3 лифта.',
        ' Выбери, на каком сейчас поедешь.'])

    global automat
    automat = False
    WIDTH = 800
    HEIGHT = 500
    global window
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
    if automat:
        printing(['Удача сегодня явно на твоей стороне, и ты без происшествий доехал до первого этажа.',
                  'Внезапно тебе приходит сообщение от Анны Витальевны Михайлович',
                  'о возможности взять автомат за предстоящий экзамен по дискретной математике.',
                  'Сегодня тебе сильно везёт!'])
        printing(['К сожалению, автомат гарантирует только 8 за предстоящий экзамен.',
                  'Подумай, достаточно ли тебе этого, или хочешь попробовать получить оценку выше и сходить на экзамен.',
                  'пойти на экзамен - 1', 'не идти на экзамен - 2'])
        a = int(input())
        if a == 1:
            res_discra = 0
        else:
            res_discra = 8
            printing(['Опа, автомат!', 'Поздравляем, трудяга, для тебя экзамены закончились.',
                      'Пока твои одногруппники мучаются на экзамене, предлагаем тебе расслабиться и посмотреть познавательное видео:',
                      'https://youtu.be/nviEkurZlao?si=K9-ZJi--WZAH_5GW'])
    else:
        res_discra = 0
        printing(['Что это за звук?!', 'О нет...', 'Ты снова застрял в лифте.',
                  'Придётся немного подождать, чтобы наконец-то выбраться из Басмача.'])
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
    if res_discra == 0:
        print('День 4')
        printing(['Ты на финишной прямой!', 'Остался последний рывок - экзамен по дискретной математике.',
                  ' Да, это будет тяжело, зато какой камень с плеч!'])
        printing([' Не спеши отчаиваться, обещаем, экзамен будет совсем не страшным.',
                  'В качестве экзамена по дискретной математике (последнего экзамена этой сессии!) мы предлагаем тебе пройти игру "Где логика?"',
                  ' Правила игры: тебе необходимо как можно более логично отвечать на вопросы.',
                  ' Всего будет задано 5 вопросов, за каждый вопрос ты получаешь 2 балла.', 'Максимум: 10 баллов.'])
        resultat = 0
        print('А сейчас время для квиза!')
        time.sleep(1)
        print('Что можно видеть с закрытыми глазами? (Введите ответ в единственном числе)')
        answer = input('')
        if answer in ['сон', 'Сон']:
            resultat += 2
        print('Сколько месяцев в году имеют 28 дней? (В ответе введите число)')
        answer = input('')
        if answer == '12':
            resultat += 2
        print('Какой болезнью на земле никто не болел?')
        answer = input('')
        if answer in ['морская', 'морской']:
            resultat += 2
        print('Маленький, серенький на слона похож. Кто это?')
        answer = input('')
        if answer in ['слонёнок', 'слоненок']:
            resultat += 2
        print("Какие часы показывают верное время только два раза в сутки?")
        answer = input('')
        if answer in ['сломанные', 'поломанные', 'не работающие']:
            resultat += 2
        res_discra = resultat
        print('Можешь расслабиться, экзамен по дискретной математике окончен!')
    print('Твой результат:', res_discra)
    res += res_discra
    printing(["Вот и подошла к концу сессионная неделя ФиКЛа!",
              ' Надеемся, ты остался доволен полученными оценками и своими знаниями.'])
    print('Твой итог:', res)
    printing(['Спасибо, что провёл эти 4 дня с нами!', 'А мы ждём тебя снова, нам есть, чем тебя удивить!'])
    if res == 40:
        printing(['Вау, вот это ты молодец', 'За такой невероятный результат держи подарок',
                  'https://youtu.be/4rE5LgTOyds?si=S4O7p1OR-bSCaf4S'])
