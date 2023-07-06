'''
 * Reto #45
 * CONTENEDOR DE AGUA
 * Fecha publicación enunciado: 07/10/22
 * Fecha publicación resolución: 14/11/22
 * Dificultad: MEDIA
 *
 * Enunciado: Dado un array de números enteros positivos, donde cada uno representa unidades
 * de bloques apilados, debemos calcular cuantas unidades de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *          ⏹
 *          ⏹
 *   ⏹💧💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹
 *   ⏹💧⏹⏹💧 ⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua.
 *   Suponemos que existe un suelo impermeable en la parte inferior que retiene el agua.
'''

def water_container (container: list):
    representation = ""

    # calculate water array
    print(container)
    
    # hacer por tramos buscando los máximos, contando los huecos de agua que entran a cada iteración. al aparecer un nuevo maximo se cierra el tramo
    for position in range(0, len(container)):
        representation += "⏹︎ " * container[position]
        representation += "\n"

    print(representation)


water_container([4, 0, 3, 6, 1, 3])
