#Ishaan Kandoth
#4/18/22
#Final Game
import os, pygame, datetime
os.system('cls')
name=input('Enter your username: ')
pygame.init()
WIDTH=700
HEIGHT=600
check=True #for the while loop
playGame=True #for the game loop
move=10
jump_move=10
jumping=False
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
MOVEMENT=False

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Final Game')

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

colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
'white':[255,255,255],'black':[0,0,0]}

background=pygame.transform.scale(pygame.image.load('FinalGame\city.jpg'),(700,600))
hb_color=colors.get('white')
sq_btn_color=colors.get('cyan')

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
    screen.fill(background)
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
