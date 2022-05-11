#Ishaan Kandoth
#4/18/22
#Final Game
import os, pygame, datetime, random, time
os.system('cls')
name=input('Enter your username: ')
pygame.init()
sf=1 #(scale factor) this is so that everything stays proportionate when the screen size changes
WIDTH=700*sf
HEIGHT=600*sf
check=True #for the while loop
playGame=True #for the game loop
move=10*sf
jump_move=10*sf
jumping=False
lvl1Success=False
lvl3Success=False
lvl1Score=0
lvl2Score=0
lvl3Score=0
gameScore=0
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
BACKGROUNDCOLOR=False
BACKGROUNDIMGS=False
playLvl1=True
playLvl2=True
playLvl3=True
displayBGimg=True

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Final Game')

wb_btn=30*sf
hb_btn=30*sf
xs_btn=50*sf
ys_btn=250*sf
MenuList=['Play','Instruction','Setting','Level 1','Level 2','Level 3','Scoreboard','Exit']
SettingList=['Screen Size','Background Images','Background Color']
ScreenSizeList=['350 x 300','700 x 600','1050 x 900']
bgimgsList=['On','Off']
ColorsMenuList1=['red','orange','yellow']
ColorsMenuList2=['green','blue','purple']
ColorsMenuList3=['cyan','magenta','white']

colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
'white':[255,255,255],'black':[0,0,0]}

menuBackground=pygame.transform.scale(pygame.image.load('FinalGame\city.jpg'),(700*sf,600*sf))
sq_btn_color=colors.get('black')
background_color=colors.get('white')

#Fonts
TITLE_FNT=pygame.font.SysFont('comicsans',int(60*sf))
MENU_FNT=pygame.font.SysFont('courier',int(40*sf))
INST_FNT=pygame.font.SysFont('calibri',int(25*sf))

#Menu Screen Variables
def TitleMenu(Message):
    global sf, menuBackground, displayBGimg, background_color
    text=TITLE_FNT.render(Message,1,'black')
    if displayBGimg:
        screen.blit(menuBackground,(0,0))
    else:
        screen.fill(background_color)
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50*sf))
square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)

def MainMenu(Mlist,xOption):
    global xs_btn,ys_btn,wb_btn,hb_btn,sf
    xs_btn=50*sf
    ty=200*sf
    xs_btn+=xOption
    ys_btn=200*sf
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,'yellow')
        screen.blit(text,(xs_btn+40*sf,ty))
        square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
        pygame.draw.rect(screen,sq_btn_color,square_button)
        ys_btn+=50*sf
        ty+=50*sf
    pygame.display.update()
    pygame.time.delay(1)


def ColorMenu():
    global xs_btn,ys_btn,wb_btn,hb_btn,sf,background_color
    xs_btn=50*sf
    ty=250*sf
    xs_btn+=40*sf
    ys_btn=250*sf
    for i in range(len(ColorsMenuList1)):
        message=ColorsMenuList1[i]
        text=INST_FNT.render(message,1,'white')
        screen.blit(text,(xs_btn+40*sf,ty))
        square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
        sq_btn_color=ColorsMenuList1[i]
        pygame.draw.rect(screen,sq_btn_color,square_button)
        ys_btn+=50*sf
        ty+=50*sf
    xs_btn=50*sf
    ty=250*sf
    xs_btn+=240*sf
    ys_btn=250*sf
    for i in range(len(ColorsMenuList2)):
        message=ColorsMenuList2[i]
        text=INST_FNT.render(message,1,'white')
        screen.blit(text,(xs_btn+40*sf,ty))
        square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
        sq_btn_color=ColorsMenuList2[i]
        pygame.draw.rect(screen,sq_btn_color,square_button)
        ys_btn+=50*sf
        ty+=50*sf
    xs_btn=50*sf
    ty=250*sf
    xs_btn+=440*sf
    ys_btn=250*sf
    for i in range(len(ColorsMenuList3)):
        message=ColorsMenuList3[i]
        text=INST_FNT.render(message,1,'white')
        screen.blit(text,(xs_btn+40*sf,ty))
        square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
        sq_btn_color=ColorsMenuList3[i]
        pygame.draw.rect(screen,sq_btn_color,square_button)
        ys_btn+=50*sf
        ty+=50*sf
    if ((xm>90*sf and xm<120*sf) and (ym>250*sf and ym<280*sf)):
        background_color=colors.get('red')
    if ((xm>90*sf and xm<120*sf) and (ym>300*sf and ym<330*sf)):
        background_color=colors.get('orange')        
    if ((xm>90*sf and xm<120*sf) and (ym>350*sf and ym<380*sf)):
        background_color=colors.get('yellow')        
    if ((xm>290*sf and xm<320*sf) and (ym>250*sf and ym<280*sf)):
        background_color=colors.get('green')        
    if ((xm>290*sf and xm<320*sf) and (ym>300*sf and ym<330*sf)):
        background_color=colors.get('blue')        
    if ((xm>290*sf and xm<320*sf) and (ym>350*sf and ym<380*sf)):
        background_color=colors.get('purple')        
    if ((xm>490*sf and xm<520*sf) and (ym>250*sf and ym<280*sf)):
        background_color=colors.get('cyan')        
    if ((xm>490*sf and xm<520*sf) and (ym>300*sf and ym<330*sf)):
        background_color=colors.get('magenta')        
    if ((xm>490*sf and xm<520*sf) and (ym>350*sf and ym<380*sf)):
        background_color=colors.get('white')
        
    pygame.display.update()
    pygame.time.delay(1)

#instructions screen variables
title=TITLE_FNT.render('MENU',1,'black')
xt=WIDTH/2-title.get_width()/2
Instructions=MENU_FNT.render('Instructions:',1,'Yellow')
inst1=INST_FNT.render('You are a ninja and the shadow cult has taken over your city',1,'white')
inst2=INST_FNT.render('You must stop them and restore order to the ninja guild',1,'white')
inst3=INST_FNT.render('Move left with A, right with D, and jump with SPACE',1,'white')
inst4=INST_FNT.render('1st level is a platformer, 2nd is a runner, 3rd is a bossfight',1,'white')
inst5=INST_FNT.render('Hold [esc] to return to main menu and [e] to return settings.',1,'white')
inst6=INST_FNT.render('Make sure to click the exit button to record your score.',1,'white')

#displaying instructions screen
def instScreen():
    global sf, displayBGimg, background_color
    if displayBGimg:
        screen.blit(menuBackground,(0,0))
    else:
        screen.fill(background_color)
    screen.blit(title,(xt,50*sf))
    screen.blit(Instructions,(200*sf,240*sf))
    screen.blit(inst1,(10*sf,300*sf))
    screen.blit(inst2,(10*sf,350*sf))
    screen.blit(inst3,(10*sf,400*sf))
    screen.blit(inst4,(10*sf,450*sf))
    screen.blit(inst5,(10*sf,500*sf))
    screen.blit(inst6,(10*sf,550*sf))

