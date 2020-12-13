"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

# print([EMPTY, X, X].count("X"))

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
    num_x = 0
    num_o = 0
    for row in board:
        num_x += row.count("X")
        num_o += row.count("O")
    if num_x > num_o:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avail_values = set()
    for i in range(len(board)):
        for j in range(len(i)):
            if board[i][j] == None:
                avail_values.update((i,j))
    return avail_values


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i, j = action
    if new_board[i][j] != None:
        raise Exception("Sorry, that box is already filled")
    else:
        move = player(new_board)
        new_board[i][j] = move
        return new_board


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
