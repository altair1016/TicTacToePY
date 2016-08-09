from tkinter import *
import TicTacToe as TTT
import time
import sys
import Ia
from TTTException import *
game = TTT.TicTacToe()
playerIa = Ia.Ia(1, "O")

root=Tk()
width=700
background = 'white'
w = Canvas(root, width=width,height=width, background=background)
dimGrid = (width)/3
clickedX=-1
clickedY=-1

def drawCircle(clickedX, clickedY):
    positionX = -1
    positionY = -1
    if clickedX > -1 and clickedY > -1:
        if clickedX in range(0,int(dimGrid)) and clickedY in range(0,int(dimGrid)):
            #case 0,1
            w.create_oval(int(dimGrid/3), int(dimGrid/3), int((dimGrid/3)*2), int((dimGrid/3)*2))
            print("Disegno")
            root.update()
            return 0,0
        elif clickedX in range(int(dimGrid), int((dimGrid)*2)) and clickedY in range(0,int(dimGrid)):
            #case 0,1
            w.create_oval(int((dimGrid/3)*4), int(dimGrid/3), int((dimGrid/3)*5), int((dimGrid/3)*2))
            print("Disegno")
            root.update()
            return 0,1
        elif clickedX in range(int((dimGrid)*2), width-5) and clickedY in range(0,int(dimGrid)):
            #case 0,2
            w.create_oval(int((dimGrid/3)*7), int(dimGrid/3), int((dimGrid/3)*8), int((dimGrid/3)*2))
            print("Disegno")
            root.update()
            return 0,2
        elif clickedX in range(0,int((dimGrid))) and clickedY in range(int(dimGrid),int((dimGrid)*2)):
            #case 1,0
            w.create_oval(int(dimGrid/3), int((dimGrid/3)*4), int((dimGrid/3)*2), int((dimGrid/3)*5))
            print("Disegno")
            root.update()
            return 1,0
        elif clickedX in range(int((dimGrid)), int((dimGrid)*2)) and clickedY in range(int(dimGrid),int((dimGrid)*2)):
            #case 1,1
            w.create_oval(int((dimGrid/3)*4), int((dimGrid/3)*4), int((dimGrid/3)*5), int((dimGrid/3)*5))
            print("Disegno")
            root.update()
            return 1,1
        elif clickedX in range(int((dimGrid)*2), int((dimGrid)*3)) and clickedY in range(int(dimGrid),int((dimGrid)*2)):
            #case 1,2
            w.create_oval(int((dimGrid/3)*7), int((dimGrid/3)*4), int((dimGrid/3)*8), int((dimGrid/3)*5))
            print("Disegno")
            root.update()
            return 1,2
        elif clickedX in range(0,int((dimGrid))) and clickedY in range(int((dimGrid)*2),int((dimGrid)*3)):
            #case 2,0
            w.create_oval(int(dimGrid/3), int((dimGrid/3)*7), int((dimGrid/3)*2), int((dimGrid/3)*8))
            print("Disegno")
            root.update()
            return 2,0
        elif clickedX in range(int((dimGrid)), int((dimGrid)*2)) and clickedY in range(int((dimGrid)*2),int((dimGrid)*3)):
            #casse 2,1
            w.create_oval(int((dimGrid/3)*4), int((dimGrid/3)*7), int((dimGrid/3)*5), int((dimGrid/3)*8))
            print("Disegno")
            root.update()
            return 2,1
        elif clickedX in range(int((dimGrid)*2), int((dimGrid)*3)) and clickedY in range(int((dimGrid)*2),int((dimGrid)*3)):
            #case 2,2
            w.create_oval(int((dimGrid/3)*7), int((dimGrid/3)*7), int((dimGrid/3)*8), int((dimGrid/3)*8))
            print("Disegno")
            root.update()
            return 2,2

