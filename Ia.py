from random import *
class Ia:

    def __init__(self, difficulty, player):
        self.difficulty = difficulty
        self.player = player
        if player is "X":
            self.enemy = "O"
        else:
            self.enemy = "X"

    def freeSpaces(self,board):
        """Searching for free spaces in the board"""
        freeCell = []
        for i, line in enumerate(board):
            for j, value in enumerate(line):
                if value is " ":
                    freeCell.append((i,j))
        return freeCell

    def nextMove(self, board):
        """Method that calculates the next move of the IA"""
        spaces = self.freeSpaces(board)
        calc = self.calculateEnemy(board)
        if len(spaces) >0:
            if calc != (-1,-1):
                return calc[0], calc[1]
            rand = randrange(0, len(spaces))
            y,x = spaces[rand]
            return y,x



    def calculateEnemy(self, board):
        """Calculate if enemy is winning and return the next movement that has to be done"""
        lineCount = [nb.count(self.enemy) for nb in board]
        column = [0,0,0]
        for i in range(0,3):
            for line in board:
                if line[i] is self.enemy:
                    column[i] += 1
        if 2 in lineCount :
            y = lineCount.index(2)
            yLine = list(board[y])
            if " " in yLine:
                x = yLine.index(" ")
                return y,x
        if 2 in column:
            index = column.index(2)
            for i, elt in enumerate(board):
                if elt[index] is " ":
                    return i,index

        diag1 = [board[0][0], board[1][1], board[2][2]]
        diag2 = [board[0][2], board[1][1], board[2][0]]
        countDiag1 = diag1.count(self.enemy)
        countDiag2 = diag2.count(self.enemy)
        if countDiag1 == 2 and " " in diag1:
            index = diag1.index(" ")
            if index==0:
                return 0,0
            elif index==1:
                return 1,1
            elif index==2:
                return 2,2
        if countDiag2 == 2 and " " in diag2:
            index = diag2.index(" ")
            if index==0:
                return 0,2
            elif index==1:
                return 1,1
            elif index==2:
                return 2,0

        return (-1,-1)
