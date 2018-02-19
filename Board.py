import turtle

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


                   
wn = turtle.Screen()    
board = turtle.Turtle()
create_board(board)

knight = turtle.Turtle()
knight.shape("turtle")




wn.exitonclick()
