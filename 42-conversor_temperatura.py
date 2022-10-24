'''
 * Reto #42
 * CONVERSOR DE TEMPERATURA
 * Fecha publicación enunciado: 17/10/22
 * Fecha publicación resolución: 24/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
'''

def temperature_unity_conversor (temperature: int, unity: str):
    result = 0
    out_message = ''
    if unity == 'ºC':
        result = (temperature * 9 / 5) + 32
        out_message = 'El resultado es: ' + str(result) + ' ºF'
    elif unity == 'ºF':
        result = (temperature - 32) * 5 / 9
        out_message = 'El resultado es: ' + str(result) + ' ºC'
    else:
        out_message = 'La unidad indicada no es correcta'

    print(out_message)


unity = input('Indica que unidad de temperatura vas a convertir (ºC o ºF): ')
temperature = int(input('Indica los grados de temperatura: '))

temperature_unity_conversor(temperature, unity)
