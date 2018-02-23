import turtle
from Point import Point
from Board import create_board

if __name__ == "__main__":
    wn = turtle.Screen()
    board = turtle.Turtle()
    create_board(board)



    knight = turtle.Turtle()
    knight.shape("circle")
    p = Point(75,75)
    p2 = Point(150, 200)
    print(p.x, p.y)
    #knight.penup()
    knight.goto(p.x,p.y)
    knight.stamp()
    knight.goto(p2.x,p2.y)
    #knight.stamp()
    wn.exitonclick()

    matrix = [[0 for i in xrange(8)] for i in xrange(8)]
    cx = -224
    cy = 224
    for i in range(0,8):
        for j in range(0,8):
            cp = Point(cx, cy)
            matrix[i][j] = cp
            cx = cx + 64
        cx = -224
        cy = cy - 64

    print(matrix[7][0].x)
