from chess.chess import Chess
from chess import chess
from point.point import Point
import math
import pygame
from chess.images.imageChess import tuongW, tuongB




class Tuong(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "E", white)
            self.primitiveMove= []
            for i in range (0,9,1):
                for j in range (0,5,1):
                    self.primitiveMove.append(Point(i,j))
            
        elif(white == 0):
            Chess.__init__(self, point, "e", white)
            self.primitiveMove= []
            for i in range (0,9,1):
                for j in range (5,10,1):
                    self.primitiveMove.append(Point(i,j))
            
        self.value = 120
        
            
    def positiveMove(self, currentBoard):
        #setUp:
        self.pMove.clear()
        # Your code:
        for m in self.primitiveMove:
            if(abs(m.x - self.point.x) == 2 and abs(m.y-self.point.y) == 2):
                if(not self.isTeammatePoint(m, currentBoard)):
                    if(not (chess.isChessPoint(self.point+(m-self.point)*(1/2), currentBoard))):
                        self.pMove.append(m)
                        
    def clone(self):
        clone = Tuong(self.point, self.white)
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
                canvas.blit(tuongW, (35+self.point.x*71-tuongW.get_size()[0]/2, 40+self.point.y*70-tuongW.get_size()[1]/2))
            else:
                canvas.blit(tuongB, (35+self.point.x*71-tuongB.get_size()[0]/2, 40+self.point.y*70-tuongB.get_size()[1]/2))






def createTuong(board):
    for i in range(2):
        for j in range(2):
            tuong = Tuong(Point(2+4*j, i*9), 1-i)
            board.chesses.append(tuong)
            board.activeChesses.append(tuong)
           



