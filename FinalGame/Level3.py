#Ishaan Kandoth
#5/8/22
#Level 3 of Final Game
import os, pygame, random
os.system('cls')
pygame.init()
sf=1
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

background=pygame.transform.scale(pygame.image.load('FinalGame\Map_DemonIsland.png'),(1920*sf,1080*sf))
xbg=-615*sf
ybg=-200*sf

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
        print('Phase2')
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
            print('boss is returning from left')
            boss.x+=move
        if bossReturnRight:
            print('boss is returning from right')
            boss.x-=move
        if boss.x==WIDTH/2-boss_wb/2:
            print('boss has returned')
            bossReturnLeft=False
            bossReturnRight=False
            projectilesOn=True
            bossPhase=0
    
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
        print('phase1')
        boss.x-=move
        if boss.x<=0:
            bossPhase=random.randint(1,2)
    if bossRight:
        print('phase1')
        boss.x+=move
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
        playLvl3=False
        print('Game Over\nYou lose')
    if projectilesOn or projectilesActive:
        if character.colliderect(projectile1) or character.colliderect(projectile2) or character.colliderect(projectile3):
            playLvl3=False
            print('Game Over\nYou lose')
    
    if character_bottom.colliderect(boss) and full_health==True:
        print('e')
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
        print('ee')
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
        playLvl3=False
        print('Game Over\nYou win')

    screen.blit(background,(xbg,ybg))
    screen.blit(Health_title,(xt,50*sf))
    pygame.draw.rect(screen,char_color,character,int(3*sf))
    pygame.draw.rect(screen,char_side_color,character_left)
    pygame.draw.rect(screen,char_side_color,character_right)
    pygame.draw.rect(screen,char_side_color,character_bottom)
    pygame.draw.rect(screen,boss_color,boss,int(3*sf))
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
    if projectilesOn or projectilesActive:
        pygame.draw.rect(screen,projectile_color1,projectile1)
        pygame.draw.rect(screen,projectile_color2,projectile2)
        pygame.draw.rect(screen,projectile_color3,projectile3)
    pygame.time.delay(20)
    pygame.display.update()
