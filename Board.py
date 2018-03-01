import turtle
from Point import Point


class Board:

            
    # Print out the points of the tour
    def printTourPoints(self):
        print(len(self.pointList))
        for point in self.pointList:
            print(point)

    # Draw the tour to screen
    def drawTour(self, knight,x,y):
        knight.speed(2)
    
        knight.penup()
        knight.goto(-224 + 64*y, 224 - 64*x)
        knight.stamp()
        knight.pendown()
        
        for i in range(1, len(self.pointList)):
            knight.goto(self.pointList[i].x, self.pointList[i].y)
            knight.stamp()

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

    def printSelf(self, knight):
        for i in range(self.row):
            for j in range (self.col):
                p = self.matrix[i][j]
                print(p)
                #knight.penup()
                knight.goto(p.x,p.y)
                knight.stamp()

  
