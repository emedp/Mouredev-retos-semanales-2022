'''
 * Reto #48
 * EL CALENDARIO DE ADEVIENTO 2022
 * Fecha publicación enunciado: 28/11/22
 * Fecha publicación resolución: 05/12/22
 * Dificultad: FÁCIL
 *
 * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software, ciencia y tecnología desde el 1 de diciembre.
 *
 * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne lo siguiente:
 * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
 * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
 * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
 *
 * Notas:
 * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00 y finaliza a las 23:59:59.
 * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos y segundos.
 * - 🎁 Cada persona que aporte su solución entrará en un nuevo sorteo del calendario de aDEViento hasta el día de su corrección (sorteo exclusivo para quien entregue su solución).
'''
import datetime

def a_dev_iento (date: datetime.datetime):
    init = datetime.datetime(2022,12,1)
    finish = datetime.datetime(2022,12,25)

    if date < init:
        print("El evento empieza en:")
        print(init - date)
    
    if date > finish:
        print("El evento terminó hace:")
        print(date - finish)
    
    if init < date and date < finish:
        print("Te ha tocado el premio del día: " + str(date.day))
        print("El sorteo de hoy acabará en: " + str((datetime.datetime(date.year, date.month, date.day + 1) - date)))

    
y = int(input("Introduce el año: "))
m = int(input("Introduce el mes: "))
d = int(input("Introduce el día: "))
h = int(input("Introduce la hora: "))
n = int(input("Introduce los minutos: "))
s = int(input("Introduce los segundos: "))

a_dev_iento(datetime.datetime(y, m, d, h, n, s))
