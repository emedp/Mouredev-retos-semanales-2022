'''
 * Reto #12
 * ¿ES UN PALÍNDROMO?
 * Fecha publicación enunciado: 21/03/22
 * Fecha publicación resolución: 28/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
'''
import string

def palindrome (text:str):

    # VARIABLES
    validation = True

    # MAIN CODE

    # text without punctuation and in lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace(" ", "")
    text = text.lower()

    for position in range(len(text)):
        if text[position] != text[-position-1]:
            validation = False

    # PRINT TO CONSOLE
    print(text)

    # RETURN
    return validation


print(palindrome("Ana lleva al oso la avellana"))
print(palindrome(input("Introduce texto como candidato a palíndromo: ")))

