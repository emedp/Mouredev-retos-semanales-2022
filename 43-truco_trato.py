'''
 * Reto #43
 * TRUCO O TRATO
 * Fecha publicación enunciado: 24/10/22
 * Fecha publicación resolución: 02/11/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y
 * un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
'''

import random

def trick_or_treat (action: str, people: list):
    halloween_result = ''

    if action == 'truco':
        print(trick(people))

    if action == 'trato':
        print(treat(people))


def trick (people: list):
    tricks = ['🎃', '👻', '💀', '🕷', '🕸', '🦇']
    trick_result = ''
    number_tricks = 0
    total_height = 0

    for person in people:

        # Un susto por cada 2 letras del nombre por persona
        if len(person['name']) % 2 == 0:
            number_tricks += int(len(person['name']) / 2)
        else:
            number_tricks += int((len(person['name']) - 1) / 2)

        # Dos sustos por cada edad que sea un número par
        if person['age'] % 2 == 0:
            number_tricks += 2
    
        # Tres sustos por cada 100 cm de altura entre todas las personas
        total_height += person['height']

    for cms in range(100, total_height, 100):
            number_tricks += 3

    for trick in range(number_tricks):
        random_trick = random.randint(0, len(tricks) - 1)
        trick_result += tricks[random_trick]

    return trick_result


def treat(people: list):
    treats = ['🍰', '🍬', '🍡', '🍭', '🍪', '🍫', '🧁', '🍩']
    treat_result = ''
    number_treats = 0

    for person in people:

        # Un dulce por cada letra de nombre
        number_treats += len(person['name'])
    
        # Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
        for years in range(3, person['age'], 3):
            number_treats += 1

        # Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
        for cms in range(50, person['height'], 50):
            number_treats += 2

    for treat in range(number_treats):
        random_treat = random.randint(0, len(treats) - 1)
        treat_result += treats[random_treat]

    return treat_result

array_people = [
    {
        'name': 'Ana',
        'age': 2,
        'height': 49,
    }
]
trick_or_treat(input('¿Truco o trato?: '), array_people)
