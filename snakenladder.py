#ludo game
from graphics import *
import random
import time

board_multiplier = 1.5
winx = 420*board_multiplier
winy = 450*board_multiplier
cx,cy = 30,30
i = 0
EXIT = 0
key = 1
toggle = 1
b = []
num = []
p1 = Circle(Point(300,600), 5)
p1.setFill("green")
p2 = Circle(Point(325,600), 5)
p2.setFill("red")
p1counter = -1
p2counter = -1

win = GraphWin("Ludo game",winx,winy, autoflush = False)

class board:
    def __init__( self, centerx, centery, ID, length = 15*board_multiplier, breadth = 15*board_multiplier):
        self.centerx = centerx*board_multiplier
        self.centery = centery*board_multiplier
        self.length = length
        self.breadth = breadth
        self.ID = ID
    
    def rect( self):
        self.rec = Rectangle( Point( self.centerx - self.length, self.centery - self.breadth), Point( self.centerx + self.length, self.centery + self.breadth))
        self.rec.setFill("white")
        self.rec.draw(win)
    def txt( self, text):
        self.t = Text(Point(self.centerx + self.length - 12, self.centery + self.breadth - 10),text)
        self.t.setFace("arial")
        self.t.setSize(10)
        self.t.draw(win)

def click_check(objx,objy,objl,objb):
    click = win.getMouse()
    if click.getX() <= objx + objl and click.getX() >= objx - objl and click.getY() <= objy + objb and click.getY() >= objy - objb:
        return 1
    else:
        return 0

while True:
    splayer = board(120,250,"sp",40,20)
    splayer.rect()
    splayer_text = Text(Point(splayer.centerx,splayer.centery),"SP")
    splayer_text.setFace("arial")
    splayer_text.draw(win)

    mplayer = board(200,250,"mp",40,20)
    mplayer.rect()
    mplayer_text = Text(Point(mplayer.centerx,mplayer.centery),"MP")
    mplayer_text.setFace("arial")
    mplayer_text.draw(win)
    
    quit_button = board(280,250,"q",30,20)
    quit_button.rect()
    quit_button_text = Text(Point(quit_button.centerx,quit_button.centery),"QUIT")
    quit_button_text.setFace("arial")
    quit_button_text.draw(win)

    if click_check(splayer.centerx, splayer.centery, splayer.length, splayer.breadth) == 1:
        mode = 1
        p1.draw(win)
        p2.draw(win)
        turntext = Text(Point(150,600),"Player 1's turn")
        turntext.draw(win)
    elif click_check(mplayer.centerx, mplayer.centery, mplayer.length, mplayer.breadth) == 1:
        mode = 2
        p1.draw(win)
        p2.draw(win)
        turntext = Text(Point(150,600),"Player 1's turn")
        turntext.draw(win)
    else:
        EXIT = 1
    splayer.rec.undraw()
    splayer_text.undraw()
    mplayer.rec.undraw()
    mplayer_text.undraw()
    quit_button.rec.undraw()
    quit_button_text.undraw()
    break
    update()

while i<10:
    j = 0
    r = 9
    if key == 1:
        key = 0
    else:
        key = 1
    while j<10:
        
        if(key == 0):    
            b.append(board(cx,cy,100-(10*i+j)))
            r = 9
        else:
            b.append(board(cx,cy,(100-(10*i+j)-r)))
            r -= 2
        b[i*10+j].rect()
        b[i*10+j].txt(b[i*10+j].ID)
        #else:
        #b[i*10+j].txt(101-(i*10+j+1))
        #print("cx:",cx," cy:",cy)
        cx += 35
        j += 1
        #print("j:",j)
    cy += 35
    cx = 30
    i += 1
    #print("i:",i)

dice_button = board(268,400,"d",40,20)
dice_button.rect()
dice_text = Text(Point(400,600),"Roll dice")
dice_text.setFace("arial")
dice_text.draw(win)

s1 = Image(Point(b[54].centerx,b[54].centery),"s1.png")
s1.draw(win)
s2 = Image(Point(b[27].centerx,b[27].centery),"s2.png")
s2.draw(win)
l1 = Image(Point(b[32].centerx,b[32].centery),"l1.png")
l1.draw(win)
l2 = Image(Point(b[76].centerx,b[76].centery),"l2.png")
l2.draw(win)