def keepScore(score):
    global sf
    date=datetime.datetime.now()
    scoreLine=str(score)+' '+name+' '+date.strftime('%m/%d/%Y'+'\n')
    #open a file and write
    #when you write it erases the previous text
    myFile=open('FinalGame\\finalgamescoreboard.txt','a')
    myFile.write(scoreLine)
    myFile.close()

def screensizeChange():
    global HEIGHT, WIDTH, screen, xmUP, ymUP, sf, menuBackground, TITLE_FNT, MENU_FNT, INST_FNT, wb_btn, hb_btn, xs_btn, ys_btn, Instructions, inst1, inst2, inst3, inst4, inst5, inst6, title, xt
    if ((xmUP>90*sf and xmUP<120*sf) and (ymUP>200*sf and ymUP<230*sf)) and ((xmR>90*sf and xmR<120*sf) and (ymR>200*sf and ymR<230*sf)):
        HEIGHT=300
        WIDTH=350
        sf=0.5  
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        menuBackground=pygame.transform.scale(pygame.image.load('FinalGame\city.jpg'),(700*sf,600*sf))
        TITLE_FNT=pygame.font.SysFont('comicsans',int(60*sf))
        MENU_FNT=pygame.font.SysFont('courier',int(40*sf))
        INST_FNT=pygame.font.SysFont('calibri',int(25*sf))
        title=TITLE_FNT.render('MENU',1,'black')
        xt=WIDTH/2-title.get_width()/2
        Instructions=MENU_FNT.render('Instructions:',1,'Yellow')
        inst1=INST_FNT.render('You are a ninja and the shadow cult has taken over your city',1,'white')
        inst2=INST_FNT.render('You must stop them and restore order to the ninja guild',1,'white')
        inst3=INST_FNT.render('Move left with A, right with D, and jump with SPACE',1,'white')
        inst4=INST_FNT.render('1st level is a platformer, 2nd is a runner, 3rd is a bossfight',1,'white')
        inst5=INST_FNT.render('Hold [esc] to return to main menu and [e] to return settings.',1,'white')
        inst6=INST_FNT.render('Make sure to click the exit button to record your score.',1,'white')
        wb_btn=30*sf
        hb_btn=30*sf
        xs_btn=50*sf
        ys_btn=250*sf
        xmUP=0
        ymUP=0
    if ((xmUP>90*sf and xmUP<120*sf) and (ymUP>250*sf and ymUP<280*sf)):
        HEIGHT=600
        WIDTH=700
        sf=1
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        menuBackground=pygame.transform.scale(pygame.image.load('FinalGame\city.jpg'),(700*sf,600*sf))
        TITLE_FNT=pygame.font.SysFont('comicsans',int(60*sf))
        MENU_FNT=pygame.font.SysFont('courier',int(40*sf))
        INST_FNT=pygame.font.SysFont('calibri',int(25*sf))
        title=TITLE_FNT.render('MENU',1,'black')
        xt=WIDTH/2-title.get_width()/2
        Instructions=MENU_FNT.render('Instructions:',1,'Yellow')
        inst1=INST_FNT.render('You are a ninja and the shadow cult has taken over your city',1,'white')
        inst2=INST_FNT.render('You must stop them and restore order to the ninja guild',1,'white')
        inst3=INST_FNT.render('Move left with A, right with D, and jump with SPACE',1,'white')
        inst4=INST_FNT.render('1st level is a platformer, 2nd is a runner, 3rd is a bossfight',1,'white')
        inst5=INST_FNT.render('Hold [esc] to return to main menu and [e] to return settings.',1,'white')
        inst6=INST_FNT.render('Make sure to click the exit button to record your score.',1,'white')
        wb_btn=30*sf
        hb_btn=30*sf
        xs_btn=50*sf
        ys_btn=250*sf
        xmUP=0
        ymUP=0
    if ((xmUP>90*sf and xmUP<120*sf) and (ymUP>300*sf and ymUP<330*sf)):
        HEIGHT=900
        WIDTH=1050
        sf=1.5
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        menuBackground=pygame.transform.scale(pygame.image.load('FinalGame\city.jpg'),(700*sf,600*sf))
        TITLE_FNT=pygame.font.SysFont('comicsans',int(60*sf))
        MENU_FNT=pygame.font.SysFont('courier',int(40*sf))
        INST_FNT=pygame.font.SysFont('calibri',int(25*sf))
        title=TITLE_FNT.render('MENU',1,'black')
        xt=WIDTH/2-title.get_width()/2
        Instructions=MENU_FNT.render('Instructions:',1,'Yellow')
        inst1=INST_FNT.render('You are a ninja and the shadow cult has taken over your city',1,'white')
        inst2=INST_FNT.render('You must stop them and restore order to the ninja guild',1,'white')
        inst3=INST_FNT.render('Move left with A, right with D, and jump with SPACE',1,'white')
        inst4=INST_FNT.render('1st level is a platformer, 2nd is a runner, 3rd is a bossfight',1,'white')
        inst5=INST_FNT.render('Hold [esc] to return to main menu and [e] to return settings.',1,'white')
        inst6=INST_FNT.render('Make sure to click the exit button to record your score.',1,'white')
        wb_btn=30*sf
        hb_btn=30*sf
        xs_btn=50*sf
        ys_btn=250*sf
        xmUP=0
        ymUP=0

def imageSelect():
    global displayBGimg
    if ((xmUP>90*sf and xmUP<120*sf) and (ymUP>200*sf and ymUP<230*sf)) and ((xmR>90*sf and xmR<120*sf) and (ymR>200*sf and ymR<230*sf)):
        displayBGimg=True
    if ((xmUP>90*sf and xmUP<120*sf) and (ymUP>250*sf and ymUP<280*sf)):
        displayBGimg=False

