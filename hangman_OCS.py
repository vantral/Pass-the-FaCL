"""Hangman
Standard game of Hangman. A word is chosen at random from a list and the
user must guess the word letter by letter before running out of attempts."""

import random
import time

print("\nДобро пожаловать в Виселицу!\n")
name = input("Введи свое имя: ")
print("Привет, " + name + "! Желаем удачи!")
time.sleep(1)


def main():
    welcome = ['Ты должен отгадывать слова по буквам, пока не закончатся попытки и тебя не повесят.',
               'Поехали!'
               ]

    for line in welcome:
        print(line, sep='\n')

    # setting up the play_again loop
    
    points = 0
    count = 0

    play_again = True

    while play_again:
        # set up the game loop

        words = ["аорист","плюсквамперфект","палатализация","мена","торт","гиперкоррекция","аблаут","дифтонг","реконструкция","чередование"
                   ,"редукция", "имперфект", "склонение", "полногласие", "спряжение", "отвердение", "сингармонизм", 
                   "евангелие", "основа", "глаголица", "неполногласие", "ять", "падение", "титло", "презенс"]

        chosen_word = random.choice(words).lower()
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

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
            except: # check valid input
                print("Неверный ввод. Попробуй ещё раз.")
                continue
            else:
                if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
                    print("Это не буква. Попробуй ещё раз.")
                    continue
                elif len(player_guess) > 1: # check the input is only one letter
                    print("Это не 1 буква. Попробуй ещё раз.")
                    continue
                elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                    print("Эта буква уже была. Попробуй ещё раз.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: # no blanks remaining
            print(("\nПоздравляем! {} - загаданное слово").format(chosen_word))
            points += 2
            print("ٔТвой счет: ", points)
        else: # loop must have ended because attempts reached 0
            print(("\nОчень жаль! Загаданное слово - {}.").format(chosen_word))
            count += 1
            print("ٔТвой счет: ", points)
        if points >= 10:
            print("Поздравляем, ты набрал 10 очков!")
            exit()
        if count == 3:
            print ("Игра окончена!")
            exit()
        
        response = input("Играем дальше? д = да, н = нет \n")
        if response not in ("д", "Д"):
            exit()


if __name__ == "__main__":
    main()