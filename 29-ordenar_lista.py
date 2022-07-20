'''
 * Reto #29
 * ORDENA LA LISTA
 * Fecha publicación enunciado: 18/07/22
 * Fecha publicación resolución: 26/07/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional
 *   "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''

def ordenar_lista (array: list, order: str):

    if order == "Asc":
        array.sort()
    elif order == "Desc":
        array.sort(reverse=True)

    return print(array)

ordenar_lista([60, 70, 55, 22, 55, 4, 7, 1], "Asc")
ordenar_lista([60, 70, 55, 22, 55, 4, 7, 1], "Desc")
