'''
 * Reto #30
 * MARCO DE PALABRAS
 * Fecha publicación enunciado: 26/07/22
 * Fecha publicación resolución: 01/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un texto y muestre cada palabra en una línea, formando
 * un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
'''
def border_words (text: str):
    # VARIABLES
    text_bordered = ''
    border = ''
    array_words = []
    size_long_word = 0
    
    # guardar en un array el texto recibido dividido por palabras
    array_words = text.split(' ')
    
    
    # buscar y contar la palabra más larga
    for word in array_words:
        if len(word) > size_long_word:
            size_long_word = len(word)

    # guardar en una variable el marco superior que debe ser la longitud de la palabra más larga + 4
    border = '*' * (size_long_word + 4) + '\n'
    text_bordered += border

    # hacer un bucle que concatene a la variable a retornar las palabras del array de forma que:
    # empiece en '* ' más la palabra más los espacio en medio para formar un rectágulo y acabe con ' *'
    for word in array_words:
        text_bordered += '* ' + word + ' ' * (size_long_word - len(word)) + ' *\n'

    # concatenar a la variable a retornar el marco inferior con la misma norma que el superior
    text_bordered += border

    return print(text_bordered)

border_words('Hola soy Emedp')
border_words('Enmarcar las palabras para formato')
