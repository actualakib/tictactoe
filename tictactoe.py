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
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


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
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


'''
FUNCTION Minimax(board):
    IF board is terminal THEN
        RETURN None

    alpha ← -infinity     // best value Maximizer can guarantee so far
    beta  ← +infinity     // best value Minimizer can guarantee so far

    IF current player is X (Maximizer) THEN
        RETURN second element of MaxValue(board, alpha, beta)   // the move
    ELSE
        RETURN second element of MinValue(board, alpha, beta)   // the move


FUNCTION MaxValue(board, alpha, beta):
    IF board is terminal THEN
        RETURN (Utility(board), None)

    bestValue ← -infinity
    bestMove  ← None

    FOR EACH action IN Actions(board):
        (value, _) ← MinValue(Result(board, action), alpha, beta)
        alpha ← max(alpha, value)

        IF value > bestValue THEN
            bestValue ← value
            bestMove  ← action

        IF alpha >= beta THEN     // beta cut-off (prune remaining branches)
            BREAK

    RETURN (bestValue, bestMove)


FUNCTION MinValue(board, alpha, beta):
    IF board is terminal THEN
        RETURN (Utility(board), None)

    bestValue ← +infinity
    bestMove  ← None

    FOR EACH action IN Actions(board):
        (value, _) ← MaxValue(Result(board, action), alpha, beta)
        beta ← min(beta, value)

        IF value < bestValue THEN
            bestValue ← value
            bestMove  ← action

        IF alpha >= beta THEN     // alpha cut-off (prune remaining branches)
            BREAK

    RETURN (bestValue, bestMove)
'''