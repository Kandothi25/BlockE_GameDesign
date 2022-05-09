#Ishaan Kandoth
#4/21/22
#Level 2 of Final Game
import os, pygame, random
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
char_color=colors.get('blue')
spike_color=colors.get('yellow')

background=pygame.transform.scale(pygame.image.load('FinalGame\9d9980e38b1bc20abdc2285fdd64dd6e.jpg'),(int(204000/149),600))
xb=0
xb2=204000/149
bg_move=5

spike1=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(30,30))
xs1=WIDTH+30
ys1=HEIGHT-100
s1_hb=30
s1_wb=30
spike1_hitbox=pygame.Rect(xs1,ys1,s1_wb,s1_hb)

spike2=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(20,20))
xs2=WIDTH+60
ys2=HEIGHT-100+10
s2_hb=20
s2_wb=20
spike2_hitbox=pygame.Rect(xs2,ys2,s2_wb,s2_hb)

spike3=pygame.transform.scale(pygame.image.load('FinalGame\Spike.png'),(40,40))
xs3=WIDTH+80
ys3=HEIGHT-100-10
s3_hb=40
s3_wb=40
spike3_hitbox=pygame.Rect(xs3,ys3,s3_wb,s3_hb)

#character variables
char_hb=30
char_wb=30
xc=60
yc=HEIGHT-100
character=pygame.Rect(xc,yc,char_wb,char_hb)

#enemy variables
enemy_hb=30
enemy_wb=30
xe=0
ye=370
enemy1=pygame.Rect(xe,ye,enemy_wb,enemy_hb)

while playLvl2:
    pygame.draw.rect(screen,spike_color,spike1_hitbox,3)
    pygame.draw.rect(screen,spike_color,spike2_hitbox,3)
    pygame.draw.rect(screen,spike_color,spike3_hitbox,3)
    screen.blit(background,(xb,0))
    screen.blit(background,(xb2,0))
    spike1_hitbox.x=xs1
    spike2_hitbox.x=xs2
    spike3_hitbox.x=xs3
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
    if character.colliderect(spike1_hitbox) or character.colliderect(spike2_hitbox) or character.colliderect(spike3_hitbox):
        playLvl2=False
    pygame.draw.rect(screen, char_color, character,3)
    screen.blit(spike1,(xs1,ys1))
    screen.blit(spike2,(xs2,ys2))
    screen.blit(spike3,(xs3,ys3))
    pygame.time.delay(20)
    pygame.display.update()