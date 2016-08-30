from blockmod import *
from boardmod import *
import pygame,random

#Pygame portion..
pygame.init()
black=(0,0,0)
white=(255,255,255)
background = white
#The game area is 351X329.
size=[600,337]
gs = pygame.display.set_mode(size)
pygame.display.set_caption("Black&White Tetris")
#Pygame portion ends.

#I am creating a 2D array where 0th row is the top-most.
class gameplay(block,board):
    def __init__(self):
        self.board = [[0 for j in range(32)] for j in range(30)]
        self.score=0
        self.curblock=None
        self.time=0.2
        self.level=0
        self.check=0#To check if the score has increased by
    #This clears the row and brings down the rest of array.
    def checkrowfull(self):
        for j in range(29,0,-1):
            temp=0
            for k in range(32):
                if self.board[j][k]==0:
                    temp=1;
            if temp==0:
                print "I am coming"
                self.updatescore(1)
                for l in range(j,0,-1):
                    self.board[l] = self.board[l-1];
                self.board[0] = [0 for p in range(32)]
    def updatescore(self,a):
        if a==0:
            self.score  = self.score + 10
        elif a==1:
            self.score = self.score + 100
        if self.score - self.check >= 100:
            self.check = self.score
            self.incrlevel()
            self.time = self.time - 0.025
    def selectpiece(self):
        sel = random.randint(1,5)
        if sel ==1: self.curblock = b1()
        elif sel ==2: self.curblock = b2()
        elif sel==3: self.curblock = b3()
        elif sel==4: self.curblock = b4()
        elif sel==5: self.curblock = b5()
    #I am putting draw here as I am printing the board only always
    def draw(self):
        for i in xrange(30):
            for j in xrange(32):
                if (self.board[i][j]==1):
                    pygame.draw.rect(gs,black,[70+j*11,i*11,10,10])
    def incrlevel(self):
        self.level = self.level + 1
        
