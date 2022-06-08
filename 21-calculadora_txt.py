'''
 * Reto #21
 * CALCULADORA .TXT
 * Fecha publicación enunciado: 23/05/22
 * Fecha publicación resolución: 01/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
'''

def calculatorTxt ():
    file = open("21-entradas_calculadora.txt","r")

    num = float(file.readline())
    print(num)

    for line in file:
        symbol = line.rstrip()
        nextNum = float(file.readline())

        print(symbol)
        print(str(nextNum))

        if symbol == '+':
            num += nextNum
        elif symbol == '-':
            num -= nextNum
        elif symbol == '*':
            num *= nextNum
        elif symbol == '/':
            num /= nextNum
        
        print('resultado paso: ' + str(num))
    
    file.close()


calculatorTxt()