def Level1():
    global sf, GAME, MAIN, LEV_I, playLvl1, playLvl2, playLvl3, lvl1_start_time, lvl1_end_time, lvl1Score, lvl1Success, background_color, displayBGimg
    WIDTH=700*sf
    HEIGHT=600*sf
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    playLvl1=True
    move=10*sf
    jump_move=20*sf
    jumping=False
    Falling=False
    fall_move=0
    GravityCancel=False
    bump=False
    shootProjectile=False
    lvl1Score=0
    lvl1_start_time=time.time()
    Leftchar=False
    Rightchar=True
    WalkCount=0
    clock=pygame.time.Clock()

    #character variables
    char_hb=30*sf
    char_wb=30*sf
    xc=0
    yc=HEIGHT-30*sf
    character=pygame.Rect(xc,yc,char_wb,char_hb)

    #character images
    characterImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightIdle\images\Right-Idles_03.png'),(60*sf,60*sf))
    characterRunLeft=[pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_01.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_02.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_03.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_04.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_05.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_06.png'),(60*sf,60*sf))]
    characterRunRight=[pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_01.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_02.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_03.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_04.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_05.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_06.png'),(60*sf,60*sf))]

    #left hitbox
    char_left_hb=10*sf
    char_left_wb=10*sf
    xc_l=-10*sf
    yc_l=HEIGHT-20*sf
    character_left=pygame.Rect(xc_l,yc_l,char_left_wb,char_left_hb)

    #right hitbox
    char_right_hb=10*sf
    char_right_wb=10*sf
    xc_r=30*sf
    yc_r=HEIGHT-20*sf
    character_right=pygame.Rect(xc_r,yc_r,char_right_wb,char_right_hb)

    #top hitbox
    char_top_hb=10*sf
    char_top_wb=10*sf
    xc_t=10*sf
    yc_t=HEIGHT-40*sf
    character_top=pygame.Rect(xc_t,yc_t,char_top_wb,char_top_hb)

    #bottom hitbox
    char_bottom_hb=10*sf
    char_bottom_wb=10*sf
    xc_b=10*sf
    yc_b=HEIGHT
    character_bottom=pygame.Rect(xc_b,yc_b,char_bottom_wb,char_bottom_hb)

    #enemy1 variables
    enemy1_hb=30*sf
    enemy1_wb=30*sf
    xe1=0
    ye1=370*sf
    enemy1=pygame.Rect(xe1,ye1,enemy1_wb,enemy1_hb)

    enemy1Img=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\images\enemy1_01.png'),(60*sf,60*sf))

    #enemy 2 variables
    enemy2_hb=30*sf
    enemy2_wb=30*sf
    xe2=500*sf
    ye2=70*sf
    enemy2=pygame.Rect(xe2,ye2,enemy2_wb,enemy2_hb)

    enemy2Img=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\enemy2.png'),(60*sf,60*sf))

    #Projectile variables
    proj_hb=10*sf
    proj_wb=10*sf
    xpr=35*sf
    ypr=370*sf
    projectile=pygame.Rect(xpr,ypr,proj_wb,proj_hb)

    projectileImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\images\enemy1_02.png'),(60*sf,60*sf))

    #Portal variables
    portal_hb=60*sf
    portal_wb=30*sf
    xpo=WIDTH-30*sf
    ypo=40*sf
    portal=pygame.Rect(xpo,ypo,portal_wb,portal_hb)

    PortalImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\Portal.png'),(30*sf,60*sf))

    #platforms

    #Platform 1 variables
    plat1_hb=60*sf
    plat1_wb=60*sf
    xpl1=200*sf
    ypl1=HEIGHT-60*sf
    platform1=pygame.Rect(xpl1,ypl1,plat1_wb,plat1_hb)
    plat1_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat1_wb,plat1_hb))

    #Platform 2 variables
    plat2_hb=120*sf
    plat2_wb=60*sf
    xpl2=WIDTH/2
    ypl2=HEIGHT-120*sf
    platform2=pygame.Rect(xpl2,ypl2,plat2_wb,plat2_hb)
    plat2_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat2_wb,plat2_hb))

    #Platform 3 variables
    plat3_hb=60*sf
    plat3_wb=180*sf
    xpl3=WIDTH-180*sf
    ypl3=HEIGHT-200*sf
    platform3=pygame.Rect(xpl3,ypl3,plat3_wb,plat3_hb)
    plat3_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat3_wb,plat3_hb))

    #Platform 4 variables
    plat4_hb=30*sf
    plat4_wb=120*sf
    xpl4=WIDTH-120*sf
    ypl4=HEIGHT/2-5*sf
    platform4=pygame.Rect(xpl4,ypl4,plat4_wb,plat4_hb)
    plat4_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat4_wb,plat4_hb))

    #Platform 5 variables
    plat5_hb=60*sf
    plat5_wb=120*sf
    xpl5=0
    ypl5=HEIGHT-200*sf
    platform5=pygame.Rect(xpl5,ypl5,plat5_wb,plat5_hb)
    plat5_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat5_wb,plat5_hb))

    #Platform 6 variables
    plat6_hb=60*sf
    plat6_wb=450*sf
    xpl6=0
    ypl6=HEIGHT-400*sf
    platform6=pygame.Rect(xpl6,ypl6,plat6_wb,plat6_hb)
    plat6_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat6_wb,plat6_hb))

    #Platform 7 variables
    plat7_hb=20*sf
    plat7_wb=WIDTH/2
    xpl7=WIDTH/2
    ypl7=100*sf
    platform7=pygame.Rect(xpl7,ypl7,plat7_wb,plat7_hb)
    plat7_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat7_wb,plat7_hb))

    platformList=[platform1,platform2,platform3,platform4,platform5,platform6,platform7]

    #background and colors
    colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
    'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
    'white':[255,255,255],'black':[0,0,0]}

    background1=pygame.transform.scale(pygame.image.load('FinalGame\\retrocity.png'),(WIDTH,HEIGHT))
    char_color=colors.get('blue')
    char_side_color=colors.get('cyan')
    enemy_color=colors.get('red')
    proj_color=colors.get('yellow')
    platform_color=colors.get('black')
    portal_color=colors.get('green')

    while playLvl1:
        print(round(time.time()-lvl1_start_time,0),'sec') #start stopwatch
        yc2=character.y+char_hb
        os.system('cls')
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                playLvl1=False
        keys=pygame.key.get_pressed()

        #exiting the game
        if keys[pygame.K_ESCAPE]:
            if GAME:
                lvl1Success=False
                GAME=False
                playLvl1=False
                playLvl2=False
                playLvl3=False
                MAIN=True
            else:
                lvl1Success=False
                LEV_I=False
                playLvl1=False
                MAIN=True
        
        #movement
        if keys[pygame.K_a] and character.x>=move and not platform1.colliderect(character_left) and not platform2.colliderect(character_left) and not platform3.colliderect(character_left) and not platform4.colliderect(character_left) and not platform5.colliderect(character_left) and not platform6.colliderect(character_left) and not platform7.colliderect(character_left):
            Leftchar=True
            Rightchar=False
            character.x-=move
            character_left.x-=move
            character_right.x-=move
            character_top.x-=move
            character_bottom.x-=move
        elif keys[pygame.K_d] and character.x<=WIDTH-(char_wb+move) and not platform1.colliderect(character_right) and not platform2.colliderect(character_right) and not platform3.colliderect(character_right) and not platform4.colliderect(character_right) and not platform5.colliderect(character_right) and not platform6.colliderect(character_right) and not platform7.colliderect(character_right) and not enemy2.colliderect(character_right):
            Leftchar=False
            Rightchar=True
            character.x+=move
            character_left.x+=move
            character_right.x+=move
            character_top.x+=move
            character_bottom.x+=move
        else:
            if Leftchar:
                characterImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftIdle\Left-Idles_03.png'),(60*sf,60*sf))
                Leftchar=False
                WalkCount=0
            if Rightchar:
                characterImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightIdle\images\Right-Idles_03.png'),(60*sf,60*sf))
                Rightchar=False
                WalkCount=0
        
        #running animation
        if WalkCount+1>=18:
            WalkCount=0
        if Leftchar and keys[pygame.K_a]:
            characterImg=(characterRunLeft[WalkCount//3])
            WalkCount+=1
        elif Rightchar and keys[pygame.K_d]:
            characterImg=(characterRunRight[WalkCount//3])
            WalkCount+=1
        
        #activate jumping loop
        if jumping==False and keys[pygame.K_SPACE] and Falling==False and bump==False:
            jumping=True

        #jumping loop
        if jumping:
            character.y-=jump_move
            character_left.y-=jump_move
            character_right.y-=jump_move
            character_top.y-=jump_move
            character_bottom.y-=jump_move
            jump_move-=2*sf
            if jump_move==0 and GravityCancel==False:
                jumping=False
                jump_move=20*sf
                Falling=True
        
        #character bottom collision
        for i in range (len(platformList)):
            if platformList[i].colliderect(character_bottom):
                GravityCancel=True
                Falling=False
                fall_move=0
                jumping=False
                jump_move=20*sf
                character.y=platformList[i].y-31*sf
                character_left.y=platformList[i].y-21*sf
                character_right.y=platformList[i].y-21*sf
                character_top.y=platformList[i].y-41*sf
                character_bottom.y=platformList[i].y-1*sf
                if keys[pygame.K_SPACE]:
                    jumping=True
            else:
                GravityCancel=False
        
        #character top collision
        for i in range (len(platformList)):
            if platformList[i].colliderect(character_top):
                bump=True
                character.y+=char_top_hb
                character_left.y+=char_top_hb
                character_right.y+=char_top_hb
                character_top.y+=char_top_hb
                character_bottom.y+=char_top_hb
                Falling=True
            else:
                bump=False

        #Activate Falling loop
        if jumping==False and character_bottom.y<HEIGHT and GravityCancel==False:
            Falling=True
            
        #Falling loop
        if Falling and GravityCancel==False:
            character.y-=fall_move
            character_left.y-=fall_move
            character_right.y-=fall_move
            character_top.y-=fall_move
            character_bottom.y-=fall_move
            fall_move-=2*sf
            if yc2>HEIGHT:
                Falling=False
                fall_move=0
                character.y=HEIGHT-30*sf
                character_left.y=HEIGHT-20*sf
                character_right.y=HEIGHT-20*sf
                character_top.y=HEIGHT-40*sf
                character_bottom.y=HEIGHT
        
        #shooting and colliding with projectile
        if character.y<=370*sf:
            shootProjectile=True
        if shootProjectile:
            projectile.x+=20*sf
        if projectile.colliderect(character):
            lvl1Success=False
            LEV_I=False
            playLvl1=False
            MAIN=True

        #portal collision
        if character.colliderect(portal):
            lvl1Success=True
            LEV_I=False
            playLvl1=False
            MAIN=True

        #updating screen

        #hitboxes
        for i in range (len(platformList)):
            pygame.draw.rect(screen,platform_color, platformList[i])
        pygame.draw.rect(screen,enemy_color,enemy1,int(3*sf))
        pygame.draw.rect(screen,enemy_color,enemy2,int(3*sf))
        pygame.draw.rect(screen, char_color, character,int(3*sf))
        pygame.draw.rect(screen,char_side_color,character_left)
        pygame.draw.rect(screen,char_side_color,character_right)
        pygame.draw.rect(screen,char_side_color,character_top)
        pygame.draw.rect(screen,char_side_color,character_bottom)
        pygame.draw.rect(screen,proj_color,projectile)
        pygame.draw.rect(screen,portal_color,portal,int(3*sf))
        if displayBGimg:
            screen.blit(background1,(0,0))
        else:
            screen.fill(background_color)
        #displaying images
        screen.blit(enemy2Img,(enemy2.x-15*sf,enemy2.y-15*sf))
        screen.blit(characterImg,(character.x-15*sf,character.y-15*sf))
        screen.blit(enemy1Img,(enemy1.x-15*sf,enemy1.y-15*sf))
        screen.blit(projectileImg,(projectile.x,projectile.y-15*sf))
        screen.blit(PortalImg,(portal.x,portal.y))
        screen.blit(plat1_img,(xpl1,ypl1))
        screen.blit(plat2_img,(xpl2,ypl2))
        screen.blit(plat3_img,(xpl3,ypl3))
        screen.blit(plat4_img,(xpl4,ypl4))
        screen.blit(plat5_img,(xpl5,ypl5))
        screen.blit(plat6_img,(xpl6,ypl6))
        screen.blit(plat7_img,(xpl7,ypl7))
        #framerate
        clock.tick(24)
        pygame.display.update()
    lvl1_end_time=time.time() #end stopwatch
    if lvl1Success:
        #only keep score if you beat the level
        lvl1Score=round(lvl1_end_time-lvl1_start_time,0)
    else:
        lvl1Score=0

def Level2():
    global sf, GAME, MAIN, LEV_II, playLvl1, playLvl2, playLvl3, lvl2Score, lvl2_start_time, lvl2_end_time, background_color, displayBGimg
    WIDTH=700*sf
    HEIGHT=600*sf
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    playLvl2=True
    lvl2_jump_move=20*sf
    jumping=False
    spawnEnemy=1
    lvl2Score=0
    lvl2_start_time=time.time()
    WalkCount=0
    clock=pygame.time.Clock()

    colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
    'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
    'white':[255,255,255],'black':[0,0,0]}
    char_color=colors.get('blue')
    spike_color=colors.get('yellow')
    enemy_color=colors.get('red')
    projectile_color=colors.get('yellow')

    background=pygame.transform.scale(pygame.image.load('FinalGame\9d9980e38b1bc20abdc2285fdd64dd6e.jpg'),(int(204000/149*sf),600*sf))
    xb=0
    xb2=204000/149*sf
    bg_move=5*sf

    spike1=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(30*sf,30*sf))
    xs1=WIDTH+30*sf
    ys1=HEIGHT-100*sf
    s1_hb=30*sf
    s1_wb=30*sf
    spike1_hitbox=pygame.Rect(xs1,ys1,s1_wb,s1_hb)

    spike2=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(20*sf,20*sf))
    xs2=WIDTH+60*sf
    ys2=HEIGHT-90*sf
    s2_hb=20*sf
    s2_wb=20*sf
    spike2_hitbox=pygame.Rect(xs2,ys2,s2_wb,s2_hb)

    spike3=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(40*sf,40*sf))
    xs3=WIDTH+80*sf
    ys3=HEIGHT-110*sf
    s3_hb=40*sf
    s3_wb=40*sf
    spike3_hitbox=pygame.Rect(xs3,ys3,s3_wb,s3_hb)

    #character variables
    char_hb=30*sf
    char_wb=30*sf
    xc=60*sf
    yc=HEIGHT-100*sf
    character=pygame.Rect(xc,yc,char_wb,char_hb)

    #character images
    characterImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightIdle\images\Right-Idles_03.png'),(60*sf,60*sf))
    characterRunRight=[pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_01.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_02.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_03.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_04.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_05.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_06.png'),(60*sf,60*sf))]

    #enemy variables
    enemy_hb=30*sf
    enemy_wb=30*sf
    xe=WIDTH-100*sf
    ye=HEIGHT-100*sf
    enemy=pygame.Rect(xe,ye,enemy_wb,enemy_hb)

    enemyImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\images\minion_02.png'),(60*sf,60*sf))

    #projectile variables
    proj_hb=10*sf
    proj_wb=10*sf
    xp=xe
    yp=ye
    projectile=pygame.Rect(xp,yp,proj_wb,proj_hb)

    projectileImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\images\minion_01.png'),(60*sf,60*sf))

    #smoke images
    smokeAnimationList=[pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\SmokeAnimation\images\\360_F_248020786_msURP2zxewEVN7MpuI4TrBSoLNSESLv5_09.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\SmokeAnimation\images\\360_F_248020786_msURP2zxewEVN7MpuI4TrBSoLNSESLv5_10.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\SmokeAnimation\images\\360_F_248020786_msURP2zxewEVN7MpuI4TrBSoLNSESLv5_11.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\SmokeAnimation\images\\360_F_248020786_msURP2zxewEVN7MpuI4TrBSoLNSESLv5_12.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\SmokeAnimation\images\\360_F_248020786_msURP2zxewEVN7MpuI4TrBSoLNSESLv5_13.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\SmokeAnimation\images\\360_F_248020786_msURP2zxewEVN7MpuI4TrBSoLNSESLv5_14.png'),(60*sf,60*sf))]
    smokeCount=0
    PlaySmoke=False

    while playLvl2:
        print(round(time.time()-lvl2_start_time,0),'sec') #start stopwatch
        #spawining hitboxes
        pygame.draw.rect(screen,spike_color,spike1_hitbox,int(3*sf))
        pygame.draw.rect(screen,spike_color,spike2_hitbox,int(3*sf))
        pygame.draw.rect(screen,spike_color,spike3_hitbox,int(3*sf))
        #moving the background
        spike1_hitbox.x=xs1
        spike2_hitbox.x=xs2
        spike3_hitbox.x=xs3
        xb-=bg_move
        xb2-=bg_move
        xs1-=bg_move
        xs2-=bg_move
        xs3-=bg_move
        if xb<int(204000/149*sf)*-1:
            xb=int(204000/149*sf)
            bg_move+=0.05*sf
        if xb2<int(204000/149*sf)*-1:
            xb2=int(204000/149*sf)
            bg_move+=0.05*sf

        #respawning spikes
        if xs1<-80*sf:
            xs1=WIDTH+30*sf
            if spawnEnemy==1:
                spawnEnemy=random.randint(1,2)
        if xs2<-50*sf:
            xs2=WIDTH+60*sf
        if xs3<-30*sf:
            xs3=WIDTH+80*sf
        
        if enemy.x<-80*sf:
            spawnEnemy=random.randint(0,2)

        #randomized enemy spawn
        if spawnEnemy==1:
            PlaySmoke=False
            enemy.x=WIDTH+30*sf
            projectile.x=enemy.x
            enemyImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\images\minion_02.png'),(60*sf,60*sf))
        if spawnEnemy==2:
            enemy.x-=bg_move
            projectile.x-=bg_move
        
        if projectile.x<WIDTH-30*sf:
            projectile.x-=bg_move*2

        if character.colliderect(projectile):
            LEV_II=False
            playLvl2=False
            MAIN=True
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                playLvl2=False
        
        #enemy collision
        if character.colliderect(enemy):
            PlaySmoke=True
            smokeCount+=1

        if smokeCount+1>=18:
            smokeCount=0
        if PlaySmoke:
            enemyImg=(smokeAnimationList[smokeCount//3])

        keys=pygame.key.get_pressed()
        #exiting the game
        if keys[pygame.K_ESCAPE]:
            if GAME:
                GAME=False
                playLvl1=False
                playLvl2=False
                playLvl3=False
                MAIN=True
            else:
                LEV_II=False
                playLvl2=False
                MAIN=True
        #jumping loop
        if jumping==False and keys[pygame.K_SPACE]:
            jumping = True
        if jumping:
            character.y-=lvl2_jump_move
            lvl2_jump_move-=1*sf
            if lvl2_jump_move<20*sf*-1:
                jumping=False
                lvl2_jump_move=20*sf
                character.y=HEIGHT-100*sf
        
        #displaying walking images
        if WalkCount+1>=18:
            WalkCount=0
        characterImg=(characterRunRight[WalkCount//3])
        WalkCount+=1
        
        #spike collision
        if character.colliderect(spike1_hitbox) or character.colliderect(spike2_hitbox) or character.colliderect(spike3_hitbox):
            LEV_II=False
            playLvl2=False
            MAIN=True
        #spawing hitboxes
        pygame.draw.rect(screen, char_color, character,int(3*sf))
        pygame.draw.rect(screen, projectile_color, projectile)
        pygame.draw.rect(screen, enemy_color, enemy,int(3*sf))
        #display background
        if displayBGimg:
            screen.blit(background,(xb,0))
            screen.blit(background,(xb2,0))
        else:
            screen.fill(background_color)
        #display images
        screen.blit(characterImg,(character.x-15*sf,character.y-15*sf))
        if character.x<=enemy.x+enemy_wb:
            screen.blit(enemyImg,(enemy.x,enemy.y))
        screen.blit(projectileImg,(projectile.x-15*sf,projectile.y-15*sf))
        screen.blit(spike1,(xs1,ys1))
        screen.blit(spike2,(xs2,ys2))
        screen.blit(spike3,(xs3,ys3))
        clock.tick(42)
        pygame.display.update()
    lvl2_end_time=time.time() #end stopwatch
    lvl2Score=round(lvl2_end_time-lvl2_start_time,0) #scoring

def Level3():
    global sf, GAME, MAIN, LEV_III, playLvl1, playLvl2, playLvl3, lvl3Score, lvl3_start_time, lvl3Success, lvl3_end_time, background_color, displayBGimg
    WIDTH=700*sf
    HEIGHT=600*sf
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    playLvl3=True
    move=10*sf
    jumping=False
    jump_move=20*sf
    full_health=True
    medium_health=False
    low_health=False
    bossLeft=False
    bossRight=False
    bossMove=True
    bossReturnLeft=False
    bossReturnRight=False
    projectilesOn=False
    projectilesActive=False
    projectilesLeft=False
    projectilesRight=False
    lvl3Score=0
    lvl3_start_time=time.time()
    Leftchar=False
    Rightchar=True
    WalkCount=0
    clock=pygame.time.Clock()

    bossNewPos=0

    colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
    'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
    'white':[255,255,255],'black':[0,0,0]}

    BOSS_FNT=pygame.font.SysFont('courier',int(40*sf))
    Health_title=BOSS_FNT.render('Boss Health',1*sf,'black')
    xt=WIDTH/2-Health_title.get_width()/2

    char_color=colors.get('blue')
    char_side_color=colors.get('cyan')
    boss_color=colors.get('red')
    projectile_color1=colors.get('purple')
    projectile_color2=colors.get('magenta')
    projectile_color3=colors.get('cyan')
    health_color3=colors.get('green')
    health_color2=colors.get('yellow')
    health_color1=colors.get('red')
    health_gone=colors.get('black')

    #character variables
    char_hb=30*sf
    char_wb=30*sf
    xc=60*sf
    yc=HEIGHT-80*sf
    character=pygame.Rect(xc,yc,char_wb,char_hb)

    characterImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightIdle\images\Right-Idles_03.png'),(60*sf,60*sf))
    characterRunLeft=[pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_01.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_02.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_03.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_04.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_05.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftMove\images\\runleft_06.png'),(60*sf,60*sf))]
    characterRunRight=[pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_01.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_02.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_03.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_04.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_05.png'),(60*sf,60*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightMove\images\characterRunRight_06.png'),(60*sf,60*sf))]

    DragonImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonLeftIdle\DragonLeftIdle.png'),(120*sf,120*sf))
    DragonRunLeft=[pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonLeftMove\images\DragonRunLeft_02.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonLeftMove\images\DragonRunLeft_03.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonLeftMove\images\DragonRunLeft_04.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonLeftMove\images\DragonRunLeft_05.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonLeftMove\images\DragonRunLeft_06.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonLeftMove\images\DragonRunLeft_07.png'),(120*sf,120*sf))]
    DragonRunRight=[pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonRightMove\DragonRunLeft_02.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonRightMove\DragonRunLeft_03.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonRightMove\DragonRunLeft_04.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonRightMove\DragonRunLeft_05.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonRightMove\DragonRunLeft_06.png'),(120*sf,120*sf)),pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonRightMove\DragonRunLeft_07.png'),(120*sf,120*sf))]
    DragonWalkCount=0

    #left hitbox
    char_left_hb=10*sf
    char_left_wb=10*sf
    xc_l=50*sf
    yc_l=HEIGHT-70*sf
    character_left=pygame.Rect(xc_l,yc_l,char_left_wb,char_left_hb)

    #right hitbox
    char_right_hb=10*sf
    char_right_wb=10*sf
    xc_r=90*sf
    yc_r=HEIGHT-70*sf
    character_right=pygame.Rect(xc_r,yc_r,char_right_wb,char_right_hb)

    #bottom hitbox
    char_bottom_hb=10*sf
    char_bottom_wb=10*sf
    xc_b=70*sf
    yc_b=HEIGHT-50*sf
    character_bottom=pygame.Rect(xc_b,yc_b,char_bottom_wb,char_bottom_hb)

    #boss variables
    boss_hb=60*sf
    boss_wb=60*sf
    xb=WIDTH/2-boss_wb/2
    yb=HEIGHT-110*sf
    boss=pygame.Rect(xb,yb,boss_wb,boss_hb)

    bossPhase=random.randint(1,2)

    #boss health bar variables

    #boss health point 1
    hp1_hb=30*sf
    hp1_wb=30*sf
    xhp1=290*sf
    yhp1=120*sf
    healthPoint1=pygame.Rect(xhp1,yhp1,hp1_wb,hp1_hb)
    #boss health point 2
    hp2_hb=30*sf
    hp2_wb=30*sf
    xhp2=330*sf
    yhp2=120*sf
    healthPoint2=pygame.Rect(xhp2,yhp2,hp2_wb,hp2_hb)
    #boss health point 3
    hp3_hb=30*sf
    hp3_wb=30*sf
    xhp3=370*sf
    yhp3=120*sf
    healthPoint3=pygame.Rect(xhp3,yhp3,hp3_wb,hp3_hb)

    #projectile variables

    #projectile 1
    proj1_hb=20*sf
    proj1_wb=20*sf
    xp1=xb-proj1_wb
    yp1=yb+20*sf
    projectile1=pygame.Rect(xp1,yp1,proj1_wb,proj1_hb)
    #projectile 2
    proj2_hb=20*sf
    proj2_wb=20*sf
    xp2=xb-proj2_wb
    yp2=yb+20*sf
    projectile2=pygame.Rect(xp2,yp2,proj2_wb,proj2_hb)
    #projectile 3
    proj3_hb=20*sf
    proj3_wb=20*sf
    xp3=xb-proj3_wb
    yp3=yb+20*sf
    projectile3=pygame.Rect(xp3,yp3,proj3_wb,proj3_hb)

    fireballImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\Fireball.png'),(50*sf,30*sf))

    background=pygame.transform.scale(pygame.image.load('FinalGame\Map_DemonIsland.png'),(1920*sf,1080*sf))
    xbg=-615*sf
    ybg=-200*sf

    while playLvl3:
        print(round(time.time()-lvl3_start_time,0),'sec') #start stopwatch
        os.system('cls')
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                playLvl3=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if GAME:
                GAME=False
                playLvl1=False
                playLvl2=False
                playLvl3=False
                MAIN=True
            else:
                LEV_III=False
                playLvl3=False
                MAIN=True
        if keys[pygame.K_a] and character.x>=move:
            Leftchar=True
            Rightchar=False
            character.x-=move
            character_left.x-=move
            character_right.x-=move
            character_bottom.x-=move
        elif keys[pygame.K_d] and character.x<=WIDTH-(char_wb+move):
            Leftchar=False
            Rightchar=True
            character.x+=move
            character_left.x+=move
            character_right.x+=move
            character_bottom.x+=move
        else:
            if Leftchar:
                characterImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterLeftIdle\Left-Idles_03.png'),(60*sf,60*sf))
                Leftchar=False
                WalkCount=0
            elif Rightchar:
                characterImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\characterRightIdle\images\Right-Idles_03.png'),(60*sf,60*sf))
                Rightchar=False
                WalkCount=0
        
        if WalkCount+1>=18:
            WalkCount=0
        if Leftchar and keys[pygame.K_a]:
            characterImg=(characterRunLeft[WalkCount//3])
            WalkCount+=1
        if Rightchar and keys[pygame.K_d]:
            characterImg=(characterRunRight[WalkCount//3])
            WalkCount+=1
        
        if DragonWalkCount+1>=18:
            DragonWalkCount=0

        if jumping==False and keys[pygame.K_SPACE]:
            jumping=True

        if jumping:
            character.y-=jump_move
            character_left.y-=jump_move
            character_right.y-=jump_move
            character_bottom.y-=jump_move
            jump_move-=2*sf
            if jump_move<-20*sf:
                jumping=False
                jump_move=20*sf
        
        if bossPhase==1:
            bossMove=True
            if bossMove:
                if character.x<boss.x:
                    bossLeft=True
                    bossRight=False
                    bossPhase=0
                if character.x>boss.x:
                    bossRight=True
                    bossLeft=False
                    bossPhase=0
        
        if bossPhase==2:
            if boss.x>WIDTH/2-boss_wb/2:
                bossReturnLeft=False
                bossReturnRight=True
            if boss.x<WIDTH/2-boss_wb/2:
                bossReturnRight=False
                bossReturnLeft=True
            if bossLeft:
                bossLeft=False
                bossReturnLeft=True
            if bossRight:
                bossRight=False
                bossReturnRight=True
            if bossReturnLeft:
                boss.x+=move
                DragonImg=(DragonRunRight[DragonWalkCount//3])
                DragonWalkCount+=1
            if bossReturnRight:
                boss.x-=move
                DragonImg=(DragonRunLeft[DragonWalkCount//3])
                DragonWalkCount+=1
            if boss.x==WIDTH/2-boss_wb/2:
                bossReturnLeft=False
                bossReturnRight=False
                projectilesOn=True
                bossPhase=0
        
        if bossPhase==0 and projectilesOn and boss.x==WIDTH/2-boss_wb/2:
            if character.x<boss.x:
                fireballImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\Fireball.png'),(50*sf,30*sf))
                DragonImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonLeftIdle\DragonLeftIdle.png'),(120*sf,120*sf))
            if character.x>boss.x:
                fireballImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\FireballRight.png'),(50*sf,30*sf))
                DragonImg=DragonImg=pygame.transform.scale(pygame.image.load('FinalGame\Sprites\SpriteSheets\DragonRightIdle\DragonRightIdle.png'),(120*sf,120*sf))

        if projectilesOn:
            if character.x<boss.x:
                projectile1.x=xb-proj1_wb
                projectile2.x=xb-proj2_wb
                projectile3.x=xb-proj3_wb
                projectilesLeft=True
            if character.x>boss.x:
                projectile1.x=xb+boss_wb
                projectile2.x=xb+boss_wb
                projectile3.x=xb+boss_wb
                projectilesRight=True
            projectilesActive=True
            projectilesOn=False

        if projectilesActive:
            if projectilesLeft:
                projectile1.x-=move
                if projectile1.x+proj1_wb<0:
                    projectile2.x-=move
                if projectile2.x+proj2_wb<0:
                    projectile3.x-=move
                if projectile3.x+proj3_wb<0:
                    projectilesLeft=False
                    projectilesActive=False
                    bossPhase=random.randint(1,2)
            if projectilesRight:
                projectile1.x+=move
                if projectile1.x-proj1_wb>WIDTH:
                    projectile2.x+=move
                if projectile2.x-proj2_wb>WIDTH:
                    projectile3.x+=move
                if projectile3.x-proj3_wb>WIDTH:
                    projectilesRight=False
                    projectilesActive=False
                    bossPhase=random.randint(1,2)

        if bossLeft:
            boss.x-=move
            DragonImg=(DragonRunLeft[DragonWalkCount//3])
            DragonWalkCount+=1
            if boss.x<=0:
                bossPhase=random.randint(1,2)
        if bossRight:
            boss.x+=move
            DragonImg=(DragonRunRight[DragonWalkCount//3])
            DragonWalkCount+=1
            if boss.x+boss_wb>=WIDTH:
                bossPhase=random.randint(1,2)

        if bossNewPos==1:
            boss.x=boss_wb
            bossPhase=random.randint(1,2)
            bossNewPos=0
        if bossNewPos==2:
            boss.x=WIDTH-boss_wb*2
            bossPhase=random.randint(1,2)
            bossNewPos=0

        if character_left.colliderect(boss) or character_right.colliderect(boss):
            if GAME:
                lvl3Success=False
                playLvl3=False
                GAME=False
                MAIN=True
            else:
                lvl3Success=False
                playLvl3=False
                LEV_III=False
                MAIN=True
        if projectilesOn or projectilesActive:
            if character.colliderect(projectile1) or character.colliderect(projectile2) or character.colliderect(projectile3):
                if GAME:
                    lvl3Success=False
                    playLvl3=False
                    GAME=False
                    MAIN=True
                else:
                    lvl3Success=False
                    playLvl3=False
                    LEV_III=False
                    MAIN=True
        
        if character_bottom.colliderect(boss) and full_health==True:
            full_health=False
            medium_health=True
            bossPhase=0
            bossLeft=False
            bossRight=False
            bossReturnLeft=False
            bossReturnRight=False
            projectilesActive=False
            projectilesOn=False
            projectilesLeft=False
            projectilesRight=False
            if boss.x==WIDTH/2-boss_wb/2:
                bossNewPos=random.randint(1,2)
            else:
                if boss.x>WIDTH/2-boss_wb/2:
                    bossNewPos=1
                if boss.x<WIDTH/2-boss_wb/2:
                    bossNewPos=2
            if bossNewPos==1:
                boss.x=0+boss_wb
                bossPhase=random.randint(1,2)
                bossNewPos=0
            if bossNewPos==2:
                boss.x=WIDTH-boss_wb*2
                bossPhase=random.randint(1,2)
                bossNewPos=0
        if character_bottom.colliderect(boss) and medium_health==True:
            medium_health=False
            low_health=True
            bossPhase=0
            bossLeft=False
            bossRight=False
            bossReturnLeft=False
            bossReturnRight=False
            if boss.x==WIDTH/2-boss_wb/2:
                bossNewPos=random.randint(1,2)
            else:
                if boss.x>WIDTH/2-boss_wb/2:
                    bossNewPos=1
                if boss.x<WIDTH/2-boss_wb/2:
                    bossNewPos=2
            if bossNewPos==1:
                boss.x=boss_wb
                bossPhase=random.randint(1,2)
                bossNewPos=0
            if bossNewPos==2:
                boss.x=WIDTH-boss_wb*2
                bossPhase=random.randint(1,2)
                bossNewPos=0

        if character_bottom.colliderect(boss) and low_health==True:
            if GAME:
                lvl3Success=True
                playLvl3=False
                GAME=False
                MAIN=True
            else:
                lvl3Success=True
                playLvl3=False
                LEV_III=False
                MAIN=True
        pygame.draw.rect(screen,char_color,character,int(3*sf))
        pygame.draw.rect(screen,char_side_color,character_left)
        pygame.draw.rect(screen,char_side_color,character_right)
        pygame.draw.rect(screen,char_side_color,character_bottom)
        pygame.draw.rect(screen,boss_color,boss,int(3*sf))
        if projectilesOn or projectilesActive:
            pygame.draw.rect(screen,projectile_color1,projectile1)
            pygame.draw.rect(screen,projectile_color2,projectile2)
            pygame.draw.rect(screen,projectile_color3,projectile3)
        if displayBGimg:
            screen.blit(background,(xbg,ybg))
        else:
            screen.fill(background_color)
        screen.blit(Health_title,(xt,50*sf))
        screen.blit(characterImg,(character.x-15*sf,character.y-15*sf))
        screen.blit(DragonImg,(boss.x-30*sf,boss.y-30*sf))
        if full_health:
            pygame.draw.rect(screen,health_color3,healthPoint1)
            pygame.draw.rect(screen,health_color3,healthPoint2)
            pygame.draw.rect(screen,health_color3,healthPoint3)
        if medium_health:
            pygame.draw.rect(screen,health_color2,healthPoint1)
            pygame.draw.rect(screen,health_color2,healthPoint2)
            pygame.draw.rect(screen,health_gone,healthPoint3)
        if low_health:
            pygame.draw.rect(screen,health_color1,healthPoint1)
            pygame.draw.rect(screen,health_gone,healthPoint2)
            pygame.draw.rect(screen,health_gone,healthPoint3)
        if projectilesOn or projectilesActive:
            screen.blit(fireballImg,(projectile1.x-15*sf,projectile1.y-15*sf))
            screen.blit(fireballImg,(projectile2.x-15*sf,projectile2.y-15*sf))
            screen.blit(fireballImg,(projectile3.x-15*sf,projectile3.y-15*sf))
        clock.tick(24)
        pygame.display.update()
    lvl3_end_time=time.time()
    if lvl3Success:
        lvl3Score=round(lvl3_end_time-lvl3_start_time,0)
    else:
        lvl3Score=0

def Game():
    Level1()
    Level2()
    Level3()

while check:
    if MAIN:
        print(lvl1Score, lvl2Score, lvl3Score)
        pygame.mouse.set_visible(True)
        pygame.display.set_caption('Menu')
        if displayBGimg:
            screen.blit(menuBackground,(0,0))
        else:
            screen.fill(background_color)
        TitleMenu("Fallen Shinobi")
        MainMenu(MenuList,0)
    if GAME:
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        pygame.mouse.set_visible(False)
        pygame.display.set_caption('Fallen Shinobi')
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
        MainMenu(ScreenSizeList,40*sf)
        screensizeChange()
        if keys[pygame.K_e]:
            SC_SIZE=False
            SETT=True
        if keys[pygame.K_ESCAPE]:
            SC_SIZE=False
            MAIN=True
    if BACKGROUNDCOLOR:
        pygame.display.set_caption('Background Color')
        TitleMenu("BACKGROUND COLOR")
        ColorMenu()
        if keys[pygame.K_e]:
            BACKGROUNDCOLOR=False
            SETT=True
        if keys[pygame.K_ESCAPE]:
            BACKGROUNDCOLOR=False
            MAIN=True
    if BACKGROUNDIMGS:
        pygame.display.set_caption('Background IMAGES')
        TitleMenu("BACKGROUND IMAGES")
        MainMenu(bgimgsList,40*sf)
        imageSelect()
        if keys[pygame.K_e]:
            BACKGROUNDIMGS=False
            SETT=True
        if keys[pygame.K_ESCAPE]:
            BACKGROUNDIMGS=False
            MAIN=True
    if LEV_I:
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        pygame.display.set_caption('Fallen Shinobi: Level 1')
        Level1()
        if keys[pygame.K_ESCAPE]:
            playLvl1=False
            LEV_I=False
            MAIN=True
    if LEV_II:
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        pygame.display.set_caption('Fallen Shinobi: Level 2')
        Level2()
        if keys[pygame.K_ESCAPE]:
            playLvl2=False
            LEV_II=False
            MAIN=True
    if LEV_III:
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos((WIDTH/2,HEIGHT/2))
        pygame.display.set_caption('Fallen Shinobi: Level 3')
        Level3()
        if keys[pygame.K_ESCAPE]:
            playLvl3=False
            LEV_III=False
            MAIN=True
    if SCOREBOARD:
        pygame.display.set_caption('Scoreboard')
        TitleMenu("SCOREBOARD")
        myFile=open('FinalGame\\finalgamescoreboard.txt','r')
        scoreboardLines=myFile.readlines()
        textY=250*sf
        for i in range(len(scoreboardLines)):
            newScoreLine=MENU_FNT.render(scoreboardLines[i],1,'white')
            textX=WIDTH/2-newScoreLine.get_width()/2
            screen.blit(newScoreLine,(textX,textY))
            textY+=50*sf
        pygame.display.update()
        if keys[pygame.K_ESCAPE]:
            SCOREBOARD=False
            MAIN=True
    if EXIT:
        TitleMenu("Game Over")
        if lvl1Score>0 and lvl2Score>0 and lvl3Score>0:
            gameScore=lvl2Score-lvl1Score-lvl3Score
            keepScore(gameScore)
        check=False

    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    mouse_posR=pygame.mouse.get_pos()
    xmR=mouse_posR[0]
    ymR=mouse_posR[1]
    # print(xmR,ymR)
    if case.type==pygame.MOUSEBUTTONUP:
        mouse_posUP=pygame.mouse.get_pos()
        xmUP=mouse_posUP[0]
        ymUP=mouse_posUP[1]
        if SETT:
            pygame.display.set_caption('Settings')
            TitleMenu("SETTINGS")
            MainMenu(SettingList,0)
            if keys[pygame.K_ESCAPE]:
                SETT=False
                MAIN=True
        if MAIN and ((xmUP >50*sf and xmUP <80*sf) and (ymUP >300*sf and ymUP <330*sf))or SETT :
            MAIN=False
            SETT=True
        
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        xm=mouse_pos[0]
        ym=mouse_pos[1]
        if MAIN and ((xm >50*sf and xm <80*sf) and (ym >200*sf and ym <230*sf))or GAME:
            MAIN=False
            GAME=True
        if MAIN and ((xm >50*sf and xm <80*sf) and (ym >250*sf and ym <280*sf))or INST :
            MAIN=False
            INST=True
        if MAIN and ((xm >50*sf and xm <80*sf) and (ym >350*sf and ym <380*sf))or LEV_I :
            MAIN=False
            LEV_I=True
        if MAIN and ((xm >50*sf and xm <80*sf) and (ym >400*sf and ym <430*sf))or LEV_II :
            MAIN=False
            LEV_II=True
        if MAIN and ((xm >50*sf and xm <80*sf) and (ym >450*sf and ym <480*sf))or LEV_III :
            MAIN=False
            LEV_III=True
        if MAIN and ((xm >50*sf and xm <80*sf) and (ym >500*sf and ym <530*sf))or SCOREBOARD :
            MAIN=False
            SCOREBOARD=True
        if MAIN and ((xm >50*sf and xm <80*sf) and (ym >550*sf and ym <580*sf))or EXIT :
            MAIN=False
            EXIT=True
        #settings menu
        if SETT and ((xm >50*sf and xm <80*sf) and (ym >200*sf and ym <230*sf)):
            SETT=False
            SC_SIZE=True
        if SETT and ((xm >50*sf and xm <80*sf) and (ym >250*sf and ym <280*sf)):
            SETT=False
            BACKGROUNDIMGS=True
        if SETT and ((xm >50*sf and xm <80*sf) and (ym >300*sf and ym <330*sf)):
            SETT=False
            BACKGROUNDCOLOR=True
    pygame.display.update()
    pygame.time.delay(1)
