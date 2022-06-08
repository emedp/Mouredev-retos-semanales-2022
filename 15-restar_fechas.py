'''
 * Reto #15
 * ¿CUÁNTOS DÍAS?
 * Fecha publicación enunciado: 11/04/22
 * Fecha publicación resolución: 18/04/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
'''

def verify_date (day, month, year):
    error_stack = ""
    wrong_month = False
    days_for_month = {
        "01": 31,
        "02": 28,
        "03": 31,
        "04": 30,
        "05": 31,
        "06": 30,
        "07": 31,
        "08": 31,
        "09": 30,
        "10": 31,
        "11": 30,
        "12": 31,
    }

    # comprobar si el año es dato correcto (4 digitos)
    if len(year) != 4:
        error_stack = error_stack + "El año " + year + " no es un valor correcto \n"

    # comprobar si el mes es dato correcto (2 digitos y menor que 13)
    if len(month) != 2 or int(month) > 12:
        error_stack = error_stack + "El mes " + month + " no es un valor correcto \n"
        wrong_month = True

    # comprobar si el dia es dato correcto (menor o igual a numero de días del mes)
    if not wrong_month:

        if int(day) >= days_for_month[month]:
            error_stack = error_stack + "El día " + day + " no es un valor correcto para el mes " + month + "\n"
    
    if error_stack != "":
        return error_stack

    return True


def distance_dates (date1, date2):

    diference = ""

    # descomponen las fechas en dia/mes/año
    date1 = date1.split("/")
    date2 = date2.split("/")

    # Verificación de fechas correctas
    check_date1 = verify_date(date1[0], date1[1], date1[2])
    check_date2 = verify_date(date2[0], date2[1], date2[2])

    if check_date1 != True or check_date2 != True:
        return check_date1 + check_date2

    diff_years  = abs(int(date1[2]) - int(date2[2]))
    diff_months = abs(int(date1[1]) - int(date2[1]))
    diff_days   = abs(int(date1[0]) - int(date2[0]))

    if int(date1[2]) < int(date2[2]) and int(date1[1]) > int(date2[1]):
        diff_years = diff_years - 1
        diff_months = 12 - abs(int(date1[1]) - int(date2[1]))

    diference = str(diff_years) + " años " + str(diff_months) + " meses y " + str(diff_days) + " días"

    return diference


print(distance_dates('25/111/blabla', '31/123/12345'))
print(distance_dates('32/12/1997', '31/02/2022'))
print(distance_dates('25/12/1997', '19/04/2022'))
print(distance_dates(input("introduce una fecha: "), input("Introduce otra fecha: ")))
