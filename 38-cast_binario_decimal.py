'''
 * Reto #38
 * BINARIO A DECIMAL
 * Fecha publicación enunciado: 19/09/22
 * Fecha publicación resolución: 27/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
 * funciones propias del lenguaje que lo hagan directamente.
'''

def cast_binary_decimal (binary_number: str):
    decimal_number = 0

    for position in range(0, len(binary_number)):

        if (binary_number[position] == '1'):
            decimal_number += 2 ** (len(binary_number) - position - 1)

    return print(binary_number + ' en decimal es: ' + str(decimal_number) )


cast_binary_decimal(input('Introduce el número binario que convertir a decimal: '))
