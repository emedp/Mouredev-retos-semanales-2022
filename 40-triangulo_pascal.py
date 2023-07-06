'''
 * Reto #40
 * TRIÁNGULO DE PASCAL
 * Fecha publicación enunciado: 03/10/22
 * Fecha publicación resolución: 10/10/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
 * únicamente el tamaño del lado.
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
'''

def pascal_triangle (size: int):
    triangle = []
    for row in range(0, size):
        pascal_row = []
        for position in range(0, row + 1):
            if position == 0 or position == row:
                pascal_row.append(1)
            else:
                father_L = triangle[row-1][position-1]
                father_R = triangle[row-1][position]
                pascal_row.append(father_L +  father_R)
        triangle.append(pascal_row)

    
    for row in triangle:
        print(row)

triangle_size = int(input('Introduce el número de altura del triángulo de Pascal: '))
pascal_triangle(triangle_size)
