import random

class Board:
    boardList = [["-","-","-"],["-","-","-"],["-","-","-"]]
    
    def display(self):
        for i in range(3):
            for j in range(3):
                print(Board.boardList[i][j], end=" ")
            print()  
        print("---------------------------------")    

    def userMove(self, x, y):
        if Board.boardList[x][y] == '-':
            Board.boardList[x][y] = 'U'
            return True
        return False
    
    def isboardEmpty():
        for i in range(3):
            for j in range(3):
                if Board.boardList[i][j] == '-':
                    return True
        return False
    
    def isEmpty(self):
        for i in range(3):
            for j in range(3):
                if Board.boardList[i][j] == '-':
                    return True
        return False
    

    def computerMove(self):
        temp = Board.isboardEmpty()
        if temp == False:
            return False 
        while True:
            n1 = random.randint(0, 2)
            n2 = random.randint(0, 2)
            if Board.boardList[n1][n2] == '-':
                Board.boardList[n1][n2] = 'C'
                break
        return True
    
    def checkWinner(self):
        if Board.boardList[0][0] == Board.boardList[1][1] and Board.boardList[1][1] == Board.boardList[2][2]:
            return Board.boardList[0][0]
        
        elif Board.boardList[0][2] == Board.boardList[1][1] and Board.boardList[1][1] == Board.boardList[2][0]:
            return Board.boardList[0][2]
        
        elif Board.boardList[0][0] == Board.boardList[0][1] and Board.boardList[0][1] == Board.boardList[0][2]:
            return Board.boardList[0][0]
        
        elif Board.boardList[1][0] == Board.boardList[1][1] and Board.boardList[1][1] == Board.boardList[1][2]:
            return Board.boardList[1][0]
        
        elif Board.boardList[2][0] == Board.boardList[2][1] and Board.boardList[2][1] == Board.boardList[2][2]:
            return Board.boardList[2][0]
        
        elif Board.boardList[0][0] == Board.boardList[1][0] and Board.boardList[1][0] == Board.boardList[2][0]:
            return Board.boardList[0][0]
        
        elif Board.boardList[0][1] == Board.boardList[1][1] and Board.boardList[1][1] == Board.boardList[2][1]:
            return Board.boardList[0][1]
        
        elif Board.boardList[0][2] == Board.boardList[1][2] and Board.boardList[1][2] == Board.boardList[2][2]:
            return Board.boardList[0][2]
        
        else:
            return 'D'


class Game:
    br = Board()

    def getValue(self, x):
        d = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}   
        return d.get(x)
    
    def start(self):
        print("\nTo play the game enter the number like for first position enter 1, for ninth position enter 9,then \'U\' will be shown")
        print("---------Game Start----------")

    def moves(self):
        while True:
            Game.br.display()
            number = int(input("Enter the number:"))
            k = game.getValue(number)
            x = k[0]
            y = k[1]
            uRes = Game.br.userMove(x, y)
            if uRes == False:
                print("Invalid Maove!!")
            if Game.end():
                Game.br.display()
                print("Game Ended")
                break  
            cRes = Game.br.computerMove()
            if Game.end():
                Game.br.display()
                print("Game Ended")
                break 
            
    
    def end():
        result = Game.br.checkWinner()
        r = Game.br.isEmpty()
        if result == 'D' and r == False:
            print("Game Draw!!!!")
            return True
        elif result == 'U':
            print("You WON!!!!!")
            return True
        elif result == 'C':
            print("YOU LOST!!!")
            return True
        return False
    

game = Game()
game.start()
game.moves()
    
    


            

