import turtle
from Point import Point


class Board:

    def __init__(self, row, col):
        self.boardSize = row * col
        self.row = row
        self.col = col
        self.pointList = []
        self.count = 0
        self.matrix = {}
        cx = -224
        cy = 224
        for i in range(row):
            for j in range(col):
                cp = Point(cx, cy)
                self.matrix[i,j] = cp
                cx = cx + 64
            cx = -224
            cy = cy - 64

    def printBoard(self, knight):
        for i in range(self.row):
            for j in range (self.col):
                p = self.matrix[i][j]
                print(p)
                #knight.penup()
                knight.goto(p.x,p.y)
                knight.stamp()

  
