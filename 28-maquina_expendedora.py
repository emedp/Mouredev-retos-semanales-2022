'''
 * Reto #28
 * MÁQUINA EXPENDEDORA
 * Fecha publicación enunciado: 11/07/22
 * Fecha publicación resolución: 18/07/22
 * Dificultad: MEDIA
 *
 * Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección del producto.
 * - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor
 *   número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje
 *   y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
'''

products = {
    1 : {
        "nombre": "Agua",
        "precio": 100,
        "cantidad": 10,
    },
    2 : {
        "nombre": "Coca-Cola",
        "precio": 215,
        "cantidad": 2,
    },
    3 : {
        "nombre": "Nestea",
        "precio": 155,
        "cantidad": 5,
    },
    4 : {
        "nombre": "Donuts",
        "precio": 175,
        "cantidad": 4,
    }
}

avaliable_coins = [5, 10, 20, 50, 100, 200]
avaliable_coins = [200, 100, 50, 20, 10, 5]

def maquina_expendedora (list_coins: list, selected_product: int):

    balance = 0
    money_back = 0
    # comprobamos que las monedas introducidas son validas
    for coin in list_coins:
        balance += coin
        if avaliable_coins.count(coin) == 0:
            return print("Se han introducido monedas falsas.", list_coins)
        
    # check el numero del producto es valido
    if products.get(selected_product) == None:
        return print("El producto seleccionado no existe.", list_coins)

    # check saldo suficiente
    money_back = balance - products[selected_product]["precio"]

    if money_back < 0:
        return print("El dinero introducido es insuficiente.", list_coins)

    # calculo de monedas a devolver
    list_coins.clear()
    for coin in avaliable_coins:
        while coin <= money_back and money_back != 0:
            money_back -= coin
            list_coins.append(coin)
    
    return print("Se ha seleccionado:", products[selected_product]["nombre"], "\nAquí está su vuelta:", list_coins)


maquina_expendedora([100,60, 200], 1)
maquina_expendedora([100, 50, 200], 7)
maquina_expendedora([20], 1)
maquina_expendedora([200,100], 1)
maquina_expendedora([200,100], 2)
maquina_expendedora([200,100], 3)
maquina_expendedora([200,100], 4)
