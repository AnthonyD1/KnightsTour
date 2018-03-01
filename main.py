import turtle
from DrawBoard import create_board
from Board import Board
import DFS
import Warnsdroff
        
if __name__ == "__main__":
    # create the chessboard with specifiec dimensions
    chessBoard = Board(8,8)

    # starting point
    row = input("select a starting row: ")
    col = input("select a starting column: ")
    
    # create the board for display using turtle
    wn = turtle.Screen()
    wn.screensize(512, 512)
    board = turtle.Turtle()
    create_board(board)

    # set the shape of the drawing tool
    knight = turtle.Turtle()
    knight.shape("circle")

    #chessBoard.printBoard(knight)

    # run the path finding algorithm and draw the board

    #DFS.tour(chessBoard,row,col)
    Warnsdroff.warnsdroff(chessBoard,row, col)
    #chessBoard.printTourPoints()
    chessBoard.drawTour(knight,row,col)
    
    wn.exitonclick()
