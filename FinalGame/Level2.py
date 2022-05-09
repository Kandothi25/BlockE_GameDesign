#Ishaan Kandoth
#4/21/22
#Level 2 of Final Game
import os, pygame, random
os.system('cls')
pygame.init()
sf=0.5
WIDTH=700*sf
HEIGHT=600*sf
screen=pygame.display.set_mode((WIDTH,HEIGHT))
playLvl2=True
lvl2_jump_move=20*sf
jumping=False

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

#left hitbox
char_left_hb=10*sf
char_left_wb=10*sf
xc_l=-10*sf
yc_l=HEIGHT-20*sf
character_left=pygame.Rect(xc_l,yc_l,char_left_wb,char_left_hb)

#bottom hitbox
char_bottom_hb=10*sf
char_bottom_wb=10*sf
xc_b=10*sf
yc_b=HEIGHT
character_bottom=pygame.Rect(xc_b,yc_b,char_bottom_wb,char_bottom_hb)

#enemy variables
enemy_hb=30*sf
enemy_wb=30*sf
xe=WIDTH-100*sf
ye=HEIGHT-100*sf
enemy=pygame.Rect(xe,ye,enemy_wb,enemy_hb)

#projectile variables
proj_hb=10*sf
proj_wb=10*sf
xp=xe-enemy_wb
yp=ye+10*sf
projectile=pygame.Rect(xp,yp,proj_wb,proj_hb)

while playLvl2:
    print(WIDTH,HEIGHT)
    pygame.draw.rect(screen,spike_color,spike1_hitbox,int(3*sf))
    pygame.draw.rect(screen,spike_color,spike2_hitbox,int(3*sf))
    pygame.draw.rect(screen,spike_color,spike3_hitbox,int(3*sf))
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
    if xb<int(204000/149*sf)*-1:
        xb=int(204000/149*sf)
        bg_move+=0.05*sf
    if xb2<int(204000/149*sf)*-1:
        xb2=int(204000/149*sf)
        bg_move+=0.05*sf

    if xs1<-80*sf:
        xs1=WIDTH+30*sf
    if xs2<-50*sf:
        xs2=WIDTH+60*sf
    if xs3<-30*sf:
        xs3=WIDTH+80*sf
    
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            playLvl2=False
    keys=pygame.key.get_pressed()
    if jumping==False and keys[pygame.K_SPACE]:
        jumping = True
    if jumping:
        character.y-=lvl2_jump_move
        lvl2_jump_move-=1*sf
        if lvl2_jump_move<20*sf*-1:
            jumping=False
            lvl2_jump_move=20*sf
            character.y=HEIGHT-100*sf
    if character.colliderect(spike1_hitbox) or character.colliderect(spike2_hitbox) or character.colliderect(spike3_hitbox):
        playLvl2=False
    pygame.draw.rect(screen, char_color, character,int(3*sf))
    screen.blit(spike1,(xs1,ys1))
    screen.blit(spike2,(xs2,ys2))
    screen.blit(spike3,(xs3,ys3))
    pygame.time.delay(20)
    pygame.display.update()
