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
        for j in range(len(board[i])):
            if board[i][j] == None:
                avail_values.add((i,j))
    return avail_values


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i, j = action
    if new_board[i][j] != None:
        raise Exception("Sorry, the move is invalid")
    else:
        move = player(board)
        new_board[i][j] = move
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if vertical(board) != None:
        return vertical(board)
    if horizontal(board) != None:
        return horizontal(board)
    if diagonal(board) != None:
        return diagonal(board)



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # when there is no more EMPTY -> game over (return True)
    # when there is a winner -> game over (return True)
    if winner(board) != None or len(actions(board)) == 0:
        return True
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_dict = {"X": 1, "O": -1}
    if (terminal(board)):
        if winner(board) == None:
            return 0
        else:
            return winner_dict[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return None
    if player(board) == "X":
        value = -math.inf
        for action in actions(board):
            max_v = min_value(result(board, action))
            if max_v > value:
                value = max_v
                best_action = action
    elif player(board) == "O":
        value = math.inf
        for action in actions(board):
            min_v = max_value(result(board, action))
            if min_v < value:
                value = min_v
                best_action = action
    return best_action


def vertical(board):
    #initialise the column count and the check set
    column = 0
    check = set()
    
    #go through each column
    while column < len(board[0]):
        
        #go through each row
        for i in range(len(board)):
            
            #if the cell contains empty space, move onto the next column immediately and re-initialise the check set
            if board[i][column] == None:
                check = set()
                break
                
            #else add the cell value into the check set
            check.update(board[i][column])
        
        #return the value if the set only contains 1 value (either X or O) -> means that there is a column winner
        if len(check) == 1:
            return check.pop()
        
        #else, check the next column
        column += 1
            

def horizontal(board):
    for i in range(len(board)):
        if board[i].count("X") == 3 or board[i].count("O") == 3:
            return board[i][0]
       

def diagonal(board):
    #initialise the left to right diagonal set and right to left diagonal set
    left_to_right = set()
    right_to_left = set()
    
    #store the values in sets for left to right diagonal and right to left diagonal
    #if value is None, re-initialise the respective set and break the loop
    for i in range(len(board)):
        if board[i][i] == None:
            left_to_right = set()
            break
        left_to_right.update(board[i][i])
    for j in range(len(board)):
        if board[j][len(board[j])-(j+1)] == None:
            right_to_left = set()
            break
        right_to_left.update(board[j][len(board[j])-(j+1)])
        
    #if length of set is 1, return value in set
    #else, return None
    if len(left_to_right) == 1:
        return left_to_right.pop()
    if len(right_to_left) == 1:
        return right_to_left.pop()

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
