#I am creating an array signifyig the board.
class board():
    def __init__(self):
        self.board=[[0 for l in range(32)] for j in range(30)]
    #returns 1 if the block can occupy else 0.
    def checkpiecepos(self,x,y,array):
        for i in range(x,x+4):
            for j in range(y,y+4):
                if(array[i-x][j-y]):
                    if(i<0 or i>31 or j>=30):
                        return 0
                if( (i>=0 and i<=31 and j<=29) and (array[i-x][j-y]==1) ):
                    if (self.board[j][i]==1):
                        return 0
        return 1
    def fillpiecepos(self,x,y,array):
        for i in range(x,x+4):
            for j in range(y,y+4):
                if(array[i-x][j-y]==1):
                    self.board[j][i] = 1
    #This is used for making the old co-ordinates of the block
    #empty when it is ready to move i.e only if checkpiecepos
    #returns 1.
    #The co-ordinates used are the old ones used for previous fill and should be called before move or rotate is called.
    def resetblockplace(self,x,y,array):
        for i in range(x,x+4):
            for j in range(y,y+4):
                if(i>=0 and i<32 and j<30 and array[i-x][j-y]==1):
                    self.board[j][i] = 0

