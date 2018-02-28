# This naive implementation makes use of Depth First Search. It runs in a few seconds for 6x6
# boards and under 2 minutes for 8x8 board. However, these are not adequate execution times, so
# a more efficient algorithm should be implemented.

from Board import Board

def tour(board,x,y):
    
    # check for out of bounds
    if (x > board.row - 1 or x < 0 or y > board.col - 1 or y < 0):
            return
    # check if all cells been visited
    if (board.count == board.boardSize):
        return
    currentPoint = board.matrix[x,y]
    # has the point been visited?
    if (currentPoint.hasBeenVisited()):
        return

    # otherwise this point has not been visited, toggle visited
    currentPoint.toggleVisited()
    board.pointList.append(currentPoint)
    board.count += 1
    #print(board.count)
    #print("added")
    #k.goto(board.matrix[x][y].x, board.matrix[x][y].y)
    #k.stamp()
    
    #recursively look at adjacent knight moves
    tour(board,x + 1, y + 2)
    tour(board,x + 2, y + 1)
    tour(board,x + 2, y - 1)
    tour(board,x + 1, y - 2)
    tour(board,x - 1, y - 2)
    tour(board,x - 2, y - 1)
    tour(board,x - 2, y + 1)
    tour(board,x - 1, y + 2)
    
    #board.tour(x + 2, y + 1)
    #board.tour(x + 2, y - 1)
    #board.tour(x + 1, y + 2)
    #board.tour(x + 1, y - 2)
    #board.tour(x - 1, y + 2)
    #board.tour(x - 1, y - 2)
    #board.tour(x - 2, y + 1)
    #board.tour(x - 2, y - 1)
        
    # this point didn't have a path so remove it
    if (board.count < board.boardSize):
        #print("deleted")
        board.count -= 1
        board.pointList.pop()
        currentPoint.toggleVisited()
        
# Print out the points of the tour
def printTourPoints(board):
    print(len(board.pointList))
    for point in board.pointList:
        print(point)

    # Draw the tour to screen
def drawTour(board, knight,x,y):
    knight.speed(3)
    
    knight.penup()
    knight.goto(-224 + 64*x, 224 - 64*y)
    knight.stamp()
    knight.pendown()
        
    for i in range(1, len(board.pointList)):
        knight.goto(board.pointList[i].x, board.pointList[i].y)
        knight.stamp()
