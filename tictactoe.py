"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(3): 
        for j in range(3): 
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    return possible_moves


def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid Action!!!")

    b2 = copy.deepcopy(board)
    b2[action[0]][action[1]] = player(board)
    
    return b2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False            
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)
    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    best_value = -math.inf
    best_move = None

    for action in actions(board):
        val, _ = min_value(result(board, action), alpha, beta)
        if val > best_value:
            best_value = val
            best_move = action
            
        alpha = max(alpha, best_value)
        if alpha >= beta:
            break 
    return best_value, best_move


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    best_value = math.inf
    best_move = None

    for action in actions(board):
        val, _ = max_value(result(board, action), alpha, beta)
        
        if val < best_value:
            best_value = val
            best_move = action
            
        beta = min(beta, best_value)
        if alpha >= beta:
            break 
    return best_value, best_move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    alpha = -math.inf
    beta = math.inf

    if player(board) == X:
        _, best_move = max_value(board, alpha, beta)
        return best_move
    else:
        _, best_move = min_value(board, alpha, beta)
        return best_move