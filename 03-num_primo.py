'''
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def check_prime_num(number):
    if number <= 1: return False

    for i in range(2,number):
        if number % i == 0: return False

    return True


for x in range(1,101):
    if check_prime_num(x):
        print(x)

