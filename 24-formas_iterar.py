'''
 * Reto #24
 * ITERATION MASTER
 * Fecha publicación enunciado: 13/06/22
 * Fecha publicación resolución: 20/06/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.
'''

# 1: For

def bucle_for ():
    for i in range(1,101):
        print(i)


# 2: While

def bucle_while ():
    i = 1
    while i <= 100:
        print(i)
        i += 1

bucle_for()
bucle_while()