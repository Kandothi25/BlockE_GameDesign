#Ishaan Kandoth
#3/8/22
#draw circles and rectangles
#use keys to move objects
#use dictionaries
import os, random, pygame, datetime
#Objective is for rectangle to run away from circle
#If they colide, circle eats the rectangle and gets larger
#Rectangle restarts
os.system('cls')
name=input('Enter your username: ')
#Initialize pygame
pygame.init()
#Declare constants, lists, variables, dictionaries, any object

#screen size
WIDTH=700
HEIGHT=600
check=True #for the while loop
playGame=True #for the game loop
move=10
jump_move=10
jumping=False
rad=15
gameScore=0
S_coords=True
C_coords=True
MAIN=True
GAME=False
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCOREBOARD=False
EXIT=False
SC_SIZE=False
SHP_COORDINATES=False
CRSR_COORDINATES=False
CIRCLE_CLR=False
MOVEMENT=False
#creating screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#Menu variables
wb_btn=30
hb_btn=30
xs_btn=50
ys_btn=250
MenuList=['Play','Instruction','Setting','Level 1','Level 2','Level 3','Scoreboard','Exit']
SettingList=['Screen Size','Shape Coordinates','Cursor Coordinates','Circle Color','Movement Speed']
ScreenSizeList=['600 x 600','800 x 800','1000 x 1000']
CoordsList=['On','Off']
ColorsMenuList1=['red','orange','yellow']
ColorsMenuList2=['green','blue','purple']
ColorsMenuList3=['cyan','magenta','white']
MovementList=['Normal','Fast','Hyperspeed']

#define colors
colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
'white':[255,255,255],'black':[0,0,0]}
randColor=random.choice(list(colors))

#Get colors
background=pygame.transform.scale(pygame.image.load('FinalGame\city.jpg'),(700,600))
cr_color=colors.get('white')
hb_color=colors.get('white')
sq_btn_color=colors.get('cyan')
#Giving the square a random color
def ChangeColor():
    global randColor
    ColorCheck=True
    while ColorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background or colors.get(randColor)==cr_color:
            randColor=random.choice(list(colors))
        else:
            ColorCheck=False
ChangeColor()
sq_color=colors.get(randColor)

def Game():
    global screen, move, check, playGame, sq_color, jump_move, jumping, gameScore, GAME, MAIN, WIDTH, HEIGHT
    gameScore=0
    #square variables
    xs=20
    ys=20
    wbox=30
    hbox=30

    #circle variables
    rad=15
    xc=random.randint(rad,WIDTH-rad)
    yc=random.randint(rad,HEIGHT-rad)
    #creating square
    square=pygame.Rect(xs,ys,wbox,hbox)

    #circle hitbox
    c_wbox=20
    c_hbox=20
    xh=xc-(rad/1.5)
    yh=yc-(rad/1.5)
    hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)
    playGame=True
    while playGame:
        if S_coords:
            print('■','[',square.x,',',square.y,']')
            print('●','[',xc,',',yc,']')
            os.system('cls')
        else:
            print('')
            os.system('cls')
        screen.blit(background,(0,0))
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                check=False
                playGame=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            GAME=False
            playGame=False
            MAIN=True
        #movement for square
        if keys[pygame.K_LEFT] and square.x>=move:
            square.x-=move
        if keys[pygame.K_RIGHT] and square.x<=WIDTH-(wbox+move):
            square.x+=move
        if keys[pygame.K_UP] and square.y>=move:
            square.y-=move
        if keys[pygame.K_DOWN] and square.y<=HEIGHT-(hbox+move):
            square.y+=move
        if jumping==False and keys[pygame.K_SPACE]:
            jumping = True
        if jumping:
            square.y-=jump_move
            jump_move-=1
            if jump_move< -10:
                jumping=False
                jump_move=10
        #movement for circle
        if keys[pygame.K_a] and xc>=move:
            xc-=move
            hitbox.x-=move
        if keys[pygame.K_d] and xc<=WIDTH-move:
            xc+=move
            hitbox.x+=move
        if keys[pygame.K_w] and yc>=move:
            yc-=move
            hitbox.y-=move
        if keys[pygame.K_s] and yc<=HEIGHT-move:
            yc+=move
            hitbox.y+=move
        #collisions
        if square.colliderect(hitbox):
            xs=random.randint(0,WIDTH-wbox)
            ys=random.randint(0,HEIGHT-hbox)
            ChangeColor()
            sq_color=colors.get(randColor)
            square=pygame.Rect(xs,ys,wbox,hbox)
            rad+=10
            c_wbox+=13.5
            c_hbox+=13.5
            xh=xc-(rad/1.5)
            yh=yc-(rad/1.5)
            hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)

        #Finish circle
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)
        pygame.draw.rect(screen, hb_color, hitbox)
        pygame.display.update()
        pygame.time.delay(1)
    gameScore=rad-15

