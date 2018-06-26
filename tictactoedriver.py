from tictactoe import Tictactoe
board=Tictactoe()
print("\t\tGIVE THE FOLLOWING DETAILS\n")
count=0
player1=(raw_input("\t\tFIRST PLAYER   :  "))
player2=(raw_input("\t\tSECOND PLAYER  :  "))
while(1):
    if(board.isfull()):
        print "\t\tNO MORE MOVE ALLOWED SPACE IS FULL"
        print "\n\t\t\t\tMATCH DRAWN !!!!!"
        break
    count=count%2
    print"\n\n"
    if(count==0):
        print ("\t\t %s YOUR TURN") % player1
    if(count==1):
        print("\t\t %s YOUR TURN") % player2
    index=int(raw_input("\t\t Place     :  "))
    index = board.input_to_index(index)
    board.move(index,count)
    board.display()
    a=board.result()
    if(a==1):
        print ("\t\t\t\tWINNER   %s  !!!!!!!!!") % player1
        break
    if(a==2):
        print  ("\t\t\t\tWINNER   %s  !!!!!!!!!") % player2
        break
    if (a==0):
        count+=1
        continue
    
               
    
    
