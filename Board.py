import turtle
from Point import Point


class Board:

    def tour(self,x,y):
    
        # check for out of bounds
        if (x > self.row - 1 or x < 0 or y > self.col - 1 or y < 0):
            return
        # check if all cells been visited
        if (self.count == self.boardSize):
            return
        currentPoint = self.matrix[x,y]
        # has the point been visited?
        if (currentPoint.hasBeenVisited()):
            return

        # otherwise this point has not been visited, toggle visited
        currentPoint.toggleVisited()
        self.pointList.append(currentPoint)
        self.count += 1
        #print(self.count)
        #print("added")
        #k.goto(self.matrix[x][y].x, self.matrix[x][y].y)
        #k.stamp()

        #recursively look at adjacent knight moves
        self.tour(x + 1, y + 2)
        self.tour(x + 2, y + 1)
        self.tour(x + 2, y - 1)
        self.tour(x + 1, y - 2)
        self.tour(x - 1, y - 2)
        self.tour(x - 2, y - 1)
        self.tour(x - 2, y + 1)
        self.tour(x - 1, y + 2)

        #self.tour(x + 2, y + 1)
        #self.tour(x + 2, y - 1)
        #self.tour(x + 1, y + 2)
        #self.tour(x + 1, y - 2)
        #self.tour(x - 1, y + 2)
        #self.tour(x - 1, y - 2)
        #self.tour(x - 2, y + 1)
        #self.tour(x - 2, y - 1)
        
        # this point didn't have a path so remove it
        if (self.count < self.boardSize):
            #print("deleted")
            self.count -= 1
            self.pointList.pop()
            currentPoint.toggleVisited()

    # Print out the points of the tour
    def printTourPoints(self):
        print(len(self.pointList))
        for point in self.pointList:
            print(point)

    # Draw the tour to screen
    def drawTour(self, knight,x,y):
        knight.speed(3)
        
        knight.penup()
        knight.goto(-224 + 64*x, 224 - 64*y)
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

    def printBoard(self, knight):
        for i in range(self.row):
            for j in range (self.col):
                p = self.matrix[i][j]
                print(p)
                #knight.penup()
                knight.goto(p.x,p.y)
                knight.stamp()

  
