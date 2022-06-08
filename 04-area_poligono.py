'''
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

from cmath import sqrt


def area_poligono(sides):
    sides.sort()
    print(sides)
    number_sides = len(sides)

    if number_sides == 3:
        # Se puede calcular el area con solo sus lados, sin utilizar la famosa (base * altura)/2
        # Para eso se utiliza la fórmula de Herón
        semiperimetro = (sides[0] + sides[1] + sides[2]) / 2
        area_tri = sqrt(semiperimetro * (semiperimetro - sides[0]) * (semiperimetro - sides[1]) * (semiperimetro - sides[2]))
        print('Area del triángulo:', area_tri)

    if number_sides == 4:
        if sides[0] == sides[1] == sides[2] == sides[3]:
            print('Area del cuadrado es:', sides[0] * sides[1])

        if sides[0] == sides[1] and sides[2] == sides[3] and sides[0] != sides[2]:
            print('Area del rectángulo:', sides[0] * sides[2])
    
    
area_poligono([20,20,20])
area_poligono([15, 15, 15,15])
area_poligono([15, 15, 25,25])
