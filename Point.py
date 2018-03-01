class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.accessibility = 0
        self.adjacentPoints = []
 

    # Will determine how points are printed
    def __str__(self):
        return "Point(%s,%s)"%(self.x,self.y)
    
    # Change whether a point has been visited or not
    def toggleVisited(self):
        self.visited = not(self.visited)

    # Have we visited the point or naw
    def hasBeenVisited(self):
        return self.visited
