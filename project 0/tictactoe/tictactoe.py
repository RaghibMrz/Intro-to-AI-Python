"""
Tic Tac Toe Player
"""

import math

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

    if terminal(board):
        return EMPTY
    xCount = 0
    oCount = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xCount += 1
            if board[i][j] == O:
                oCount += 1

    if xCount == oCount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board):
        return EMPTY

    actionList = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actionList.append((i, j))

    return set(actionList)


def deepCopyBoard(board):
    newBoard = []
    for row in board:
        newRow = []
        for col in row:
            newRow.append(col)
        newBoard.append(newRow)
    return newBoard


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception

    copyBoard = deepCopyBoard(board)
    copyBoard[action[0]][action[1]] = player(board)
    return copyBoard


def checkRow(board):
    for i in range(len(board)):
        xNum = 0
        oNum = 0
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                continue
            if board[i][j] == X:
                xNum += 1
            if board[i][j] == O:
                # print(i, j)
                oNum += 1
        if xNum == 3:
            return X
        if oNum == 3:
            return O
    return None


def checkCol(board):
    for i in range(len(board)):
        xNum = 0
        oNum = 0
        for j in range(len(board[i])):
            if board[j][i] == EMPTY:
                continue
            if board[j][i] == X:
                xNum += 1
            if board[j][i] == O:
                oNum += 1
        if xNum == 3:
            return X
        if oNum == 3:
            return O
    return None


def checkDiag(board, dir):
    xNum = 0
    oNum = 0
    for i in range(3):
        if dir == -1:
            j = 2 - i
        else:
            j = i
        if board[i][j] == X:
            xNum += 1
        if board[i][j] == O:
            oNum += 1
    if xNum == 3:
        return X
    if oNum == 3:
        return O
    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x = checkRow(board)
    if x is not None:
        return x
    y = checkCol(board)
    if y is not None:
        return y

    w = checkDiag(board, 0)
    if w is not None:
        return w

    z = checkDiag(board, -1)
    if z is not None:
        return z
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    mtCount = 0
    for row in board:
        for col in row:
            if col == EMPTY:
                mtCount += 1

    if winner(board) is not None or mtCount == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def maxVal(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, minVal(result(board, action), alpha, beta))
        alpha = max(v, alpha)
        if alpha >= beta:
            break
    return v


def minVal(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxVal(result(board, action), alpha, beta))
        beta = min(v, beta)
        if alpha >= beta:
            break
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    currPlayer = player(board)
    if currPlayer == X:
        maxReq = True
    else:
        maxReq = False

    actionsList = actions(board)
    currBest = -math.inf
    currWorst = math.inf
    bestMove = 1, 1

    for action in actionsList:
        r = result(board, action)
        if maxReq:
            mV = minVal(r, currBest, currWorst)
            if mV > currBest:
                currBest = mV
                bestMove = action
        else:
            mV = maxVal(r, currBest, currWorst)
            if mV < currWorst:
                currWorst = mV
                bestMove = action
    return bestMove


# arr = [[X, O, X],
#        [O, X, O],
#        [X, O, EMPTY]]
#
# print(check(arr, -1))
# print(checkDiag(arr, 1))
# print(checkDiag(arr, -1))