#Fonts
TITLE_FNT=pygame.font.SysFont('comicsans',80)
MENU_FNT=pygame.font.SysFont('courier',40)
INST_FNT=pygame.font.SysFont('calibri',25)

#Menu Screen Variables
def TitleMenu(Message):
    text=TITLE_FNT.render(Message,1,'green')
    screen.blit(background,(0,0))
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)

def MainMenu(Mlist,xOption):
    global xs_btn,ys_btn,wb_btn,hb_btn
    xs_btn=50
    ty=250
    xs_btn+=xOption
    ys_btn=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,'green')
        screen.blit(text,(xs_btn+40,ty))
        square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
        pygame.draw.rect(screen,sq_btn_color,square_button)
        ys_btn+=50
        ty+=50
    pygame.display.update()
    pygame.time.delay(1)

def ColorMenu():
    global xs_btn,ys_btn,wb_btn,hb_btn,cr_color,hb_color
    xs_btn=50
    ty=250
    xs_btn+=40
    ys_btn=250
    for i in range(len(ColorsMenuList1)):
        message=ColorsMenuList1[i]
        text=INST_FNT.render(message,1,'white')
        screen.blit(text,(xs_btn+40,ty))
        square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
        sq_btn_color=ColorsMenuList1[i]
        pygame.draw.rect(screen,sq_btn_color,square_button)
        ys_btn+=50
        ty+=50
    xs_btn=50
    ty=250
    xs_btn+=240
    ys_btn=250
    for i in range(len(ColorsMenuList2)):
        message=ColorsMenuList2[i]
        text=INST_FNT.render(message,1,'white')
        screen.blit(text,(xs_btn+40,ty))
        square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
        sq_btn_color=ColorsMenuList2[i]
        pygame.draw.rect(screen,sq_btn_color,square_button)
        ys_btn+=50
        ty+=50
    xs_btn=50
    ty=250
    xs_btn+=440
    ys_btn=250
    for i in range(len(ColorsMenuList3)):
        message=ColorsMenuList3[i]
        text=INST_FNT.render(message,1,'white')
        screen.blit(text,(xs_btn+40,ty))
        square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
        sq_btn_color=ColorsMenuList3[i]
        pygame.draw.rect(screen,sq_btn_color,square_button)
        ys_btn+=50
        ty+=50
    if ((xm>90 and xm<120) and (ym>250 and ym<290)):
        cr_color=colors.get('red')
        hb_color=colors.get('red')
        ChangeColor()
    if ((xm>90 and xm<120) and (ym>300 and ym<340)):
        cr_color=colors.get('orange')
        hb_color=colors.get('orange')
        ChangeColor()
    if ((xm>90 and xm<120) and (ym>350 and ym<390)):
        cr_color=colors.get('yellow')
        hb_color=colors.get('yellow')
        ChangeColor()
    if ((xm>290 and xm<320) and (ym>250 and ym<290)):
        cr_color=colors.get('green')
        hb_color=colors.get('green')
        ChangeColor()
    if ((xm>290 and xm<320) and (ym>300 and ym<340)):
        cr_color=colors.get('blue')
        hb_color=colors.get('blue')
        ChangeColor()
    if ((xm>290 and xm<320) and (ym>350 and ym<390)):
        cr_color=colors.get('purple')
        hb_color=colors.get('purple')
        ChangeColor()
    if ((xm>490 and xm<520) and (ym>250 and ym<290)):
        cr_color=colors.get('cyan')
        hb_color=colors.get('cyan')
        ChangeColor()
    if ((xm>490 and xm<520) and (ym>300 and ym<340)):
        cr_color=colors.get('magenta')
        hb_color=colors.get('magenta')
        ChangeColor()
    if ((xm>490 and xm<520) and (ym>350 and ym<390)):
        cr_color=colors.get('white')
        hb_color=colors.get('white')
        ChangeColor()
    pygame.display.update()
    pygame.time.delay(1)

#instructions screen variables
title=TITLE_FNT.render('MENU',1,'green')
xt=WIDTH/2-title.get_width()/2
Instructions=MENU_FNT.render('Instructions:',1,'white')
inst1=INST_FNT.render('~ There is one circle and one square.',1,'white')
inst2=INST_FNT.render('- Move the square with arrow keys.',1,'white')
inst3=INST_FNT.render('- Move the circle with WASD keys.',1,'white')
inst4=INST_FNT.render('~ The circle must eat the square and the square must escape.',1,'white')
inst5=INST_FNT.render('~ When they collide, the circle grows and the square is teleported.',1,'white')
inst6=INST_FNT.render('- [esc] to return to the main menu and [e] to return to settings.',1,'white')
inst7=INST_FNT.render('- Make sure to click the exit button to record your score.',1,'white')
inst8=INST_FNT.render('* Coordinates are displayed in the terminal',1,'white')

