
def minFunBlack(board, depth, alpha, beta, maxDepth, turn):
    lowestScore = 100000
    if(depth >= maxDepth):
        board.setScore()
        return board.score 
    boards = board.generateNewBoardWhitesTurn(turn)
    for i in range(len(boards)):
        if(not (boards[i]).isDead(0)):
            score = maxFunBlack(boards[i], depth + 1, alpha, beta, maxDepth, turn)
            if(score < lowestScore):
                lowestScore = score
            if(score < alpha):
                return lowestScore
            if(score < beta):
                beta = score
    return lowestScore
def maxFunBlack(board, depth, alpha, beta, maxDepth, turn):
    topScore = -100000
    if(depth >= maxDepth):
        board.setScore()
        return board.score 
    boards = board.generateNewBoardBlacksTurn(turn)
    for i in range(len(boards)):
        if(not boards[i].kingOverlap()):
            score = minFunBlack(boards[i], depth + 1, alpha, beta, maxDepth, turn)
            if(score > topScore):
                topScore = score
            if(score > beta):
                return topScore
            if(score > alpha):
                alpha = score
    return topScore

def minFunWhite(board, depth, alpha, beta, maxDepth, turn):
    lowestScore = 100000
    if(depth >= maxDepth):
        board.setScore()
        return board.score 
    boards = board.generateNewBoardWhitesTurn(turn)
    for i in range(len(boards)):
        if(not boards[i].kingOverlap()):
            score = maxFunWhite(boards[i], depth + 1, alpha, beta, maxDepth, turn)
            if(score < lowestScore):
                lowestScore = score
            if(score < alpha):
                return lowestScore
            if(score < beta):
                beta = score
    return lowestScore
def maxFunWhite(board, depth, alpha, beta, maxDepth, turn):
    topScore = -100000
    if(depth >= maxDepth):
        board.setScore()
        return board.score 
    boards = board.generateNewBoardBlacksTurn(turn)
    for i in range(len(boards)):
        if(not (boards[i]).isDead(1)):
            score = minFunWhite(boards[i], depth + 1, alpha, beta, maxDepth, turn)
            if(score > topScore):
                topScore = score
            if(score > beta):
                return topScore
            if(score > alpha):
                alpha = score
    return topScore



    
