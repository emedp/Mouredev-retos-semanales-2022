'''
 * Reto #35
 * BATALLA POKÉMON
 * Fecha publicación enunciado: 29/08/22
 * Fecha publicación resolución: 06/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
'''

pokemon_types_table = {
    'agua': {
      'efective':['fuego'],
      'resistence':['planta', 'agua']
    },
    'fuego': {
        'efective': ['planta'],
        'resistence': ['agua', 'fuego']
    },
    'planta': {
        'efective': ['agua'],
        'resistence': ['fuego','planta']
    },
    'eléctrico': {
        'efective': ['agua'],
        'resistence': ['eléctrico', 'planta']
    }
}
pokemon_types = list( pokemon_types_table.keys() )

def pokemon_atack (type_move: str, type_pokemon: str, atack: int, defense: int):
    # VARIABLES
    damage = 0
    efectivity = 1

    # CONTROLS
    # los tipos existen
    if pokemon_types.count(type_move) == 0:
        return print ('Ese tipo Pokémon del movimiento no es válido.')

    if pokemon_types.count(type_pokemon) == 0:
        return print ('Ese tipo Pokémon del Pokémon no es válido.')

    # los valores de ataque y defensa están entre 1 y 100
    if atack < 1 or atack > 100:
        return print ('El ataque no tiene un valor válido.')

    if defense < 1 or defense > 100:
        return print('La defensa no tiene un valor válido.')

    # CALCULATEDS
    # efectivity
    pokemon_type = pokemon_types_table[type_move]
    
    if pokemon_type['efective'].count(type_pokemon) == 1:
        print ('¡Es súper eficaz!')
        efectivity = 2
    
    if pokemon_type['resistence'].count(type_pokemon) == 1:
        print ('No es muy eficaz...')
        efectivity = 0.5

    # ALGORITHM
    damage = 50 * ( atack / defense ) * efectivity
    print('Daño inflingido: ', damage)

    return damage

type_move = input (' Introduce el tipo del movimiento del Pokémon atacante: ')
type_pokemon = input('Introduce el tipo del Pokémon defensor: ')
atack = int ( input ( 'Introduce el valor de ataque del Pokémon atacante: ' ) )
defense = int ( input( 'Introduce el valor de defensa del Pokémon defensor: ' ) )

damage = pokemon_atack (type_move, type_pokemon, atack, defense)
