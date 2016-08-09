import TTTException as Exception
import Stack as S


class TicTacToe:
    def __init__(self):
        self.board = [(' ',' ',' '),(' ',' ',' '),(' ',' ',' ')]
        self.play = 1
        self.stack = S.Stack()
        self.stack.push("O")
        self.winner = ""



    def printBoard(self):
        """This method prints the gameboard"""
        string = ""
        for elt in self.board:
            string += "\n"
            for case in elt:
                string += case
        print(string)

    def placeSymbol(self,posY, posX, player):
        """Places a Symbol on the gameboard depending by player and position"""
        """posX and posY are referenced to the board as carthesian values"""
        print((posY,posX))
        if posY > 2 or posX > 2 or posX < 0 or posY < 0:
            raise Exception.TTTException(4)
        if type(posX) is not int or type(posY) is not int:
            raise Exception.TTTException(5)
        if self.board[posY][posX] is ' ' and self.play == 1 and self.stack.canInsert(player) is True:
            self.stack.pop()
            li = list(self.board[posY])
            li[posX] = player
            self.board[posY] = li
            self.stack.push(player)
            self.win(posY, posX, player)
            self.printBoard()
            print(self.stack.getStack())
        elif self.play == 0:
            raise Exception.TTTException(2)
        elif self.board[posY][posX] is not ' ':
            raise Exception.TTTException(1)
        else:
            raise Exception.TTTException(3)

    def win(self, posY, posX, player):
        """Verify if a player won the game"""
        line = self.board[posY]
        column = [nb[posX] for nb in self.board].count(player)
        if line.count(player) == 3 or column == 3: #Verifying Lines or Columns
            self.play = 0
            self.winner = player
            print (self.winner.upper() + " hai vinto!")
            return True
        elif (posX == posY) or (abs(posX-posY) == 2): #Verifying Diagonals
            firstDiag = [nb[i] for i,nb in enumerate(self.board)]
            secondDiag = [nb[2-i] for i,nb in enumerate(self.board)]
            if firstDiag.count(player) == 3 or secondDiag.count(player) == 3:
                self.play = 0
                self.winner = player
                print (self.winner.upper() + " hai vinto!")
                return True
        return False

    def getPlay(self):
        """Return 1 if the game is still running else 0 if the game ended"""
        return self.play

    def getTurn(self):
        """Return the value of player who has to play the next turn"""
        actual = self.stack.top()
        if actual == "O":
            return "X"
        return "O"

    def getBoard(self):
        """Return the main board"""
        return self.board
