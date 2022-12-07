'''
 * Reto #47
 * VOCAL MÁS COMÚN
 * Fecha publicación enunciado: 21/11/22
 * Fecha publicación resolución: 28/11/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un función que reciba un texto y retorne la vocal que más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
'''

def count_vowels (text: str):
    vowels = {
        'a' : 0,
        'e' : 0,
        'i' : 0,
        'o' : 0,
        'u': 0,
    }
    max_vowel_letter = ''
    max_vowel_times = 0

    text = text.lower()
    
    for letter in text:
        if letter == 'a':
            vowels['a'] += 1
        if letter == 'e':
            vowels['e'] += 1
        if letter == 'i':
            vowels['i'] += 1
        if letter == 'o':
            vowels['o'] += 1
        if letter == 'u':
            vowels['u'] += 1

    for vowel in vowels:
        if vowels[vowel] > max_vowel_times:
            max_vowel_letter = vowel
            max_vowel_times = vowels[vowel]

    print('Frecuencia de vocales en el texto:')
    print('a: ' + str(vowels['a']))
    print('e: ' + str(vowels['e']))
    print('i: ' + str(vowels['i']))
    print('o: ' + str(vowels['o']))
    print('u: ' + str(vowels['u']))

    print('La vocal más repetida es la "' + max_vowel_letter + '" con un total de ' + str(max_vowel_times) + ' veces')

count_vowels(input('Introduce el texto para contar sus vocales: '))
