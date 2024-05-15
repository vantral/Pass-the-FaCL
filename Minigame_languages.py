import pygame
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Окно игры
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Экзамен по ЯРам")

# Отображение текста
def display_text(text, x, y, font_size=30, color=BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Вопросы и ответы
questions = [
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': '/Users/alexshnaydy/Desktop/водский.MP3',
        'ответы': ['A) Английский', 'B) Водский', 'C) Коми-пермяцкий', 'D) Аварский'],
        'правильный_ответ': 'B) Водский'
    },
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': 'лакский.MP3',
        'ответы': ['A) Лакский', 'B) Мокшанский', 'C) Агульский', 'D) Русский'],
        'правильный_ответ': 'A) Лакский'
    },
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': '/Users/alexshnaydy/Desktop/нанайский.MP3',
        'ответы': ['A) Нанайский', 'B) Татарский', 'C) Испанский', 'D) Табасаранский'],
        'правильный_ответ': 'A) Нанайский'
    },
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': '/Users/alexshnaydy/Desktop/чеченский.MP3',
        'ответы': ['A) Калмыцкий', 'B) Французский', 'C) Чеченский', 'D) Эвенкийский'],
        'правильный_ответ': 'C) Чеченский'
    },
    {
        'вопрос': 'Какой язык? Для выбора ответа нажмите на английской раскладке A/B/C/D.',
        'мелодия': '/Users/alexshnaydy/Desktop/эвенкийский.MP3',
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
        screen.fill(WHITE)
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
            grade = score * 2

    # Результат игры
    screen.fill(WHITE)
    display_text("Игра окончена!", 300, 50)
    display_text(f"Ваша оценка: {grade}", 300, 100)
    pygame.display.flip()
    time.sleep(3)


# Запуск игры
game()

# Выход из программы Pygame
pygame.quit()
