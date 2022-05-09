#Ishaan Kandoth
#5/8/22
import os, pygame, random
os.system('cls')
pygame.init()
WIDTH=700
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
playLvl3=True
move=10
jumping=False
jump_move=20
full_health=True
medium_health=False
low_health=False

colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
'white':[255,255,255],'black':[0,0,0]}

BOSS_FNT=pygame.font.SysFont('courier',40)
Health_title=BOSS_FNT.render('Boss Health',1,'black')
xt=WIDTH/2-Health_title.get_width()/2

char_color=colors.get('blue')
char_side_color=colors.get('cyan')
boss_color=colors.get('red')
projectile_color=colors.get('yellow')
health_color3=colors.get('green')
health_color2=colors.get('yellow')
health_color1=colors.get('red')
health_gone=colors.get('black')

#character variables
char_hb=30
char_wb=30
xc=60
yc=HEIGHT-80
character=pygame.Rect(xc,yc,char_wb,char_hb)

#left hitbox
char_left_hb=10
char_left_wb=10
xc_l=50
yc_l=HEIGHT-70
character_left=pygame.Rect(xc_l,yc_l,char_left_wb,char_left_hb)

#right hitbox
char_right_hb=10
char_right_wb=10
xc_r=90
yc_r=HEIGHT-70
character_right=pygame.Rect(xc_r,yc_r,char_right_wb,char_right_hb)

#bottom hitbox
char_bottom_hb=10
char_bottom_wb=10
xc_b=70
yc_b=HEIGHT-50
character_bottom=pygame.Rect(xc_b,yc_b,char_bottom_wb,char_bottom_hb)

#boss variables
boss_hb=60
boss_wb=60
xb=WIDTH/2
yb=HEIGHT-110
boss=pygame.Rect(xb,yb,boss_wb,boss_hb)

#boss health bar variables

#boss health point 1
hp1_hb=30
hp1_wb=30
xhp1=290
yhp1=120
healthPoint1=pygame.Rect(xhp1,yhp1,hp1_wb,hp1_hb)
#boss health point 2
hp2_hb=30
hp2_wb=30
xhp2=330
yhp2=120
healthPoint2=pygame.Rect(xhp2,yhp2,hp2_wb,hp2_hb)
#boss health point 3
hp3_hb=30
hp3_wb=30
xhp3=370
yhp3=120
healthPoint3=pygame.Rect(xhp3,yhp3,hp3_wb,hp3_hb)

#projectile variables

#projectile 1
proj_hb=10
proj_wb=10
xp=xb-proj_wb
yp=yb+25
projectile1=pygame.Rect(xp,yp,proj_wb,proj_hb)

background=pygame.transform.scale(pygame.image.load('FinalGame\Map_DemonIsland.png'),(1920,1080))
xbg=-615
ybg=-200

while playLvl3:
    os.system('cls')
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            playLvl3=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a] and character.x>=move:
        character.x-=move
        character_left.x-=move
        character_right.x-=move
        character_bottom.x-=move
    if keys[pygame.K_d] and character.x<=WIDTH-(char_wb+move):
        character.x+=move
        character_left.x+=move
        character_right.x+=move
        character_bottom.x+=move
    if jumping==False and keys[pygame.K_SPACE]:
        jumping=True

    if jumping:
        character.y-=jump_move
        character_left.y-=jump_move
        character_right.y-=jump_move
        character_bottom.y-=jump_move
        jump_move-=2
        if jump_move<-20:
            jumping=False
            jump_move=20
    
    if character_left.colliderect(boss) or character_right.colliderect(boss):
        playLvl3=False
        print('Game Over\nYou lose')
    
    if character_bottom.colliderect(boss) and full_health==True:
        full_health=False
        medium_health=True
        boss.x=0
    if character_bottom.colliderect(boss) and medium_health==True:
        medium_health=False
        low_health=True
        boss.x=WIDTH-boss_wb
    if character_bottom.colliderect(boss) and low_health==True:
        playLvl3=False
        print('Game Over\nYou win')

    screen.blit(background,(xbg,ybg))
    screen.blit(Health_title,(xt,50))
    pygame.draw.rect(screen,char_color,character,3)
    pygame.draw.rect(screen,char_side_color,character_left)
    pygame.draw.rect(screen,char_side_color,character_right)
    pygame.draw.rect(screen,char_side_color,character_bottom)
    pygame.draw.rect(screen,boss_color,boss,3)
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
    #pygame.draw.rect(screen,projectile_color,)
    pygame.time.delay(20)
    pygame.display.update()