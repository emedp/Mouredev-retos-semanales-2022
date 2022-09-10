'''
 * Reto #36
 * LOS ANILLOS DE PODER
 * Fecha publicación enunciado: 06/09/22
 * Fecha publicación resolución: 14/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron
 * contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la
 *   suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco, 2 Pelosos empatan contra 1 Orco, 3 Pelosos ganan a 1 Orco.
'''

puntos_razas_buenas = {
    'Pelosos': 1,
    'Sureños buenos': 2,
    'Enanos': 3,
    'Númenóreanos': 4,
    'Elfos': 5,
}

puntos_razas_malvadas = {
    'Sureños malos': 2,
    'Orcos': 2,
    'Goblins': 2,
    'Huargos': 3,
    'Trolls': 5,
}

def batalla (ejercito_del_bien: list, ejercito_del_mal: list):
    resultado_batalla = 'Empate'
    puntos_batalla = 0
    puntos_ejercito_bueno = 0
    puntos_ejercito_malvado = 0

    # Mapear las razas de cada ejercito con su respectiva tabla de puntos
    # Multiplicar cada raza por el número de integrantes que posee
    # Sumar los puntos para cada ejercito
    for raza in ejercito_del_bien:
        puntos_ejercito_bueno += puntos_razas_buenas[raza['nombre_raza']] * raza['integrantes']

    for raza in ejercito_del_mal:
        puntos_ejercito_malvado += puntos_razas_malvadas[raza['nombre_raza']] * raza['integrantes']

    # Calcular la diferencia entre puntos (+) gana el bien, (0) empate, (-) gana el mal
    puntos_batalla = puntos_ejercito_bueno - puntos_ejercito_malvado

    print('puntos buenos: ', puntos_ejercito_bueno)
    print('puntos malos: ', puntos_ejercito_malvado)
    print('puntos batalla: ', puntos_batalla)

    if (puntos_batalla > 0):
        resultado_batalla = 'Gana el bien'
    elif (puntos_batalla < 0):
        resultado_batalla = 'Gana el mal'

    # Devolver el resultado de la batalla
    return resultado_batalla

ejercito_bueno = [
    {'nombre_raza': 'Elfos', 'integrantes': 4},
    {'nombre_raza': 'Enanos', 'integrantes': 5},
    {'nombre_raza': 'Pelosos', 'integrantes': 10},
]

ejercito_malo = [
    {'nombre_raza': 'Orcos', 'integrantes': 5},
    {'nombre_raza': 'Goblins', 'integrantes': 5},
    {'nombre_raza': 'Huargos', 'integrantes': 5},
    {'nombre_raza': 'Trolls', 'integrantes': 4},
]

resultado_batalla = batalla(ejercito_bueno, ejercito_malo)
print(resultado_batalla)
