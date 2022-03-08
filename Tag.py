#Ishaan Kandoth
#3/8/22
#draw circles and rectangles
#use keys to move objects
#use dictionaries
import os, time, random, pygame
from turtle import circle
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

#creating screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tag')

#define colors
colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'cyan':[0,255,255],'purple':[128,0,128],'magenta':[255,0,255],
'black':[0,0,0],'white':[255,255,255]}

#Get colors
background=colors.get('black')
sq_color=colors.get('red')
cr_color=colors.get('blue')

while check:
    screen.fill(background)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_LEFT] and square.x>=move:
        square.x-=move
    if keys[pygame.K_RIGHT] and square.x<=WIDTH-hbox:
        square.x+=move
    if keys[pygame.K_UP] and square.y>=move:
        square.y-=move
    if keys[pygame.K_DOWN] and square.y<=HEIGHT-wbox:
        square.y+=move
    
    if keys[pygame.K_a] and xc>=rad:
        xc-=move
    if keys[pygame.K_d] and xc<=WIDTH-rad:
        xc+=move
    if keys[pygame.K_w] and yc>=rad:
        yc-=move
    if keys[pygame.K_s] and yc<=HEIGHT-rad:
        yc+=move
#Finish circle
    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)
    pygame.display.update()
    pygame.time.delay(1)
