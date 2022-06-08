'''
 * Reto #23
 * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
 * Fecha publicación enunciado: 07/06/22
 * Fecha publicación resolución: 13/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''

def factores_primos(num: int):
    
    lista_factores_primos = list()
    divisor = 2

    while (num != 1):
        
        if num % divisor == 0:
            num /= divisor
            lista_factores_primos.append(divisor)
            divisor = 1
        
        divisor += 1
    
    return lista_factores_primos


def mcm (num1: int, num2: int):
    print("MAXIMO COMUN MULTIPLO:")
    mcm = 1
    fp1 = factores_primos(num1)
    fp2 = factores_primos(num2)

    bases = set(fp1)
    bases.update(fp2)

    for primo in bases:
        exp1 = fp1.count(primo)
        exp2 = fp2.count(primo)
        if exp1 > exp2:
            mcm *= primo ** exp1
        else:
            mcm *= primo ** exp2
    
    return mcm


def mcd (num1: int, num2: int):
    print("MAXIMO COMUN DIVISOR:")
    mcd = 1
    fp1 = factores_primos(num1)
    fp2 = factores_primos(num2)

    bases = set(fp1).intersection(fp2)

    for primo in bases:
        exp1 = fp1.count(primo)
        exp2 = fp2.count(primo)
        if exp1 < exp2:
            mcd *= primo ** exp1
        else:
            mcd *= primo ** exp2
    
    return mcd



num1 = input('Introduce un valor: ')
num2 = input('Introduce un valor: ')
num1 = int(num1)
num2 = int (num2)

print(factores_primos(num1))
print(factores_primos(num2))
print(mcm(num1, num2))
print(mcd(num1, num2))
