'''
 * Reto #34
 * LOS NÚMEROS PERDIDOS
 * Fecha publicación enunciado: 22/08/22
 * Fecha publicación resolución: 29/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule
 * y retorne todos los que faltan entre el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
'''

def missing_numbers (array: list):
    missing_numbers_list = []
    
    # check if array is sort and unique values
    last_number = 0
    for number in array:
        if last_number == 0:
            last_number = number
        
        if last_number > number:
            return "Error: el array no está ordenado de forma ascendiente."

        if array.count(number) > 1:
            return "Error: el array contiene valores repetidos."
        
        last_number = number

    # search for missing numbers in the array
    min = array[0]
    max = array[-1]

    for number in range(min,max):
        if array.count(number) == 0:
            missing_numbers_list.append(number)
    
    return missing_numbers_list

array = [1, 2, 4, 7, 9]
print(missing_numbers(array))
