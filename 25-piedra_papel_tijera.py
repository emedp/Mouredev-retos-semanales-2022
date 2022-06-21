'''
 * Reto #25
 * PIEDRA, PAPEL, TIJERA
 * Fecha publicación enunciado: 20/06/22
 * Fecha publicación resolución: 27/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
'''

def rock_paper_scrissor_game (game: list):

    contador_player_1 = 0
    contador_player_2 = 0
    
    for par in game:
        if par[0] == "R":
            if par[1] == "S": contador_player_1 += 1
            if par[1] == "P": contador_player_2 += 1
        if par[0] == "P":
            if par[1] == "R": contador_player_1 += 1
            if par[1] == "S": contador_player_2 += 1
        if par[0] == "S":
            if par[1] == "P": contador_player_1 += 1
            if par[1] == "R": contador_player_2 += 1
    
    if contador_player_1 > contador_player_2: print("Player 1")
    elif contador_player_1 < contador_player_2: print("Player 2")
    else: print("Tie")


rock_paper_scrissor_game(
    [("R", "S"), ("S", "R"), ("P", "S")]
)
