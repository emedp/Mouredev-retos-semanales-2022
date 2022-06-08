'''
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
'''

from posixpath import split


def check_anagrama (string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if string1 == string2:
        return print('Las palabras [', string1,'] [',string2,'] son iguales, no son un anagrama')

    lista1 = list(string1)
    lista1.sort()

    lista2 = list(string2)
    lista2.sort()

    print(lista1)
    print(lista2)

    return print(lista1 == lista2)


palabra_1 =input('Introduce la primera palabra: ')
palabra_2 = input('Introduce la segunda palabra: ')
check_anagrama(palabra_1, palabra_2)
