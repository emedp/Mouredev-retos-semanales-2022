'''
 * Reto #32
 * EL SEGUNDO
 * Fecha publicación enunciado: 08/08/22
 * Fecha publicación resolución: 15/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.
'''

def second_greater (list: list):
    second = 0

    list.sort()
    second = list[-2]

    return second


lista = [9, 4, 7, 3, 6]
print("El segundo mayor de", lista, "es el", second_greater(lista))
