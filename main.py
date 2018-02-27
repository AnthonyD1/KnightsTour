import turtle
from DrawBoard import create_board
from Board import Board
        
if __name__ == "__main__":
    chessBoard = Board(8,8)
    wn = turtle.Screen()
    wn.screensize(512, 512)
    board = turtle.Turtle()
    create_board(board)



    knight = turtle.Turtle()
    knight.shape("circle")

    #chessBoard.printBoard(knight)

    chessBoard.tour(0,0)
    chessBoard.printTourPoints()
    chessBoard.drawTour(knight,0,0)
    
    wn.exitonclick()
