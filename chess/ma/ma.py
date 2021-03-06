from chess.chess import Chess
from chess import chess
from point.point import Point
import pygame
from chess.images.imageChess import maW, maB



class Ma(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "M", white)
            self.primitiveMove= []
            for i in range (0,9,1):
                for j in range (0,10,1):
                    self.primitiveMove.append(Point(i,j))
            
        elif(white == 0):
            Chess.__init__(self, point, "m", white)
            self.primitiveMove= []
            for i in range (0,9,1):
                for j in range (0,10,1):
                    self.primitiveMove.append(Point(i,j))
            
        self.value = 270
        

    def positiveMove(self, currentBoard):
        #setUp:
        self.pMove.clear()
        # Your code:
        for m in self.primitiveMove:
            if((abs(m.x - self.point.x) == 1 and abs(m.y-self.point.y) == 2) or 
                (abs(m.x - self.point.x) == 2 and abs(m.y-self.point.y) == 1) ):
                if(not self.isTeammatePoint(m, currentBoard)):
                    if(abs(m.x - self.point.x) == 1):
                        if(not (chess.isChessPoint(Point(self.point.x,self.point.y + (m.y-self.point.y)/abs(m.y-self.point.y)  ), currentBoard))):
                            self.pMove.append(m)
                    elif (abs(m.x - self.point.x) == 2): 
                        if(not (chess.isChessPoint(Point(self.point.x + (m.x-self.point.x)/abs(m.x-self.point.x), self.point.y ), currentBoard))):
                            self.pMove.append(m)
    def clone(self):
        clone = Ma(self.point, self.white)
        clone.active = self.active
        clone.value = self.value

        return clone

    def genarateNewBoards(self, currentBoard, tP):
        boards = []
        self.positiveMove(currentBoard)
        for i in range(len(self.pMove)):
            boards.append(currentBoard.clone(tP))
            boards[i].move(self.point, self.pMove[i])
        return boards
    def imageRender(self, canvas):
        if self.active:
            if self.white:
                canvas.blit(maW, (35+self.point.x*71-maW.get_size()[0]/2, 40+self.point.y*70-maW.get_size()[1]/2))
            else:
                canvas.blit(maB, (35+self.point.x*71-maB.get_size()[0]/2, 40+self.point.y*70-maB.get_size()[1]/2))

def createMa(board):
    for i in range(2):
        for j in range(2):
            ma = Ma(Point(1+6*j, i*9), 1-i)
            board.chesses.append(ma)
            board.activeChesses.append(ma)
        