def snknladder(p,counter,board,toggle,color):
    if(counter == board[6].ID):
        p.undraw()
        if toggle == 0:
            p = Circle(Point(board[48].centerx+8,board[48].centery),5)
        else:
            p = Circle(Point(board[48].centerx-8,board[48].centery),5)
        counter = board[48].ID
        p.setFill(color)
        p.draw(win)
    elif(counter == board[35].ID):
        p.undraw()
        if toggle == 0:
            p = Circle(Point(board[73].centerx+8,board[73].centery),5)
        else:
            p = Circle(Point(board[73].centerx-8,board[73].centery),5)
        counter = board[73].ID
        p.setFill(color)
        p.draw(win)
    elif(counter == board[61].ID):
        p.undraw()
        if toggle == 0:
            p = Circle(Point(board[3].centerx+8,board[3].centery),5)
        else:
            p = Circle(Point(board[3].centerx-8,board[3].centery),5)
        counter = board[3].ID
        p.setFill(color)
        p.draw(win)
    elif(counter == board[97].ID):
        p.undraw()
        if toggle == 0:
            p = Circle(Point(board[55].centerx+8,board[55].centery),5)
        else:
            p = Circle(Point(board[55].centerx-8,board[55].centery),5)
        counter = board[55].ID
        p.setFill(color)
        p.draw(win)
    return p,counter

def mov(p,counter,add,board,toggle,color):
    while add > 0:
        update(12)
        p.undraw()
        counter += 1
        add -= 1
        r = 99
        for obj in board:
            #print(obj.ID,":",counter)
            if obj.ID == counter:
                #print("ID:",obj.ID)
                if toggle == 0:
                    p = Circle(Point(obj.centerx+8,obj.centery), 5)
                else:
                    p = Circle(Point(obj.centerx-8,obj.centery), 5)
                p.setFill(color)
                p.draw(win)
                break
            else:
                continue
        r -= 1
    p,counter = snknladder(p,counter,board,toggle,color)
    return counter, p    

def dice():
    rand = random.randint(1,6)
    return rand

def turn(toggle,text):
    if toggle == 0:
        text.undraw()
        text = Text(Point(150,600),"Player 1's turn")
        text.setFace("arial")
        text.draw(win)
        toggle = 1
    else:
        text.undraw()
        text = Text(Point(150,600),"Player 2's turn")
        text.setFace("arial")
        text.draw(win)
        toggle = 0
    return toggle,text

while EXIT == 0:
    update(15)
    if mode == 2:
        if click_check(dice_button.centerx, dice_button.centery, dice_button.length, dice_button.breadth) == 1:
            die_num = dice()
            toggle,turntext = turn(toggle,turntext)
            if toggle == 0:
                if p1counter == -1:
                    p1counter = 0
                    p1.undraw()
                    p1 = Circle(Point(b[90].centerx-8,b[90].centery), 5)
                    p1.setFill("green")
                    p1.draw(win)
                else:
                    p1.undraw()
                    p1counter,p1 = mov(p1,p1counter,die_num,b,toggle,"green")
                    #print(die_num)
            else:
                if p2counter == -1:
                    p2counter = 0
                    p2.undraw()
                    p2 = Circle(Point(b[90].centerx+8,b[90].centery), 5)
                    p2.setFill("red")
                    p2.draw(win)
                else:
                    p2.undraw()
                    p2counter,p2 = mov(p2,p2counter,die_num,b,toggle,"red")
                    #print(die_num)
    if mode == 1:
        if toggle == 0:
            if click_check(dice_button.centerx, dice_button.centery, dice_button.length, dice_button.breadth) == 1:
                die_num = dice()
                if p1counter == -1:
                    p1counter = 0
                    p1.undraw()
                    p1 = Circle(Point(b[90].centerx-8,b[90].centery), 5)
                    p1.setFill("green")
                    p1.draw(win)
                else:
                    p1.undraw()
                    p1counter,p1 = mov(p1,p1counter,die_num,b,toggle,"green")
                    #print(die_num)
                toggle,turntext = turn(toggle,turntext)
                time.sleep(0.5)
        else:
            die_num = dice()
            if p2counter == -1:
                p2counter = 0
                p2.undraw()
                p2 = Circle(Point(b[90].centerx+8,b[90].centery), 5)
                p2.setFill("red")
                p2.draw(win)
            else:
                p2.undraw()
                p2counter,p2 = mov(p2,p2counter,die_num,b,toggle,"red")
                #print(die_num)
            toggle,turntext = turn(toggle,turntext)
    if p1counter >= 100:
        win2 = GraphWin("Winner",401,401)
        winner = Text(Point(201,201),"Player 1 won!!")
        winner.setFace("arial")
        winner.setSize(25)
        winner.draw(win2)
        EXIT = 1
    elif p2counter >= 100:
        win2 = GraphWin("Winner",401,401)
        winner = Text(Point(201,201),"Player 2 won!!")
        winner.setFace("arial")
        winner.setSize(25)
        winner.draw(win2)
        EXIT = 1
win.getMouse()
win.close()
