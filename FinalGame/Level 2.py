#Ishaan Kandoth
#4/21/22
#Level 2 of Final Game
import os, pygame
os.system('cls')
pygame.init()
WIDTH=700
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
playLvl2=True
lvl2_jump_move=20
jumping=False

colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
'white':[255,255,255],'black':[0,0,0]}

background=pygame.transform.scale(pygame.image.load('FinalGame\9d9980e38b1bc20abdc2285fdd64dd6e.jpg'),(int(204000/149),600))
xb=0
xb2=204000/149
bg_move=5

spike1=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(30,30))
xs1=WIDTH+30
ys1=HEIGHT-100

spike2=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(20,20))
xs2=WIDTH+60
ys2=HEIGHT-100+10

spike3=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(40,40))
xs3=WIDTH+80
ys3=HEIGHT-100-10

#character variables
char_hb=30
char_wb=30
xc=60
yc=HEIGHT-100
character=pygame.Rect(xc,yc,char_wb,char_hb)
char_color=colors.get('blue')

while playLvl2:
    screen.blit(background,(xb,0))
    screen.blit(background,(xb2,0))
    xb-=bg_move
    xb2-=bg_move
    xs1-=bg_move
    xs2-=bg_move
    xs3-=bg_move
    if xb<int(204000/149)*-1:
        xb=int(204000/149)
        bg_move+=0.05
    if xb2<int(204000/149)*-1:
        xb2=int(204000/149)
        bg_move+=0.05

    if xs1<-80:
        xs1=WIDTH+30
    if xs2<-50:
        xs2=WIDTH+60
    if xs3<-30:
        xs3=WIDTH+80
    
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            playLvl2=False
    keys=pygame.key.get_pressed()
    if jumping==False and keys[pygame.K_SPACE]:
        jumping = True
    if jumping:
        character.y-=lvl2_jump_move
        lvl2_jump_move-=1
        if lvl2_jump_move< -20 and yc-char_hb<HEIGHT:
            jumping=False
            lvl2_jump_move=20
    pygame.draw.rect(screen, char_color, character,3)
    screen.blit(spike1,(xs1,ys1))
    screen.blit(spike2,(xs2,ys2))
    screen.blit(spike3,(xs3,ys3))
    pygame.time.delay(20)
    pygame.display.update()