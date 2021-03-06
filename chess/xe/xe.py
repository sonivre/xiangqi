from chess.chess import Chess
from chess import chess
from point.point import Point
import pygame
from chess.images.imageChess import xeW, xeB



class Xe(Chess):
    def __init__(self, point, white):
        if(white == 1):
            Chess.__init__(self, point, "X", white)

        elif(white == 0):
            Chess.__init__(self, point, "x", white)
        self.primitiveMove = []
        for i in range(9):
            for j in range(10):
                self.primitiveMove.append(Point(i,j))
        self.value = 600
    def positiveMove(self, currentBoard):
        # setUp:
        self.pMove.clear()
        # Your code:
        for i in range(self.point.x+1, 9, 1):
            tPoint =  Point(i, self.point.y)
            if(not chess.isChessPoint(tPoint, currentBoard)):
                self.pMove.append(tPoint)
            else:
                if(self.isTeammatePoint(tPoint, currentBoard)):
                    break
                else:
                    self.pMove.append(tPoint)
                    break
        for i in range(self.point.x-1, -1, -1):
            tPoint =  Point(i, self.point.y)
            if(not chess.isChessPoint(tPoint, currentBoard)):
                self.pMove.append(tPoint)
            else:
                if(self.isTeammatePoint(tPoint, currentBoard)):
                    break
                else:
                    self.pMove.append(tPoint)
                    break
        for i in range(self.point.y+1, 10, 1):
            tPoint =  Point(self.point.x, i)
            if(not chess.isChessPoint(tPoint, currentBoard)):
                self.pMove.append(tPoint)
            else:
                if(self.isTeammatePoint(tPoint, currentBoard)):
                    break
                else:
                    self.pMove.append(tPoint)
                    break
        for i in range(self.point.y-1, -1, -1):
            tPoint =  Point(self.point.x, i)
            if(not chess.isChessPoint(tPoint, currentBoard)):
                self.pMove.append(tPoint)
            else:
                if(self.isTeammatePoint(tPoint, currentBoard)):
                    break
                else:
                    self.pMove.append(tPoint)
                    break
    def clone(self):
        clone = Xe(self.point, self.white)
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
                canvas.blit(xeW, (35+self.point.x*71-xeW.get_size()[0]/2, 40+self.point.y*70-xeW.get_size()[1]/2))
            else:
                canvas.blit(xeB, (35+self.point.x*71-xeB.get_size()[0]/2, 40+self.point.y*70-xeB.get_size()[1]/2))





def createXe(board):
    for i in range(2):
        for j in range(2):
            xe = Xe(Point(j*8, i*9), 1-i)
            board.chesses.append(xe)
            board.activeChesses.append(xe)
        