'''
 * Reto #31
 * AÑOS BISIESTOS
 * Fecha publicación enunciado: 01/08/22
 * Fecha publicación resolución: 08/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
'''

def bisiestos (year: int):
    years_list = []

    while year % 4 != 0:
        year = year + 1

    for i in range(30):
        years_list.append(year)
        year = year + 4
    
    print("Imprimiendo total de siguientes años bisiestos:", len(years_list))
    return years_list


print(bisiestos(2022))