'''
 * Reto #22
 * CONJUNTOS
 * Fecha publicación enunciado: 01/06/22
 * Fecha publicación resolución: 07/06/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''

def conjuntos (array1: list, array2: list, boolean: bool):
    
    arrayFinal = list()
    merge = array1.copy()
    merge.extend(array2)
    merge.sort()

    if boolean: # devolver los valores comunes
        for element in merge:
            if merge.count(element) == 2 and arrayFinal.count(element) == 0:
                arrayFinal.append(element)

    else: # devolver los valores distintos
        for element in merge:
            if merge.count(element) == 1:
                arrayFinal.append(element)
    
    return arrayFinal

print(conjuntos([1,3,5,7,9],[1,2,3,4,5], True))
