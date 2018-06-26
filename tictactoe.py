class Tictactoe:
    def __init__(self):
        self.board=[".",".",".",".",".",".",".",".","."]
    
    def display(self):
        print "\n\n\t\t\t "+self.board[0]+" | "+self.board[1]+" | "+self.board[2]+" \n"
        print "\t\t\t-----------"
        print " \t\t\t"+self.board[3]+" | "+self.board[4]+" | "+self.board[5]+" \n"
        print "\t\t\t-----------"
        print " \t\t\t"+self.board[6]+" | "+self.board[7]+" | "+self.board[8]+" \n"         
    
    def isfull(self):
        count=0
        for i in self.board:
            if(i!='.'):
                count +=1
        if(count==9):
            return True
        else:
                return False   
    def input_to_index(self,user_input):
        converted_input = user_input - 1
        return converted_input                 
    def move(self,index,player):
        if(self.board[index]!='.'):
            print "\t\tWRONG MOVE SPACE ALREADY OCCUPIED"
        else:
            if(player==0):    
                self.board[index]='X'
            if(player==1):
                self.board[index]='O' 
    
    def result(self):
        if((self.board[0]=='X'and self.board[1]=='X' and self.board[2]=='X')):
           return 1
        elif((self.board[0]=='O'and self.board[1]=='O' and self.board[2]=='O')):
           return 2   
        elif((self.board[3]=='X'and self.board[4]=='X' and self.board[5]=='X')):
           return 1   
        else:
            return 0

