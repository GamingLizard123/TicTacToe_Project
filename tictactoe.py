"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None
maxDepth = 6

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
    num_ofX= 0
    num_ofO=0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                num_ofX += 1
            elif board[i][j]==O:
                num_ofO += 1

    if num_ofX > num_ofO:
        return O
    else:
        return X
    
    #raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #initialized set
    actionsSet = set()

    #checks if the board is in end state
    if terminal(board):
        return None
    
    #checks if cells are empty
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY: #if cell is empty
                actionsSet.add((i,j)) #add location to possible actions
    
    #returns the set
    return actionsSet

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #makes copy of board
    
    boardCopy = copy.deepcopy(board)
    
    
    
    #checks if the current action is withing the possible actions
    
    
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Action not available")

    #replaces the location of action with the player that is currently playing
    boardCopy[action[0]][action[1]] = player(boardCopy)
    returnBoard = boardCopy
    boardCopy = board
    return returnBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    num_ofX = 0
    num_ofO = 0
    #check if game has been won Horizontally
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == O:
                num_ofO += 1
            elif board[i][j]==X:
                num_ofX += 1
        if num_ofO == 3:
            return O
        elif num_ofX == 3:
            return X
        else:
            num_ofX = 0
            num_ofO = 0

    #check if the game was won vertically
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] == O:
                num_ofO += 1
            elif board[j][i]==X:
                num_ofX += 1
        if num_ofO == 3:
            return O
        elif num_ofX == 3:
            return X
        else:
            num_ofX = 0
            num_ofO = 0

    #checks diagonal from top left to bottom right
    for i in range(len(board)):
        if board[i][i] == O:
            num_ofO += 1
        elif board[i][i] == X:
            num_ofX += 1
    if num_ofX == 3:
        return X
    elif num_ofO == 3:
        return O
    else:
        num_ofO = 0
        num_ofX = 0

    #checks diagonal from top right to bottom left
    for i in range(len(board)):
        if board[i][2-i] == O:
            num_ofO += 1
        elif board[i][2-i] == X:
            num_ofX += 1
    if num_ofX == 3:
        return X
    elif num_ofO == 3:
        return O
    else:
        num_ofO = 0
        num_ofX = 0

    return None
    raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #checks if all slots in the board are taken
    EmptySlots = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                EmptySlots += 1
    
    #gets winner
    win = winner(board)
    
    #if there is a winner the game is over
    if win != None:
        return True
    #if there are no more empty slots the game is over
    elif EmptySlots == 0:
        return True
    #otherwise it isn't over
    else: return False
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else: return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == O:
        move = maximize(board, maxDepth,0, 0, False)
        return move
    else:
        move = maximize(board, maxDepth,0, 0, True)
        return move
    

def maximize(board, depth, alpha, beta, maximizingPlayer):
    #Returns the evaluated expression if it is terminal board or end board
    if depth <= 0 or terminal(board) == True:  
        return utility(board)

    maxaction = tuple()
    minaction = tuple()
    if maximizingPlayer:
        maxEval = -math.inf
        children = actions(board)
        #evaluate each child
        for child in children:
            eval = maximize(result(board, child), depth-1,alpha,beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)


            if beta > alpha and depth != maxDepth:

                break
            #if the depth is shallow return the move rather than the eval
            if depth == maxDepth and eval == alpha:

                maxaction = child
        #if depth is shallow then return action
        if depth==maxDepth:
            if maxaction != ():    
                return maxaction
            else:
                actions1 = actions(board)
                action1 = actions1.pop()
                return action1
        return alpha
    else:
        minEval = math.inf
        children = actions(board)
        for child in children:
            eval = maximize(result(board, child), depth-1,alpha,beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)

            
            if beta > alpha and depth != maxDepth:
                break
                
            if depth == maxDepth and eval == beta:
                minaction = child
                
        if depth == maxDepth:
            if minaction != ():
                return minaction
            else:
                actions1 = actions(board)
                action1 = actions1.pop()
                return action1

        return beta