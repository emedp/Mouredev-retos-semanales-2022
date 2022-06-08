'''
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
'''

morse_code = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'Ñ':'--.--',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '"': '.-..-.',
    '/': '-..-.',
}
morse_code_reversed = { value : key for key, value in morse_code.items()}

def natural_morse (text:str):
    
    # VARIABLES
    text_splitted = []
    translation = ""
    is_morse = True

    # MAIN CODE
    if '-' not in text and '.' not in text:
        is_morse = False
    
    if is_morse:
        # split text in words
        text_splitted = text.split("  ")
        
        # store text splitted (array) in translation with conversion
        for word in text_splitted:
            word = word.split()
            for code in word:
                translation = translation + morse_code_reversed[code]
            translation = translation + " " # Space to separete words



    else:
        # text to uppercase
        text = text.upper()

        # split text in words
        text_splitted = text.split()

        # store text splitted (array) in translation with conversion
        for word in text_splitted:
            for letter in word:
                translation = translation + morse_code[letter] + ' ' # one space
            translation = translation + ' ' # +1 space, between words needs to be 2  

    # PRINT CONSOLE
    print("Text: " + text)
    print("Is morse: " + str(is_morse))
    print("Translation: " + translation)
    print()

    # RETURN
    return translation

natural_text = input("Introduce texto para traducir a morse: ")
natural_morse(natural_morse(natural_text))