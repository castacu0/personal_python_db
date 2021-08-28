# -*- coding: utf-8 -*-
import os
import random
from images_for_hangman import IMAGES
from words_for_hangman import WORDS


def random_word_func():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word_u, tries):
    #os.system("cls")
    print(IMAGES[tries])
    print('')
    print(hidden_word_u)
    print(' ---------------------------------- ')


def run():
    random_word = random_word_func()
    # hidden_word_u = '-' * len(random_word)
    hidden_word_u = ['-'] * len(random_word)
    # print(hidden_word_u)
    tries = 0

    while True:
        display_board(hidden_word_u, tries)
        current_letter = str(input('Choose only one word: '))

        letter_indexes = []
        for idx in range(len(random_word)):
            if random_word[idx] == current_letter:
                letter_indexes.append(idx)
                print(letter_indexes, "//////***//")

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word_u, tries)
                print('')
                print('You lost! The correct word was {}'.format(random_word))
                break
        else:
            for idx in letter_indexes:
                print(f"idx --> {idx}")
                hidden_word_u[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word_u.index('-')
        except ValueError:
            print('')
            print('Congrats! You won. The correct word is: {}'.format(random_word))
            break


if __name__ == '__main__':
    print("LET'S PLAY SOME HANGMAN")
    run()
