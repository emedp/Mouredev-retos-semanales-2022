'''
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
'''

# Una expresión equilibrada es aquella que el primer simbolo que se abre, es el último que se cierra
def check_expression (expression:str):

    # VARIABLES
    open_close = {
        '{' : '}',
        '(' : ')',
        '[' : ']',
    }
    result = False
    opened = []
    closed = []

    # MAIN CODE
    # add opened and closed symbols in arrays
    for character in expression:
        if character in open_close.keys():
            opened.append(character)
        elif character in open_close.values():
            closed.insert(0,character)

    # compare arrays
    if len(opened) == len(closed):
        result = True
        for index in range(len(opened)):
            if open_close [opened [index]] != closed [index]:
                result = False

    # PRINT CONSOLE
    print (expression)
    print (opened)
    print (closed)
    print (result, end="\n\n")

    # RETURN
    return result


check_expression("{ [ a * ( c + d ) ] - 5 }")
check_expression("{ a * ( c + d ) ] - 5 }")
