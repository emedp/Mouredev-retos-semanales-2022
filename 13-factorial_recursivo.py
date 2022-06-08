'''
 * Reto #13
 * FACTORIAL RECURSIVO
 * Fecha publicación enunciado: 28/03/22
 * Fecha publicación resolución: 04/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
'''

def factorial (num):
    result = 1
    if num >= 1:
        result = num * factorial(num-1)
        
    return result

num_factorizar = input('Introduce el número a calcular su factorial: ')
num_factorizar = int(num_factorizar)
print('El factorial de', num_factorizar, '=', factorial(num_factorizar))

