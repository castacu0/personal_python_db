import os
import random

def random_word_func(filepath=r'C:\Users\Cesar Castanon\courses\python_course\intermediate_python_pl\words.txt'):

    with open(filepath, 'r', encoding='utf-8') as f:
        list_words = [word.strip().upper() for word in f]
        idx = random.randint(0, len(list_words)-1)
    return list_words[idx]


def game(random_word, letter_indexes, hidden_word_u):
    if letter_indexes in random_word:
        for i in range(len(random_word)):
            if letter_indexes == random_word[i]:
                hidden_word_u[i] = letter_indexes

    return ' '.join(hidden_word_u)


def run():
    lives = 5
    letter_indexes = ''
    random_word = random_word_func()
    hidden_word_u = ['_' for i in range(len(random_word))]

    while lives > 0:
        os.system('cls')
        print(f'Vidas restantes: {"❤" * (lives)}')
        print('¡Adivina la palabra!')
        print(game(random_word, letter_indexes, hidden_word_u))
        try:
            if len(letter_indexes) > 1:
                raise ValueError('Solo puedes ingresar una letra')
            else:
                if game(random_word, letter_indexes, hidden_word_u).count('_') > 0:
                    if letter_indexes in game(random_word, letter_indexes, hidden_word_u):
                        letter_indexes = input('Escoge una letra: ').upper()
                    else:
                        lives -= 1
                        if lives > 0:
                            os.system('cls')
                            print(f'Vidas restantes: {"❤" * (lives)}')
                            print('¡Adivina la palabra!')
                            print(game(random_word, letter_indexes, hidden_word_u))
                            letter_indexes = input('Escoge una letra: ').upper()
                        else:
                            os.system('cls')
                            print('¡Te quedaste sin vidas!\nJuego terminado...\n')
                            print('La palabra era: ' + random_word)
                else:
                    print('¡Ganaste! √')
                    break

        except ValueError as ve:
            return print(ve)
    

if __name__ == '__main__':
    run()