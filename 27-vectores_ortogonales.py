'''
 * Reto #27
 * VECTORES ORTOGONALES
 * Fecha publicación enunciado: 07/07/22
 * Fecha publicación resolución: 11/07/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
'''

'''
dos vectores son orgonales cuando forman un angulo de 90º, es decir,
cuando su producto escalar es igual a 0.
producto escalar: (a1, a2).(b1, b2) = a1.b1 + a2.b2 = 0
'''
def ortogonal_vectors (vector1: list, vector2: list):
    # check vectors only have 2 values
    if len(vector1) != 2 or len(vector2) != 2:
        return print("El tamaño de los vectores no es correcto.")

    producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1]

    if producto_escalar == 0:
        return print("Los vectores son ortogonales.")
    else:
        return print("Los vectores NO son ortogonales.")
    



ortogonal_vectors([1, 2], [2, 3, 4])
ortogonal_vectors([1, 2], [2, 3])
ortogonal_vectors([2, 1], [-1, 2])
