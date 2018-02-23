import turtle
from Point import Point

def makeSquare(board):

    for i in range(4):
        board.forward(256)
        board.left(90)

def L_shape(board):
    board.forward(512)
    board.right(90)
    board.forward(64)
    board.right(90)
    board.forward(512)
    board.left(90)
    board.forward(64)
    board.left(90)

def create_board(board):
    board.speed(0)
    board.penup()
    board.goto(-256, 256)
    board.pendown()
    for i in range(4):
        L_shape(board)
    board.forward(512)
    board.forward(-512)
    board.left(90)
    for i in range(4):
        L_shape(board)
    board.forward(512)
    board.hideturtle()

####################
##every grid is 64 * 64

if __name__ == "__main__":
    wn = turtle.Screen()
    wn.screensize(512, 512)
    print(wn.screensize())

    board = turtle.Turtle()
    create_board(board)

    knight = turtle.Turtle()
    knight.shape("circle")

    #p = Point(75,75)
    #p2 = Point(256, -256)
    #print(p.x, p.y)
    #knight.penup()
    #knight.goto(p.x,p.y)
    #knight.stamp()
    #knight.goto(p2.x,p2.y)
    #knight.stamp()

    #create and initialize a matrix of points
    Matrix = {}
    cellSize = 512 // 8
    midpoint = cellSize // 2
    for i in range (8):
        for j in range (8):
            # calculate x and y coordinates for points
            x = ((cellSize * (i + 1)) - midpoint) - 256
            y = ((cellSize * (j + 1)) - midpoint) - 256
            Matrix[i,j] = Point(x,y)

    for i in range(8):
        for j in range (8):
            p = Matrix[i,j]
            print(p)
            #knight.penup()
            knight.goto(p.x,p.y)
            knight.stamp()




    wn.exitonclick()
