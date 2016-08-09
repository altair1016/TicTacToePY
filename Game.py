import TicTacToe as TTT
import time
import sys
import Ia
from TTTException import *
game = TTT.TicTacToe()
playerIa = Ia.Ia(1, "O")
while game.getPlay() != 0:
    player = game.getTurn()
    print("E il turno di " + player)
    try:
        val = input("Dammi le coordinate Riga,Colonna: ")
        posY,posX = val.split(",")
        posY = int(posY)
        posX = int(posX)
        game.placeSymbol(posY,posX, player)
        time.sleep(0.3)
        y,x = playerIa.nextMove(game.board)
        game.placeSymbol(y,x,"O")


    except TTTException:
        print(sys.exc_info()[1])
    #except ValueError:
        #print("Solo Valori numerici")