def drawEcs(clickedX, clickedY):
    positionX = -1
    positionY = -1
    if clickedX > -1 and clickedY > -1:
        if clickedX in range(0,int(dimGrid)) and clickedY in range(0,int(dimGrid)):
            #case 0,1
            w.create_line(int(dimGrid/3), int(dimGrid/3), int((dimGrid/3)*2), int((dimGrid/3)*2))
            w.create_line(int((dimGrid/3)*2), int(dimGrid/3),int(dimGrid/3) , int((dimGrid/3)*2))
            print("Disegno")
            root.update()
            return 0,0
        elif clickedX in range(int(dimGrid), int((dimGrid)*2)) and clickedY in range(0,int(dimGrid)):
            #case 0,1
            w.create_line(int((dimGrid/3)*4), int(dimGrid/3), int((dimGrid/3)*5), int((dimGrid/3)*2))
            w.create_line(int((dimGrid/3)*5), int(dimGrid/3), int((dimGrid/3)*4), int((dimGrid/3)*2))
            print("Disegno")
            root.update()
            return 0,1
        elif clickedX in range(int((dimGrid)*2), width-5) and clickedY in range(0,int(dimGrid)):
            #case 0,2
            w.create_line(int((dimGrid/3)*7), int(dimGrid/3), int((dimGrid/3)*8), int((dimGrid/3)*2))
            w.create_line(int((dimGrid/3)*8), int(dimGrid/3), int((dimGrid/3)*7), int((dimGrid/3)*2))
            print("Disegno")
            root.update()
            return 0,2
        elif clickedX in range(0,int((dimGrid))) and clickedY in range(int(dimGrid),int((dimGrid)*2)):
            #case 1,0
            w.create_line(int(dimGrid/3), int((dimGrid/3)*4), int((dimGrid/3)*2), int((dimGrid/3)*5))
            w.create_line(int((dimGrid/3)*2), int((dimGrid/3)*4), int(dimGrid/3), int((dimGrid/3)*5))
            print("Disegno")
            root.update()
            return 1,0
        elif clickedX in range(int((dimGrid)), int((dimGrid)*2)) and clickedY in range(int(dimGrid),int((dimGrid)*2)):
            #case 1,1
            w.create_line(int((dimGrid/3)*4), int((dimGrid/3)*4), int((dimGrid/3)*5), int((dimGrid/3)*5))
            w.create_line(int((dimGrid/3)*5), int((dimGrid/3)*4), int((dimGrid/3)*4), int((dimGrid/3)*5))
            print("Disegno")
            root.update()
            return 1,1
        elif clickedX in range(int((dimGrid)*2), int((dimGrid)*3)) and clickedY in range(int(dimGrid),int((dimGrid)*2)):
            #case 1,2
            w.create_line(int((dimGrid/3)*7), int((dimGrid/3)*4), int((dimGrid/3)*8), int((dimGrid/3)*5))
            w.create_line(int((dimGrid/3)*8), int((dimGrid/3)*4), int((dimGrid/3)*7), int((dimGrid/3)*5))
            print("Disegno")
            root.update()
            return 1,2
        elif clickedX in range(0,int((dimGrid))) and clickedY in range(int((dimGrid)*2),int((dimGrid)*3)):
            #case 2,0
            w.create_line(int(dimGrid/3), int((dimGrid/3)*7), int((dimGrid/3)*2), int((dimGrid/3)*8))
            w.create_line(int((dimGrid/3)*2), int((dimGrid/3)*7), int(dimGrid/3), int((dimGrid/3)*8))
            print("Disegno")
            root.update()
            return 2,0
        elif clickedX in range(int((dimGrid)), int((dimGrid)*2)) and clickedY in range(int((dimGrid)*2),int((dimGrid)*3)):
            #casse 2,1
            w.create_line(int((dimGrid/3)*4), int((dimGrid/3)*7), int((dimGrid/3)*5), int((dimGrid/3)*8))
            w.create_line(int((dimGrid/3)*5), int((dimGrid/3)*7), int((dimGrid/3)*4), int((dimGrid/3)*8))
            print("Disegno")
            root.update()
            return 2,1
        elif clickedX in range(int((dimGrid)*2), int((dimGrid)*3)) and clickedY in range(int((dimGrid)*2),int((dimGrid)*3)):
            #case 2,2
            w.create_line(int((dimGrid/3)*7), int((dimGrid/3)*7), int((dimGrid/3)*8), int((dimGrid/3)*8))
            w.create_line(int((dimGrid/3)*8), int((dimGrid/3)*7), int((dimGrid/3)*7), int((dimGrid/3)*8))
            print("Disegno")
            root.update()
            return 2,2


def drawGrid():
    w.create_line(0,dimGrid,width,dimGrid)
    w.create_line(0,dimGrid*2,width,dimGrid*2)
    w.create_line(dimGrid,0,dimGrid,width)
    w.create_line(dimGrid*2,0,dimGrid*2,width)


def callback(event):

    player = game.getTurn()
    print("E il turno di " + player)

    try:
        if player == "X":
            x,y = drawEcs(event.x, event.y)
        else:
            x,y = drawCircle(event.x, event.y)
        posY = int(y)
        posX = int(x)
        game.placeSymbol(posX,posY, player)
        player = game.getTurn()
        time.sleep(0.3)
        IA_y,IA_x = playerIa.nextMove(game.board)
        game.placeSymbol(IA_y,IA_x,"O")
        graph_x = -1
        graph_y = -1
        if (IA_y,IA_x) == (0,0):
            graph_x, graph_y = int(dimGrid/3), int(dimGrid/3)
        elif (IA_y,IA_x) == (0,1):
            graph_x,graph_y = int((dimGrid/3)*4), int(dimGrid/3)
        elif (IA_y,IA_x) == (0,2):
            graph_x,graph_y = int((dimGrid/3)*7), int(dimGrid/3)
        elif (IA_y,IA_x) == (1,0):
            graph_x,graph_y = int((dimGrid/3)), int((dimGrid/3)*4)
        elif (IA_y,IA_x) == (1,1):
            graph_x,graph_y = int((dimGrid/3)*4), int((dimGrid/3)*4)
        elif (IA_y,IA_x) == (1,2):
            graph_x,graph_y = int((dimGrid/3)*7), int((dimGrid/3)*4)
        elif (IA_y,IA_x) == (2,0):
            graph_x,graph_y = int((dimGrid/3)), int((dimGrid/3)*7)
        elif (IA_y,IA_x) == (2,1):
            graph_x,graph_y = int((dimGrid/3)*4), int((dimGrid/3)*7)
        elif (IA_y,IA_x) == (2,2):
            graph_x,graph_y = int((dimGrid/3)*7), int((dimGrid/3)*7)
        if player == "X":
            x,y = drawEcs(graph_x, graph_y)
        else:
            x,y = drawCircle(graph_x, graph_y)

        w = Message(root, text="this is a message")
        root.update()
    except TTTException:
        print(sys.exc_info()[1])
        #except ValueError:
            #print("Solo Valori numerici")

    print ("Clicked at:", event.x, event.y)


drawGrid()
w.bind("<Button-1>", callback)
w.pack()
root.mainloop()
