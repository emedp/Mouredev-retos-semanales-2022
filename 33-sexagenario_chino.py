'''
 * Reto #33
 * CICLO SEXAGENARIO CHINO
 * Fecha publicación enunciado: 15/08/22
 * Fecha publicación resolución: 22/08/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
 * en el ciclo sexagenario del zodíaco chino.
 * - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos madera,
 *   fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
 *   caballo, oveja, mono, gallo, perro, cerdo (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
'''

troncos_celestiales = [
    "madera",
    "fuego",
    "tierra",
    "metal",
    "agua"
]

ramas_terrenales = [
    "rata",
    "buey",
    "tigre",
    "conejo",
    "dragón",
    "serpiente",
    "caballo",
    "oveja",
    "mono",
    "gallo",
    "perro",
    "cerdo"
]

def combinaciones_sexagenario_chino():
    combinaciones = []
    pos_animal = 0
    pos_elemento = 0

    while len(combinaciones) != 60:
        pos_elemento %= len(troncos_celestiales)
        pos_animal %= len(ramas_terrenales)

        combinaciones.append(troncos_celestiales[pos_elemento] + " " + ramas_terrenales[pos_animal])
        pos_animal = pos_animal + 1
        combinaciones.append(troncos_celestiales[pos_elemento] + " " + ramas_terrenales[pos_animal])
        pos_animal += 1
        pos_elemento += 1
    
    return combinaciones

sexagenario_list = combinaciones_sexagenario_chino()

def sexagenario_chino (year: int):
    year_cicle_reference = 1984

    position = abs(year - year_cicle_reference) % 60

    return sexagenario_list[position]


year = input("Introduce un año a consultar su valor de elemento y animal en el ciclo sexagenario chino:")
print("El elemento y animal de", year,"corresponde con:", sexagenario_chino(int(year)))
