#Ishaan Kandoth
#3/23/22
import os, pygame, time, random
os.system('cls')
pygame.init()
#Main menu for the game
#Creating functions for the menu

#Variables
WIDTH=700
HEIGHT=700
wb_btn=30
hb_btn=30
xs_btn=50
ys_btn=250

#Lists
MenuList=['Instruction','Setting','Level 1','Level 2','Level 3','Scoreboard','Exit']


#screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#Colors
colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'cyan':[0,255,255],'purple':[128,0,128],'magenta':[255,0,255],
'black':[0,0,0],'white':[255,255,255]}
background=colors.get('black')
cr_color=colors.get('white')
hb_color=colors.get('white')
sq_btn_color=colors.get('cyan')

#Fonts
TITLE_FNT=pygame.font.SysFont('comicsans',80)
MENU_FNT=pygame.font.SysFont('courier',40)
INST_FNT=pygame.font.SysFont('calibri',25)

#Text
text=TITLE_FNT.render('MENU',1,'green')
screen.fill('black')
#get width of text
#x value = WIDTH/2-Wtext/2
xt=WIDTH/2-text.get_width()/2
screen.blit(text,(xt,50))

#Create first button


#create square
square_button=pygame.Rect(xs_btn,ys_btn,wb_btn,hb_btn)
ty=250
for i in range(7):
    message=MenuList[i]
    text=INST_FNT.render(message,1,'green')
    screen.blit(text,(90,ty))
    pygame.draw.rect(screen,sq_btn_color,square_button)
    square_button.y+=50
    ty+=50
pygame.display.update()
pygame.time.delay(999)