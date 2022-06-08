'''
* Reto #20
 * PARANDO EL TIEMPO
 * Fecha publicación enunciado: 16/05/22
 * Fecha publicación resolución: 23/05/22
 * Dificultad: MEDIA

 * Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal.
 * - Se podría ejecutar varias veces al mismo tiempo.
'''
import asyncio

async def sum_waiting (num1: int, num2: int, seconds: int):
    await asyncio.sleep(seconds)
    print('total suma: ' + str(num1 + num2))

num1 = int(input('introduce un valor: '))
num2 = int(input('introduce un valor: '))
seconds = int(input('segundos en espera: '))

asyncio.run(sum_waiting(num1, num2, seconds))
