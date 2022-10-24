'''
 * Reto #41
 * LA LEY DE OHM
 * Fecha publicación enunciado: 10/10/22
 * Fecha publicación resolución: 17/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
'''

def ohms_law(V:str, R:str, I:str):
    validV = False
    validR = False
    validI = False
    total_valid = 0

    if (V != '' and int(V) != 0):
        validV = True
        total_valid += 1

    if (R != '' and int(R) != 0):
        validR = True
        total_valid += 1

    if (I != '' and int(I) != 0):
        validI = True
        total_valid += 1

    if total_valid != 2:
        return print('Invalid values')

    # V = R * I

    if (not validV):
        V = int(R) * int(I)
        return print('La potencia es igual a: ', V)
    
    if (not validR):
        R = int(V) / int(I)
        return print('La resistencia es igual a: ', R)

    if (not validI):
        I = int(V) / int(R)
        return print('La intensidad es igual a: ', I)
    
ohms_law (input('Introduce la potencia (V): '), input('Introduce la resistencia (R): '), input('Introduce la intensidad (I): '))
