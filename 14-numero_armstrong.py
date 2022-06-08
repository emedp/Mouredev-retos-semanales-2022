'''
 * Reto #14
 * ¿ES UN NÚMERO DE ARMSTRONG?
 * Fecha publicación enunciado: 04/04/22
 * Fecha publicación resolución: 11/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.

 NUMERO ARMSTRONG: conocido en matemática recreativa como número narcisista,
 es aquel que es igual a la suma de sus dígitos elevados al número de sus cifras.
 153 = 1^3 + 5^3 + 3^3
'''

def is_armstrong (number):
    
    is_armstrong = False
    sum_of_digits = 0
    number = str(number)

    for digit in number:
        sum_of_digits = sum_of_digits + int(digit) ** len(number)

    is_armstrong = int(number) == int(sum_of_digits)

    return is_armstrong


print(is_armstrong(153))
print(is_armstrong(input("Introduce un numero para comprobar si es un número de Armstrong: ")))
