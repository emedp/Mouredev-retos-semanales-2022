'''
 * Reto #8
 * DECIMAL A BINARIO
 * Fecha publicación enunciado: 18/02/22
 * Fecha publicación resolución: 02/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

def decimal_to_binary(decimal:int):

    # VARIABLES
    number = decimal
    binary = ""

    # MAIN CODE
    while number >= 1:
        module = number % 2
        number /= 2

        binary = str(int(module)) + binary

    # PRINT TO CONSOLE
    print ("decimal: " + str(decimal))
    print ("binary: " + binary)
    #print (binary)

    # RETURN

    return binary


decimal_to_binary(24)
decimal_to_binary(9)
decimal_to_binary(5)
