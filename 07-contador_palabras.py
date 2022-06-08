'''
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''
import string


def word_counter(text:str):
    
    # VARIABLES
    total_words = 0
    array = []

    # Crear una estructura de datos 'diccionario' con pares {clave - valor} siendo {palabra - numero}
    dictionary = {}


    # MAIN CODE

    # pasar todo el texto a minusculas
    text = text.lower()
    # Eliminar los signos de puntuacion
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Dividir el texto en palabras
    array = text.split(' ')
    # recorrer la lista de palabras
    # si es una palabra nueva, añadirla al diccionario, si no +1 a su valor en el diccionario
    for word in array:
        if word in dictionary.keys():
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1
    

    # PRINT IN CONSOLE
    print("Output de las variables")
    print(text)
    print(array)
    print(dictionary)

    # RETURN
    print("\nListado de palabras y veces que se repite:")
    for word in dictionary:
        print (word + " - " + str(dictionary[word]))
    
    print("\nTotal de palabras: " + str(len(array)))


word_counter('Contador de palabras, (y contador por palabras)?')
