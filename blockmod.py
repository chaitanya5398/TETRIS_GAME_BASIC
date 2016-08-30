color=(0,0,0)

class block():
    #mode 1,2,3,4,5. I am making a 4X4 array and 1-blocks.curr is the block to be used for display.
    def __init__(self):
        self.bar = [[0 for y in range(4)]for x in range(4)]
        #Storing various positions in the rot array.
        #The 0,0 index's x,y in xb,yb 
        self.rotcnt=0
        self.xb=14
        self.yb=0
        self.rot=[[[0 for k in range(4)] for l in range(4)]for p in range(4)]
    def rotate(self):
        self.rotcnt = self.rotcnt + 1
        self.curr = self.rot[self.rotcnt%4]
    def revertrot(self):
        self.rotcnt = self.rotcnt - 1
        self.curr = self.rot[self.rotcnt%4]
    def moveleft(self):
        self.xb = self.xb-1
    def moveright(self):
        self.xb = self.xb+1

        
        
        
        
class b1(block):        ####
    def __init__(self):
        block.__init__(self)
        for j in range(4):
            self.bar[0][j] = 1
        self.rot[0]= self.bar
        self.curr = self.bar
        self.rot[1]= [ [0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0] ]
        self.rot[2]= self.bar;self.rot[3]= self.rot[1]

class b2(block):              ###
    def __init__(self):        #
        block.__init__(self)
        for j in range(3):    
            self.bar[0][j] = 1
        self.bar[1][1] = 1
        self.rot[0]= self.bar
        self.curr = self.bar
        self.rot[1]= [ [0,1,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0] ]
        self.rot[2]= [ [0,1,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0] ]
        self.rot[3]= [ [0,1,0,0],[0,1,1,0],[0,1,0,0],[0,0,0,0] ]

class b3(block):
    def __init__(self):
        block.__init__(self)
        for j in range(2):   ##
            self.bar[0][j] = 1    ##
            self.bar[1][j] = 1
        self.rot[0]=self.bar
        self.curr = self.bar
        self.rot[1] = self.bar;self.rot[2]= self.bar;self.rot[3]=self.bar

class b4(block):
    def __init__(self):
        block.__init__(self)
        for j in range(3):       ###
            self.bar[0][j] = 1     #
        self.bar[1][2] = 1
        self.rot[0]= self.bar
        self.curr = self.bar
        self.rot[1]= [ [0,1,0,0],[0,1,0,0],[1,1,0,0],[0,0,0,0] ]
        self.rot[2]= [ [1,0,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0] ]
        self.rot[3]= [ [0,1,1,0],[0,1,0,0],[0,1,0,0],[0,0,0,0] ]

class b5(block):
    def __init__(self):
        block.__init__(self)
        for j in range(2):       ##
            self.bar[0][j] = 1    ##
            self.bar[1][j+1] = 1
        self.rot[0]=self.bar
        self.curr = self.bar
        self.rot[1]= [ [0,1,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0] ]
        self.rot[2]= self.rot[0]
        self.rot[3]= self.rot[1]
