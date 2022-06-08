'''
 * Reto #11
 * ELIMINANDO CARACTERES
 * Fecha publicación enunciado: 14/03/22
 * Fecha publicación resolución: 21/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
'''

def del_caracters (string1:str, string2:str):

    # VARIABLES
    out1 = ""
    out2 = ""

    # MAIN CODE
    string1.lower()
    string2.lower()

    for character in string1:
        if character not in string2 and character not in out1:
            out1 = out1 + character

    for character in string2:
        if character not in string1 and character not in out2:
            out2 = out2 + character
    
    # PRINT TO CONSOLE

    # RETURN
    return out1, out2

string1 = input("Introduce una cadena: ")
string2 = input("Introduce otra cadena: ")
result = del_caracters(string1, string2)
print(result)
