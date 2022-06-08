'''
 * Reto #6
 * INVIRTIENDO CADENAS
 * Fecha publicación enunciado: 07/02/22
 * Fecha publicación resolución: 14/02/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def reverse_string(string):
    reversed = ''

    for x in range(len(string)-1,-1,-1):
        reversed = reversed + string[x]

    return reversed

print(reverse_string(input('Introduce la cadena a invertir: ')))
