import snks
import msvcrt
import os
import time

def game():
    myscreen=snks.SCREEN
    w=b'a'
    boundary=list()
    for i in range(0,len(myscreen)):
        if myscreen[i]!=" ":
            boundary.append(i)

    snks.setscreen()

    #snake defining
    snake_pos=snks.randpos()
    snake=list()
    snake.append(snake_pos)
    snake.append(snake_pos+1)
    snake.append(snake_pos+2)
    lost=0
    counter=0
    speed=20
    fps=60
    #  bait came in here
    baitp=snks.randpos()
    w=b'w'
    while baitp in snake:
        baitp=snks.randpos()
    #  Whole game I/O and mechanics. I know its a mess
    while True:
        ate=0
        if(msvcrt.kbhit()):
            start=time.time()
            oldw=w
            w=msvcrt.getch()
            if w==b'w' and oldw==b's':
                w=oldw
            elif w==b's' and oldw==b'w':
                w=oldw
            elif w==b'a' and oldw==b'd':
                w=oldw
            elif w==b'd' and oldw==b'a':
                w=oldw
            next_pos=snks.move(w,snake[0],boundary)
            if next_pos in snake:
                lost=1
                break
            myscreen=snks.trailremove(snake[-1],myscreen)
            snake=snks.snmove(snake,next_pos)
            myscreen=snks.bait(baitp,myscreen)
            myscreen=snks.snakeprint(snake,myscreen)
            end=time.time()
            delay=end-start
            flag=snks.screenprint(myscreen,fps,delay)
            if(flag) and fps>1:
                fps-=1
            elif fps<60:
                fps+=1
            if baitp==snake[0]:
                ate=1
        else:
            start=time.time()
            if counter>=speed:
                next_pos=snks.move(w,snake[0],boundary)
                if next_pos in snake :
                    lost=1
                    break
                myscreen=snks.trailremove(snake[-1],myscreen)
                snake=snks.snmove(snake,next_pos)
                myscreen=snks.bait(baitp,myscreen)
                myscreen=snks.snakeprint(snake,myscreen)
                counter=0
                if baitp==snake[0]:
                    ate=1
            else:
                end=time.time()
                delay=end-start
                flag=snks.screenprint(myscreen,fps,delay)
                if(flag) and fps>1:
                    fps-=1
                elif fps<60:
                    fps+=1
            if w==b'a' or w==b'd':
                counter+=4
            else:
                counter+=2
        if ate==1:
            baitp=snks.randpos()
            while baitp in snake:
                baitp=snks.randpos()
            snake.append(next_pos)
            if speed>0:
                speed-=1
            else:
                speed=speed
    if(lost==1):
        os.system('cls')
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\tGAME OVER.....\n\n\n\n\n\n\n\n\n\n\n\n")
        time.sleep(1)
        os.system('cls')
# what was I thingking ? 
game()