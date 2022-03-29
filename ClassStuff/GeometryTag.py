#Ishaan Kandoth
#3/8/22
#draw circles and rectangles
#use keys to move objects
#use dictionaries
import os, random, pygame
#Objective is for rectangle to run away from circle
#If they colide, circle eats the rectangle and gets larger
#Rectangle restarts
os.system('cls')
#Initialize pygame
pygame.init()
#Declare constants, lists, variables, dictionaries, any object

#screen size
WIDTH=700
HEIGHT=700
check=True #for the while loop
move=1
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False

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

#Menu variables
wb_btn=30
hb_btn=30
xs_btn=50
ys_btn=250
MenuList=['Instruction','Setting','Level 1','Level 2','Level 3','Scoreboard','Exit']
SettingList=['Screen Size','Sound','Music']

#circle hitbox
c_wbox=20
c_hbox=20
xh=xc-(rad/1.5)
yh=yc-(rad/1.5)
hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)
#creating screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tag')

#define colors
colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'cyan':[0,255,255],'purple':[128,0,128],'magenta':[255,0,255],
'black':[0,0,0],'white':[255,255,255]}
randColor=random.choice(list(colors))

#Get colors
background=colors.get('black')
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

#Fonts
TITLE_FNT=pygame.font.SysFont('comicsans',80)
MENU_FNT=pygame.font.SysFont('courier',40)
INST_FNT=pygame.font.SysFont('calibri',25)

#Menu Screen Variables
def TitleMenu(Message):
    text=TITLE_FNT.render(Message,1,'green')
    screen.fill('black')
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)

def MainMenu(Mlist):
    ty=250
    square_button.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,'green')
        screen.blit(text,(90,ty))
        pygame.draw.rect(screen,sq_btn_color,square_button)
        square_button.y+=50
        ty+=50
    pygame.display.update()
    pygame.time.delay(1)

#instructions screen variables
title=TITLE_FNT.render('MENU',1,'green')
xt=WIDTH/2-title.get_width()/2
Instructions=MENU_FNT.render('Instructions:',1,'white')
inst1=INST_FNT.render('1) There is one circle and one square.',1,'white')
inst2=INST_FNT.render('2) Move the square with arrow keys.',1,'white')
inst3=INST_FNT.render('3) Move the circle with WASD keys.',1,'white')
inst4=INST_FNT.render('4) The circle must eat the square and the square must escape.',1,'white')
inst5=INST_FNT.render('5) When they collide, the circle grows and the square is teleported.',1,'white')
play=MENU_FNT.render('Press [esc] to play',1,'white')

#displaying instructions screen
def instScreen():
    instr_Check=True
    while instr_Check:
        screen.fill(background)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                instr_Check=False
        keys=pygame.key.get_pressed() #this returns a list
        if keys[pygame.K_ESCAPE]:
            instr_Check=False
        else:
            screen.blit(title,(xt,50))
            screen.blit(Instructions,(200,200))
            screen.blit(inst1,(10,300))
            screen.blit(inst2,(10,350))
            screen.blit(inst3,(10,400))
            screen.blit(inst4,(10,450))
            screen.blit(inst5,(10,500))
            screen.blit(play,(125,600))
        pygame.display.update()
        pygame.time.delay(1)

# TitleMenu('MENU')
# MainMenu(MenuList)
# pygame.time.delay(999)
# instScreen()
while check:
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST:
        instScreen()
    if SETT:
        MainMenu(SettingList)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
            MAIN=False
            screen.fill(background)
            TitleMenu("INSTRUCTIONS")
            INST=True
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340))or SETT :
            MAIN=False
            screen.fill(background)
            TitleMenu("SETTINGS")
            SETT=True
    if keys[pygame.K_ESCAPE]:
            INST=False
            SETT=False
            MAIN=True

    # screen.fill(background)
    # TitleMenu('Geometry Tag')
    # MainMenu(MenuList)
    # pygame.time.delay(999)
    # instScreen()
    # for case in pygame.event.get():
    #     if case.type==pygame.QUIT:
    #         check=False
    # keys=pygame.key.get_pressed()
    # #movement for square
    # if keys[pygame.K_LEFT] and square.x>=move:
    #     square.x-=move
    # if keys[pygame.K_RIGHT] and square.x<=WIDTH-(wbox+move):
    #     square.x+=move
    # if keys[pygame.K_UP] and square.y>=move:
    #     square.y-=move
    # if keys[pygame.K_DOWN] and square.y<=HEIGHT-(hbox+move):
    #     square.y+=move
    # #movement for circle
    # if keys[pygame.K_a] and xc>=move:
    #     xc-=move
    #     hitbox.x-=move
    # if keys[pygame.K_d] and xc<=WIDTH-move:
    #     xc+=move
    #     hitbox.x+=move
    # if keys[pygame.K_w] and yc>=move:
    #     yc-=move
    #     hitbox.y-=move
    # if keys[pygame.K_s] and yc<=HEIGHT-move:
    #     yc+=move
    #     hitbox.y+=move
    # #collisions
    # if square.colliderect(hitbox):
    #     xs=random.randint(0,WIDTH-wbox)
    #     ys=random.randint(0,HEIGHT-hbox)
    #     ChangeColor()
    #     sq_color=colors.get(randColor)
    #     square=pygame.Rect(xs,ys,wbox,hbox)
    #     rad+=10
    #     c_wbox+=13.5
    #     c_hbox+=13.5
    #     xh=xc-(rad/1.5)
    #     yh=yc-(rad/1.5)
    #     hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)

    #Finish circle
    # pygame.draw.rect(screen, sq_color, square)
    # pygame.draw.circle(screen, cr_color, (xc,yc), rad)
    # pygame.draw.rect(screen, hb_color, hitbox)
    pygame.display.update()
    pygame.time.delay(3)
