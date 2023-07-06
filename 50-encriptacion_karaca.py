'''
 * Reto #50
 * LA ENCRIPTACIÓN DE KARACA
 * Fecha publicación enunciado: 12/12/22
 * Fecha publicación resolución: 19/12/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto utilizando el
 * algoritmo de encriptación de Karaca (debes buscar información sobre él).
'''

def karaca_algorith (encript: str):
    result = ""
    encript = encript.lower()
    words = encript.split()

    for word in words:
        word = word.replace("a", "0")
        word = word.replace("e", "1")
        word = word.replace("i", "2")
        word = word.replace("o", "3")
        word = word.replace("u", "4")
        result += word [::-1] + "aca "

    print(result)

text = input("Introduce el texto a encriptar:\n")
karaca_algorith(text)