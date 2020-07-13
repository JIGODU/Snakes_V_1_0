#importing Stuff
import os
import random
import time

#constants
SLEEP_DELAY=0.00043853282928466795
SCREEN="╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n║                                                                                                                      ║\n╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"

boundary=list()
for i in range(0,len(SCREEN)):
    if SCREEN[i]!=" ":
        boundary.append(i)

#screen resolution setting
def setscreen():
    if(os.name=='nt'):
        os.system('mode con cols=120 lines=30')
    else:
        os.system("printf \'\\e[8;30;120t\'")

#screen clear
def clean():
    if(os.name=='nt'):
        os.system('cls')
    else:
        os.system('clear')

#screenprinter
#good to call setscreen before call
def screenprint(screen,fps,workdelay):
    start=time.perf_counter()
    print(screen)
    end=time.perf_counter()
    total=end-start+SLEEP_DELAY+workdelay
    if(total<1/fps):
        sleeps=(1/fps)-total
        time.sleep(sleeps)
        clean()
        return 0
    else:
        return 1
#random position maker
def randpos():
    rowsel=0
    colsel=0
    selpoint=0
    rowsel=random.randrange(1,26)
    colsel=random.randrange(4,116)
    selpoint=122
    selpoint=selpoint+colsel
    for _ in range(0,rowsel):
        selpoint=selpoint+121
    return selpoint

#string editor of space
def trailremove(pos,strin):
    tempscreen=""
    for i in range(0,len(strin)):
        if i==pos:
            tempscreen+=' '
        else:
            tempscreen+=strin[i]
    return tempscreen

#print snake
def snakeprint(snake,screen):
    tempscreen=""
    snakechar=list()
    for i in range(0,len(snake)):
        if i==0 :
            snakechar.append('█')
        elif snake[i]==snake[i-1]-1 :
            snakechar.append('█')
        elif snake[i]==snake[i-1]+1:
            snakechar.append('█')
        elif snake[i]==(snake[i-1]+121):
            snakechar.append('█')
        elif snake[i]==(snake[i-1]-121):
            snakechar.append('█')
    for i in range(0,len(screen)):
        if i in snake:
            pos=snake.index(i)
            tempscreen+=snakechar[pos]
        else:
            tempscreen+=screen[i]
    return tempscreen

#bait postion editor
def bait(pos,strin):
    tempscreen=""
    for i in range(0,len(strin)):
        if i==pos:
            tempscreen+='♦'
        else:
            tempscreen+=strin[i]
    return tempscreen

#movement detector
def move(w,selpos,boudary):
    selposold=selpos
    if w==b'w':
        selpos=selpos-121
    elif w==b'a':
        selpos=selpos-1
    elif w==b's':
        selpos=selpos+121
    elif w==b'd':
        selpos=selpos+1
    if selpos in boundary:
        selpos=selposold
    return selpos

#snake mover
def snmove(snake,selpos):
    snake.insert(0,selpos)
    del snake[-1]
    return snake

#debuggers
#fps binder
def bindfps(strin,fps):
    fps="fps:"+str(fps)
    out=strin+"\n"+str(fps)
    return out