'''
 * Reto #46
 * ¿DÓNDE ESTÁ EL ROBOT?
 * Fecha publicación enunciado: 14/11/22
 * Fecha publicación resolución: 21/11/22
 * Dificultad: MEDIA
 *
 * Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cuadrícula
 * representada por los ejes "x" e "y".
 * - El robot comienza en la coordenada (0, 0).
 * - Para idicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos)
 *   que indican la secuencia de pasos a dar.
 *  - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene, luego 5, se detiene,
 *    y finalmente 2. El resultado en este caso sería (x: -5, y: 12)
 * - Si el número de pasos es negativo, se desplazaría en sentido contrario al que está mirando.
 * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando hacia la parte
 *   positiva del eje "y".
 * - El robot tiene un fallo en su programación: cada vez que finaliza una secuencia de pasos gira
 *   90 grados en el sentido contrario a las agujas del reloj.
'''

def move_robot (steps: list):
    x = 0
    y = 0

    for step in range(0, len(steps)):
        # cada paso gira 90 grados, cada 4 una vuelta completa
        # y +
        if step % 4 == 0:
            y += steps[step]
        # x -
        if step % 4 == 1:
            x -= steps[step]
        # y -
        if step % 4 == 2:
            y -= steps[step]
        # x +
        if step % 4 == 3:
            x += steps[step]

    print("x: " + str(x) + " y: " + str(y))

move_robot([10,5,-2])