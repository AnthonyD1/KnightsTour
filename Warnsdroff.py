# This is an implementation of the Warnsdroff algorithm for finding knight's tour path.
# It utilizes weights on each adjacent node and picks the smallest of the weights. It is
# a sort of greedy algorithm.

from Board import Board
from Point import Point

# check for out of bounds
def boundaryCheck(board,x,y):
    
    if (x > board.row - 1 or x < 0 or y > board.col - 1 or y < 0):
            return True
    else:
        return False
    
# Find the weight of a given point based on how many adjacent accessible points there are.
def accessibility(board,x,y):

    xCords = [1, 2, 2, 1, -1, -2, -2, -1]
    yCords = [2, 1, -1, -2, -2, -1, 1, 2]
    count = 0

    for i in range(8):
        xChange = xCords[i]
        yChange = yCords[i]
        
        # out of bounds check
        if (boundaryCheck(board, x + xChange, y + yChange) == True):
            continue
        
        # find how many open adjacent points there are
        if (board.matrix[x + xChange, y + yChange].hasBeenVisited() == False):
            count += 1

    # assign the weight to the point
    board.matrix[x, y].accessibility = count

    
# Will find the accessibility of each adjacent point
def accessibilityOfAdjacents(board, x, y):

    xCords = [1, 2, 2, 1, -1, -2, -2, -1]
    yCords = [2, 1, -1, -2, -2, -1, 1, 2]
    points = []

    for i in range(8):
        xChange = xCords[i]
        yChange = yCords[i]
        
        # out of bounds check
        if (boundaryCheck(board, x + xChange, y + yChange)):
            continue
        if (board.matrix[x + xChange, y + yChange].hasBeenVisited() == True):
            continue

        accessibility(board, x + xChange, y + yChange)
        # add the point to the list of adjacent points
        points.append(board.matrix[x + xChange, y + yChange])

    # store adjacent points in current point
    board.matrix[x, y].adjacentPoints = points


# Sorts a list of points by accessibility from largest to smallest
def sortPoints(points):
    #for point in points: print point.accessibility,
    #print
    for i in range(0, len(points) - 1):
        #print(i)
        max = points[i].accessibility
        #print(max)
        pos = 0;
        for j in range(i + 1, len(points)):
            #print(j)
            # find largest value in weights
            if(points[j].accessibility > max):
                max = points[j].accessibility
                #print(max)
                pos = j # keep track of which point is biggest
        if(max == points[i].accessibility): continue
        #print("done with max")
        #print("position: " , pos)
        #print("i: ", i)
        # move largest into position
        temp = points[i]
        points[i] = points[pos]
        points[pos] = temp
        #for point in points: print point.accessibility,
        #print

def warnsdroff(board, x, y):
    # check if all cells have been visited
    if (board.count == board.boardSize):
        return
    
    currentPoint = board.matrix[x,y]
    # this point has not been visited to toggle visited and add to path
    currentPoint.toggleVisited()
    board.pointList.append(currentPoint)
    board.count += 1
    #print(board.count)

    # find accessibility for children and sort
    accessibilityOfAdjacents(board, x, y)
    sortPoints(board.matrix[x,y].adjacentPoints)

    # recursively traverse graph by picking next point of smallest accessibility
    while (len(board.matrix[x,y].adjacentPoints) > 0):
        #print("point: " ,x,y, " has adjacent points: ")
        #for point in board.matrix[x,y].adjacentPoints:
            #print point.accessibility,
        #print
        nextPoint = board.matrix[x,y].adjacentPoints.pop()
        #print("nextPoint: " + str(nextPoint) + "weight: " + str(nextPoint.accessibility))
        # convert coordinates to  matrix indices FIX THIS SHIT
        row = (nextPoint.y - 224) // -64
        col = (nextPoint.x + 224) // 64
        #print(row, col)
        warnsdroff(board, row, col)

    # this point didn't have a path so remove it
    if (board.count < board.boardSize):
        #print("deleted")
        board.count -= 1
        #print(board.count)
        board.pointList.pop()
        currentPoint.toggleVisited()
    

    
        
if __name__ == "__main__":
    board = Board(8,8)
    x = input("select a starting row")
    y = input("select a starting column")
    #nextPoint = Point(-224, -224)
    #row = (nextPoint.x - 32 + 256) // 64
    #col = (nextPoint.y - 32 + 256) // 64
    #print(row, col)
    board.matrix[0,0].toggleVisited()
    
    accessibility(board,x,y)
    print("accessibility of this point: " + str(board.matrix[x,y].accessibility))

    accessibilityOfAdjacents(board, x, y)
    for point in board.matrix[x,y].adjacentPoints:
        #print(point)
        col = (point.x + 224 ) // 64
        row = (point.y - 224 ) // -64
        print(row, col)
        print(point.accessibility)

    sortPoints(board.matrix[x,y].adjacentPoints)

    for point in board.matrix[x,y].adjacentPoints:
        print(point)
        col = (point.x + 224 ) // 64
        row = (point.y - 224 ) // -64
        print(row, col)
        print(point.accessibility)
            
        
