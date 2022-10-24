'''
 * Reto #37
 * LOS LANZAMIENTOS DE "THE LEGEND OF ZELDA"
 * Fecha publicación enunciado: 14/09/22
 * Fecha publicación resolución: 19/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! Se llamará "Tears of the Kingdom"
 * y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto
 *   puedes usar el mes, o incluso inventártelo)
'''


# La información de los juegos se ha extraído de Wikipedia: https://es.wikipedia.org/wiki/Anexo:Videojuegos_de_The_Legend_of_Zelda
# Las fechas se han tomado la fecha de publicación original japonesa
zelda_games = {
    1: {
        'name': 'The Legend of Zelda',
        'release' : '21/02/1986'
    },
    2: {
        'name': 'The Adventure of Link',
        'release': '14/01/1987'
    },
    3: {
        'name': 'A Link to the Past',
        'release': '21/11/1991'
    },
    4: {
        'name': 'Link\'s Awakening',
        'release': '06/06/1993'
    },
    5: {
        'name': 'Ocarina of Time',
        'release': '21/11/1998'
    },
    6: {
        'name': 'Majora\'s Mask',
        'release': '27/04/2000'
    },
    7: {
        'name': 'Oracle of Seasons y Oracle of Ages',
        'release': '27/02/2001'
    },
    8: {
        'name': 'The Wind Waker',
        'release': '13/12/2002'
    },
    9: {
        'name': 'A Link to the Past',
        'release': '14/03/2003'
    },
    10: {
        'name': 'Four Swords Adventures',
        'release': '18/03/2004'
    },
    11: {
        'name': 'The Minish Cap',
        'release': '04/11/2004'
    },
    12: {
        'name': 'Twilight Princess',
        'release': '02/12/2006'
    },
    13: {
        'name': 'Phantom Hourglass',
        'release': '23/06/2007'
    },
    14: {
        'name': 'Spirit Tracks',
        'release': '23/12/2009'
    },
    15: {
        'name': 'Skyward Sword',
        'release': '23/11/2011'
    },
    16: {
        'name': 'A Link Between Worlds',
        'release': '26/12/2013'
    },
    17: {
        'name': 'Tri Force Heroes',
        'release': '22/10/2015'
    },
    18: {
        'name': 'Breath of the Wild',
        'release': '03/03/2017'
    },
    19: {
        'name': 'Tears of the Kingdom',
        'release': '12/05/2023'
    },
}

def time_between_games_zelda (game1: int, game2: int):

    diference = ""

    # descomponen las fechas en dia/mes/año
    date1 = zelda_games[game1]['release'].split("/")
    date2 = zelda_games[game2]['release'].split("/")

    diff_years = abs(int(date1[2]) - int(date2[2]))
    diff_months = abs(int(date1[1]) - int(date2[1]))
    diff_days = abs(int(date1[0]) - int(date2[0]))

    if int(date1[2]) < int(date2[2]) and int(date1[1]) > int(date2[1]):
        diff_years = diff_years - 1
        diff_months = 12 - abs(int(date1[1]) - int(date2[1]))

    diference = str(diff_years) + " años " + str(diff_months) + " meses y " + str(diff_days) + " días"

    return print (zelda_games[game1]['name'] + ' y ' + zelda_games[game2]['name'] + ' tienen una diferencia de: ' + diference)

for game in zelda_games:
    print( str(game) + '. ' + zelda_games[game]['name'] + ' - ' + zelda_games[game]['release'] )

game1 = int(input('Select the first game by his number: '))
game2 = int(input('Select the second game by his number: '))

time_between_games_zelda(game1, game2)
