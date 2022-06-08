'''
 * Reto #19
 * CONVERSOR TIEMPO
 * Fecha publicación enunciado: 09/05/22
 * Fecha publicación resolución: 16/05/22
 * Dificultad: FACIL
 *
 * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
'''

def to_miliseconds (days:int, hours:int, minutes:int, seconds:int):
    days    = days * 24 * 60 * 60 * 1000
    hours   = hours * 60 * 60 * 1000
    minutes = minutes * 60 * 1000
    seconds = seconds * 1000

    # PRINT CONSOLE
    print('Días en milisegundos: ' + str(days))
    print('Horas en milisegundos: ' + str(hours))
    print('Minutos en milisegundos: ' + str(minutes))
    print('Segundos en milisegundos: ' + str(seconds))
    print('total en milisegundos: ' + str(days + hours + minutes + seconds))

    # RETURN
    return (days + hours + minutes + seconds)

input_days      = int(input('Días: '))
input_hours     = int(input('Horas: '))
input_minutes   = int(input('Minutos: '))
input_seconds   = int(input('Segundos: '))

to_miliseconds(input_days, input_hours, input_minutes, input_seconds)