#displaying instructions screen
def instScreen():
    screen.blit(background,(0,0))
    screen.blit(title,(xt,50))
    screen.blit(Instructions,(200,200))
    screen.blit(inst1,(10,300))
    screen.blit(inst2,(10,350))
    screen.blit(inst3,(10,400))
    screen.blit(inst4,(10,450))
    screen.blit(inst5,(10,500))
    screen.blit(inst6,(10,550))
    screen.blit(inst7,(10,600))
    screen.blit(inst8,(10,650))
def keepScore(score):
    date=datetime.datetime.now()
    scoreLine=str(score)+' '+name+' '+date.strftime('%m/%d/%Y'+'\n')
    #open a file and write
    #when you write it erases the previous text
    myFile=open('ClassStuff\score.txt','a')
    myFile.write(scoreLine)
    myFile.close()
def screensizeChange():
    global HEIGHT, WIDTH, screen, xmUP, ymUP
    if ((xmUP>90 and xmUP<120) and (ymUP>250 and ymUP<290)) and ((xmR>90 and xmR<120) and (ymR>250 and ymR<290)):
        HEIGHT=600
        WIDTH=600
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        xmUP=0
        ymUP=0
    if ((xmUP>90 and xmUP<120) and (ymUP>300 and ymUP<340)):
        HEIGHT=800
        WIDTH=800
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        xmUP=0
        ymUP=0
    if ((xmUP>90 and xmUP<120) and (ymUP>350 and ymUP<390)):
        HEIGHT=1000
        WIDTH=1000
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        xmUP=0
        ymUP=0
def movementChange():
    global move
    if ((xm>90 and xm<120) and (ym>250 and ym<290)):
        move=10
    if ((xm>90 and xm<120) and (ym>300 and ym<340)):
        move=25
    if ((xm>90 and xm<120) and (ym>350 and ym<390)):
        move=50

