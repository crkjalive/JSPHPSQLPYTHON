# -*- coding: utf-8 -*-

import random

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
    ======''','''
    +---+
    |   |
    O   |
        |
        |
        |
    ======''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
    ======''','''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ======''','''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    ======''','''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    ======''','''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ======'''
]


WORDS = [
    'fondercats',
    'motoratones',
    'simpsons',
    'garfield',
    'super campeones',
    'dragon ball',
    'caballeros del zodiaco',
    'monstruos',
    'maximals beast wars',
    'la pantera rosa',
    'power rangers',
    'transformers',
    'aventuras de zonic',
    'super mario bross',
    'masha and the bear'
    ]



# retorna una palabra
def random_word():
    idx = random.randint(0, len(WORDS) -1)
    return WORDS[idx]


# imprime interface
def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- * ---')


# funcion principal
def run():
    word = random_word()
    hidden_word = ['-'] *len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 6:
                display_board(hidden_word,tries)
                print('')
                print(f'Lo sentimo perdiste! la palabra correcta era {word}')
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []


        # evalua si ya no hay guiones
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print(f'felicidades! Ganaste. la palabra es {word}')
            break



# interpreta python desde aquí
if __name__ == '__main__':
    
    print('BIENVENIDOS A AHORCADOS')

    run()