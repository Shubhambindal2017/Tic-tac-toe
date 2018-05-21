class Tictactoe:
    def __init__(self):
        self.board=[ ['.','.','.'],['.','.','.'],['.','.','.']]
    def isfull(self):
        count=0
        for i in self.board:
            if(i!='.'):
                count +=1
        if(count==9):
            return True
        else:
                return False
    def move(self,row,column,player):
        if(self.board[row][column]!='.'):
            print "\t\tWRONG MOVE SPACE ALREADY OCCUPIED"
        else:
            if(player==0):    
                self.board[row][column]='X'
            if(player==1):
                self.board[row][column]='O'
    def result(self):
        for i in range(3):
            if((self.board[0][i]=='X'and self.board[1][i]=='X' and self.board[2][i]=='X')):
               return 1
            if((self.board[0][i]=='O'and self.board[1][i]=='O' and self.board[2][i]=='O')):
               return 2   
            if((self.board[i][0]=='X'and self.board[i][1]=='X' and self.board[i][2]=='X')):
               return 1
            if((self.board[i][0]=='O'and self.board[i][1]=='O' and self.board[i][2]=='O')):
               return 2   
        if((self.board[0][0]=='X'and self.board[1][1]=='X' and self.board[2][2]=='X') or (self.board[0][2]=='X'and self.board[1][1]=='X' and self.board[2][0]=='X')):
           return 1
        if((self.board[0][0]=='O'and self.board[1][1]=='O' and self.board[2][2]=='O') or (self.board[0][2]=='O'and self.board[1][1]=='O' and self.board[2][0]=='O')):
           return 2
        else:
           return 0
    def display(self):
        for i in range(3):
            print "\n\t\t"
            for j in range(3):
                print "\t\t",
                print self.board[i][j],
        print "\n"        
                
            
