'''
 * Reto #44
 * BUMERANES
 * Fecha publicación enunciado: 02/10/22
 * Fecha publicación resolución: 07/11/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que retorne el número total de bumeranes de un array de números
 * enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números seguidos, en el que el
 *   primero y el último son iguales, y el segundo es diferente. Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).
'''

def count_number_boomerangs (array: list):
    boomerangs = []
    for x in range(len(array) - 2):
        if array[x] == array[x+2]:
            boomerangs.append([array[x], array[x+1], array[x+2]])
    print(boomerangs)

count_number_boomerangs([2, 1, 2, 3, 3, 4, 2, 4])
