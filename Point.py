class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False

    # Returns the x-coordinate
    def getXCoord(self):
        return self.x
    # Returns the y-coordinate
    def getYCoord(self):
        return self.y
    # Change whether a point has been visited or not
    def toggleVisited(self):
        self.visited = not(self.visited)

    # Have we visited the point or naw
    def hasBeenVisited(self):
        return self.visited
