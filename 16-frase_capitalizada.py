'''
 * Reto #16
 * EN MAYÚSCULA
 * Fecha publicación enunciado: 18/04/22
 * Fecha publicación resolución: 25/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''

def capitalize_phrase (phrase):
    phrase_capitalized = ""
    phrase_splitted = phrase.split(" ")

    for word in phrase_splitted:
        phrase_capitalized = phrase_capitalized + word.capitalize() + " "

    return phrase_capitalized

phrase = input("Introduce una frase a capitalizar: ")
print(capitalize_phrase(phrase))
