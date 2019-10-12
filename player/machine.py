from player.player import Player , players
from random import choice
from minimaxFunction import maxFun, minFun, maxDepth
from board import board

class Machine(Player):
    def __init__(self):
        Player.__init__(self)
        self.get = 0

    def play(self, board):
        # random move:
        # randomMove(board)
        # end 
        board.chesses = minimaxMove(board).chesses
def minimaxMove(board):
    depth = 0
    topBoardNo = 0
    topScore = -100000
    boards = board.generateNewBoardBlacksTurn()
    print(len(boards))

    for i in range(len(boards)):
        if(not boards[i].isDead(1)):
            score = minFun(boards[i], depth + 1)
            if(score > topScore):
                topBoardNo = i
                topScore = score
    return boards[topBoardNo]



def createMachine():
    m = Machine()
    players.append(m)

def randomMove(board):
    while True:
        c = choice(board.chesses)
        if(not c.white):
            if(c.active):
                if(c.shape != "."):
                    break
    c.positiveMove(board)
    c.move(choice(c.pMove), board)

    

    