while check:
    if MAIN:
        pygame.mouse.set_visible(True)
        pygame.display.set_caption('Menu')
        screen.blit(background,(0,0))
        TitleMenu("Circle eats Square")
        MainMenu(MenuList,0)
    if GAME:
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        pygame.mouse.set_visible(False)
        pygame.display.set_caption('Circle eats Square')
        Game()
        if keys[pygame.K_ESCAPE]:
            GAME=False
            MAIN=True
    if INST:
        pygame.display.set_caption('Instructions')
        TitleMenu("INSTRUCTIONS")
        instScreen()
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
    if SETT:
        pygame.display.set_caption('Settings')
        TitleMenu("SETTINGS")
        MainMenu(SettingList,0)
        if keys[pygame.K_ESCAPE]:
            SETT=False
            MAIN=True
    if SC_SIZE:
        pygame.display.set_caption('Screen Size')
        TitleMenu("SCREEN SIZE")
        MainMenu(ScreenSizeList,40)
        screensizeChange()
        if keys[pygame.K_e]:
            SC_SIZE=False
            SETT=True
        if keys[pygame.K_ESCAPE]:
            SC_SIZE=False
            MAIN=True
    if SHP_COORDINATES:
        pygame.display.set_caption('Shape Coordinates')
        TitleMenu("COORDINATES")
        MainMenu(CoordsList,40)
        if ((xm>90 and xm<120) and (ym>250 and ym<290)):
            S_coords=True
        if ((xm>90 and xm<120) and (ym>300 and ym<340)):
            S_coords=False
        if keys[pygame.K_e]:
            SHP_COORDINATES=False
            SETT=True
        if keys[pygame.K_ESCAPE]:
            SHP_COORDINATES=False
            MAIN=True
    if CRSR_COORDINATES:
        pygame.display.set_caption('Cursor Coordinates')
        TitleMenu("COORDINATES")
        MainMenu(CoordsList,40)
        if ((xm>90 and xm<120) and (ym>250 and ym<290)):
            C_coords=True
        if ((xm>90 and xm<120) and (ym>300 and ym<340)):
            C_coords=False
        if keys[pygame.K_e]:
            CRSR_COORDINATES=False
            SETT=True
        if keys[pygame.K_ESCAPE]:
            CRSR_COORDINATES=False
            MAIN=True
    if CIRCLE_CLR:
        pygame.display.set_caption('Circle Color')
        TitleMenu("CIRCLE COLOR")
        ColorMenu()
        if keys[pygame.K_e]:
            CIRCLE_CLR=False
            SETT=True
        if keys[pygame.K_ESCAPE]:
            CIRCLE_CLR=False
            MAIN=True
    if MOVEMENT:
        pygame.display.set_caption('Movement')
        TitleMenu("MOVEMENT")
        MainMenu(MovementList,40)
        movementChange()
        if keys[pygame.K_e]:
            MOVEMENT=False
            SETT=True
        if keys[pygame.K_ESCAPE]:
            MOVEMENT=False
            MAIN=True
    if LEV_I:
        pygame.display.set_caption('Level 1')
        TitleMenu("LEVEL 1")
        if keys[pygame.K_ESCAPE]:
            LEV_I=False
            MAIN=True
    if LEV_II:
        pygame.display.set_caption('Level 2')
        TitleMenu("LEVEL 2")
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        pygame.display.set_caption('Level 3')
        TitleMenu("LEVEL 3")
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCOREBOARD:
        pygame.display.set_caption('Scoreboard')
        TitleMenu("SCOREBOARD")
        myFile=open('ClassStuff\score.txt','r')
        scoreboardLines=myFile.readlines()
        textY=250
        for i in range(len(scoreboardLines)):
            newScoreLine=MENU_FNT.render(scoreboardLines[i],1,'white')
            textX=WIDTH/2-newScoreLine.get_width()/2
            screen.blit(newScoreLine,(textX,textY))
            textY+=50
        pygame.display.update()
        if keys[pygame.K_ESCAPE]:
            SCOREBOARD=False
            MAIN=True
    if EXIT:
        TitleMenu("Game Over")
        keepScore(gameScore)
        check=False

    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    mouse_posR=pygame.mouse.get_pos()
    xmR=mouse_posR[0]
    ymR=mouse_posR[1]
    if C_coords:
        print('NEUTRAL','[',xmR,',',ymR,']')
        os.system('cls')
    if case.type==pygame.MOUSEBUTTONUP:
        mouse_posUP=pygame.mouse.get_pos()
        xmUP=mouse_posUP[0]
        ymUP=mouse_posUP[1]
        if C_coords:
            print('UP','[',xmUP,',',ymUP,']')
        if SETT:
            pygame.display.set_caption('Settings')
            TitleMenu("SETTINGS")
            MainMenu(SettingList,0)
            if keys[pygame.K_ESCAPE]:
                SETT=False
                MAIN=True
        if MAIN and ((xmUP >20 and xmUP <80) and (ymUP >350 and ymUP <390))or SETT :
            MAIN=False
            SETT=True
        
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        xm=mouse_pos[0]
        ym=mouse_pos[1]
        if C_coords:
            print('DOWN','[',xm,',',ym,']')
            os.system('cls')
        if MAIN and ((xm >20 and xm <80) and (ym >250 and ym <290))or GAME:
            MAIN=False
            GAME=True
        if MAIN and ((xm >20 and xm <80) and (ym >300 and ym <340))or INST :
            MAIN=False
            INST=True
        # if MAIN and ((xm >20 and xm <80) and (ym >350 and ym <390))or SETT :
        #     MAIN=False
        #     SETT=True
        if MAIN and ((xm >20 and xm <80) and (ym >400 and ym <440))or LEV_I :
            MAIN=False
            LEV_I=True
        if MAIN and ((xm >20 and xm <80) and (ym >450 and ym <490))or LEV_II :
            MAIN=False
            LEV_II=True
        if MAIN and ((xm >20 and xm <80) and (ym >500 and ym <540))or LEV_III :
            MAIN=False
            LEV_III=True
        if MAIN and ((xm >20 and xm <80) and (ym >550 and ym <590))or SCOREBOARD :
            MAIN=False
            SCOREBOARD=True
        if MAIN and ((xm >20 and xm <80) and (ym >600 and ym <640))or EXIT :
            MAIN=False
            EXIT=True
        #settings menu
        if SETT and ((xm >20 and xm <80) and (ym >250 and ym <290)):
            SETT=False
            SC_SIZE=True
        if SETT and ((xm >20 and xm <80) and (ym >300 and ym <340)):
            SETT=False
            SHP_COORDINATES=True
        if SETT and ((xm >20 and xm <80) and (ym >350 and ym <390)):
            SETT=False
            CRSR_COORDINATES=True
        if SETT and ((xm >20 and xm <80) and (ym >400 and ym <440)):
            SETT=False
            CIRCLE_CLR=True
        if SETT and ((xm >20 and xm <80) and (ym >450 and ym <490)):
            SETT=False
            MOVEMENT=True
    pygame.display.update()
    pygame.time.delay(1)