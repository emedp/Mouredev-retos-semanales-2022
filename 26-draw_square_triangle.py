'''
 * Reto #26
 * CUADRADO Y TRIÁNGULO 2D
 * Fecha publicación enunciado: 27/06/22
 * Fecha publicación resolución: 07/07/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
'''

def draw_figure (figure: str, side: int):
    if figure == 'square':
        draw_square(side)
    elif figure == 'triangle':
        draw_triangle(side)


def draw_square (side: int):
    print('\nSQUARE')
    for row in range(side):
        for column in range(side):
            if column != side-1:
                print('*  ',end='')
            else:
                print('*')

def draw_triangle (side: int):
    print('\nTRIANGLE')
    for row in range(side):
        for column in range(row + 1):
            if column != row:
                print('*  ', end='')
            else:
                print('*')


draw_figure('square', 3)
draw_figure('triangle', 4)
