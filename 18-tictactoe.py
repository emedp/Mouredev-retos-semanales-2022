'''
 * Reto #18
 * TRES EN RAYA
 * Fecha publicación enunciado: 02/05/22
 * Fecha publicación resolución: 09/05/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
'''

from cgitb import reset


def validate_tictactoe_game (board_tictactoe):

    # VARIABLES
    result = ""
    win_X = False
    win_O = False

    # MAIN CODE
    # verificate correct board and game
    if not len(board_tictactoe) == 3:
        return "Nulo"
    elif not len(board_tictactoe[0]) == 3:
        return "Nulo"
    elif not len(board_tictactoe[1]) == 3:
        return "Nulo"
    elif not len(board_tictactoe[2]) == 3:
        return "Nulo"
    
    # verificate horizontal
    for row in board_tictactoe:
        if row == ['X','X','X']:
            win_X = True
        elif row == ['O', 'O', 'O']:
            win_O = True
    
    # verificate vertical
    for column in range(3):
        if board_tictactoe[0][column] == board_tictactoe[1][column] and board_tictactoe[0][column] == board_tictactoe[2][column]:
            if board_tictactoe[0][column] == 'X':
                win_X = True
            elif board_tictactoe[0][column] == 'O':
                win_O = True

    # verificate diagonal

    # PRINT CONSOLE
    if win_X and win_O:
        result = "Nulo"
    elif not win_X and not win_O:
        result = "Empate"
    elif win_O:
        result = 'O'
    elif  win_X:
        result = 'X'
    

    # RETURN
    return result


# NULO: por ganar los 2
board_tictactoe = [
    ['X', 'O', 'X'],
    ['X', 'O', 'X'],
    ['X', 'O', 'X'],
]
print (validate_tictactoe_game(board_tictactoe))

# EMPATE
board_tictactoe = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'O'],
]
print (validate_tictactoe_game(board_tictactoe))

# GANA X: horizontal
board_tictactoe = [
    ['X', 'X', 'X'],
    ['O', 'X', ''],
    ['O', '', 'O'],
]
print (validate_tictactoe_game(board_tictactoe))

# GANA O: vertical
board_tictactoe = [
    ['O', 'X', 'X'],
    ['O', 'O', ''],
    ['O', '', 'X'],
]
print (validate_tictactoe_game(board_tictactoe))
