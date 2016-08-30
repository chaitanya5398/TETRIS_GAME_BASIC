from gamepalymod import *
import sys,time,threading

"""
I am implementing levels based on the speed.
For every increment of 100 in the score the level increases.
And for each level increase I am decreasing the block fall speed by 0.025s and base speed is 2s.
"""
#To reset all the global variables used for a fresh instance of the game.
def resetvar():
    global gm 
    global dtime
    global new
    global spc
    global fl
    global exit
    gm = gameplay()
    dtime=0
    new=0
    spc=0
    fl=0
    exit=0

#Putting a margin leaving 70 on either side
def setup():
    gs.fill(background)
    pygame.draw.rect(gs,black,[0,0,62,337])
    pygame.draw.rect(gs,black,[428,0,172,337])
    pygame.draw.rect(gs,white,[471,43,110,100])
    pygame.draw.rect(gs,white,[471,215,110,100])
    display_scr_cntrl()
    display_score_level()
    pygame.draw.lines(gs,black,False,[(62,0),(62,335),(428,335),(428,0)],10)
""""
This is the function which takes care of the intermeiatery portion-event handling portion.
here a different approach to reset is used only in the rotate portion K-s .see if problem comes in block merging.
"""
def middle(e):
    global dtime#For the onedown fucntion to be called.
    global fl#for restarting the game.
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
            gm.resetblockplace(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)
            if gm.checkpiecepos(gm.curblock.xb+1,gm.curblock.yb,gm.curblock.curr ) == 1:
                gm.fillpiecepos(gm.curblock.xb+1,gm.curblock.yb,gm.curblock.curr)
                gm.curblock.moveright()
            else:
                gm.fillpiecepos(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)

    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT or e.key == pygame.K_a:
            gm.resetblockplace(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)
            if gm.checkpiecepos(gm.curblock.xb-1,gm.curblock.yb,gm.curblock.curr) == 1:
                gm.fillpiecepos(gm.curblock.xb-1,gm.curblock.yb,gm.curblock.curr)
                gm.curblock.moveleft()
            else:
                gm.fillpiecepos(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)
                
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_DOWN or e.key == pygame.K_s:
            gm.resetblockplace(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)
            gm.curblock.rotate()
            if(gm.checkpiecepos(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr) == 1):
                gm.fillpiecepos(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)
            else:
                gm.curblock.revertrot()
                gm.fillpiecepos(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)
                
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_SPACE:
            while spc==0:
                onedown()
                
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_r:
            fl=1

#The function for when block starts falling.
def start():
    global new
    global spc
    global fl
    spc=0
    new=1
    #First checking conditoins.
    gm.checkrowfull()
    gm.selectpiece()
    #Checking if the position is empty.
    #gm.resetblockplace(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)        
    if(  (gm.checkpiecepos(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr) == 0) and (gm.curblock.xb==14 and gm.curblock.yb==0) ):
        fl=1
    else:
        gm.fillpiecepos(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)

def onedown():
    global new
    global spc
    gm.resetblockplace(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)
    #first reset and then check and see correspondingly.
    if gm.checkpiecepos(gm.curblock.xb,gm.curblock.yb+1,gm.curblock.curr) == 0:
        gm.fillpiecepos(gm.curblock.xb,gm.curblock.yb,gm.curblock.curr)
        gm.updatescore(0)
        spc=1
        new=0
    else:
        gm.fillpiecepos(gm.curblock.xb,gm.curblock.yb+1,gm.curblock.curr)
        gm.curblock.yb = gm.curblock.yb+1#This was not written in the functions.

#This is a function which is called when the game is over and relpay is asked.        
def replay():
    gs.fill(black)
    display_text("Game Over",white,50,250,85)
    display_text("Press RETURN for NewGame",white,25,125,170)
    display_text("Press q for Exit",white,25,325,255)
    pygame.display.update()
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            sys.exit()
        if p.type == pygame.KEYDOWN:
            if p.key==pygame.K_RETURN:
                resetvar()
                return
            elif p.key==pygame.K_q:
                exit=1

#Function to display text on screen.
def display_text(txt,color,size,x,y):
    msg = pygame.font.SysFont(None,size)
    fin = msg.render(txt,True,color)
    gs.blit(fin,[x,y])

def display_scr_cntrl():
    display_text("CONTROLS",black,15,485,48)
    display_text("LEFT/a - Left",black,15,485,65)
    display_text("RIGHT/d - Right",black,15,485,80)
    display_text("DOWN/a - Rotate",black,15,485,95)
    display_text("SPACE - Full Down",black,15,485,110)
    display_text("r - Restart",black,15,485,125)

def display_score_level():
    display_text("SCORE",black,15,485,240)
    display_text(str(gm.score),black,20,485,250)
    display_text("LEVEL",black,15,485,265)
    display_text(str(gm.level),black,20,485,280)
    

        
##The final runtime-management code.
"""
new: tells wheter or not to execute start so each time a new one falls it is 1.
spc: To find till when it has to go-down.
     So each time a new block falls we make it 0 and hence the space key press for enabling is done.
"""


gm = gameplay()
dtime=0
new=0
spc=0
fl=0
exit=0

while exit==0:
    setup()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit=1
            break
        else:
            if new==0:
                start()
        if fl==0:
            middle(e)
        else:
            break
    if new==0:
        start()
        print "Speed Of Falling: ",gm.time
    if(time.time() - dtime >=gm.time):
        onedown()#To move the block down by one unit.
        dtime = time.time()
    if fl == 1:
        replay()
        continue
    gm.draw()
    pygame.display.update()
    
pygame.quit()
quit()    
