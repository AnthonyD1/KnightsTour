import turtle
from DrawBoard import create_board
from Board import Board
import DFS
        
if __name__ == "__main__":
    chessBoard = Board(8,8)
    wn = turtle.Screen()
    wn.screensize(512, 512)
    board = turtle.Turtle()
    create_board(board)



    knight = turtle.Turtle()
    knight.shape("circle")

    #chessBoard.printBoard(knight)

    DFS.tour(chessBoard,0,0)
    DFS.printTourPoints(chessBoard)
    DFS.drawTour(chessBoard,knight,0,0)
    
    wn.exitonclick()
