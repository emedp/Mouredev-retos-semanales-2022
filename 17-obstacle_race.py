'''
 * Reto #17
 * LA CARRERA DE OBSTÁCULOS
 * Fecha publicación enunciado: 25/04/22
 * Fecha publicación resolución: 02/05/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
 *        variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
'''


def race (athlete_actions, running_track):
    # VARIABLES
    athlete_track = ''

    # MAIN CODE

    # transform athlete actions in athlete track
    # compare running track with athlete track
    for i in range(len(athlete_actions)):
        action      = athlete_actions[i]
        obstacle    = running_track[i]

        if action == 'run' and obstacle == '_':
            result = '_'
        elif action == 'run' and obstacle == '|':
            result = '/'
        elif action == 'jump' and obstacle == '|':
            result = '|'
        elif action == 'jump' and obstacle == '_':
            result = 'x'

        athlete_track = athlete_track + result

    # PRINT IN CONSOLE
    
    print ("athlete actions: ", end = '')
    print(athlete_actions)
    print ("running track: " + running_track)
    print ("athlete track: " + athlete_track)

    # RETURN
    # determinate if athlete has done the race well

    # The athelete is running other race...
    if len(running_track) is not len(athlete_actions):
        return False
    
    # the athelete runs all well or something bad happends
    if running_track == athlete_track:
        return True
    else:
        return False


actions = ['run', 'jump', 'run', 'jump']
result = race (actions, '_|_|')
print ("The athlete has done well the race?: " + str(result))

result = race(actions, '|_|_')
print("The athlete has done well the race?: " + str(result))

result = race(actions, '_||_')
print("The athlete has done well the race?: " + str(result))
