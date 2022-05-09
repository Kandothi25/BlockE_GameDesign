#Ishaan Kandoth
#4/21/22
#Level 1 of Final Game
import os, pygame
os.system('cls')
pygame.init()
WIDTH=700
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
move=10
playLvl1=True
jump_move=20
jumping=False
Falling=False
fall_move=0
GravityCancel=False
bump=False
shootProjectile=False

#character variables
char_hb=30
char_wb=30
xc=0
yc=HEIGHT-30
character=pygame.Rect(xc,yc,char_wb,char_hb)

#left hitbox
char_left_hb=10
char_left_wb=10
xc_l=-10
yc_l=HEIGHT-20
character_left=pygame.Rect(xc_l,yc_l,char_left_wb,char_left_hb)

#right hitbox
char_right_hb=10
char_right_wb=10
xc_r=30
yc_r=HEIGHT-20
character_right=pygame.Rect(xc_r,yc_r,char_right_wb,char_right_hb)

#top hitbox
char_top_hb=10
char_top_wb=10
xc_t=10
yc_t=HEIGHT-40
character_top=pygame.Rect(xc_t,yc_t,char_top_wb,char_top_hb)

#bottom hitbox
char_bottom_hb=10
char_bottom_wb=10
xc_b=10
yc_b=HEIGHT
character_bottom=pygame.Rect(xc_b,yc_b,char_bottom_wb,char_bottom_hb)

#enemy1 variables
enemy1_hb=30
enemy1_wb=30
xe1=0
ye1=370
enemy1=pygame.Rect(xe1,ye1,enemy1_wb,enemy1_hb)

#enemy 2 variables
enemy2_hb=30
enemy2_wb=30
xe2=500
ye2=70
enemy2=pygame.Rect(xe2,ye2,enemy2_wb,enemy2_hb)

#Projectile variables
proj_hb=5
proj_wb=5
xpr=35
ypr=370
projectile=pygame.Rect(xpr,ypr,proj_wb,proj_hb)

#Portal variables
portal_hb=60
portal_wb=30
xpo=WIDTH-30
ypo=40
portal=pygame.Rect(xpo,ypo,portal_wb,portal_hb)
#pygame.transform.scale(pygame.image.load(''))

#Platform 1 variables
plat1_hb=60
plat1_wb=60
xpl1=200
ypl1=HEIGHT-60
platform1=pygame.Rect(xpl1,ypl1,plat1_wb,plat1_hb)
plat1_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat1_wb,plat1_hb))

#Platform 2 variables
plat2_hb=120
plat2_wb=60
xpl2=WIDTH/2
ypl2=HEIGHT-120
platform2=pygame.Rect(xpl2,ypl2,plat2_wb,plat2_hb)
plat2_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat2_wb,plat2_hb))

#Platform 3 variables
plat3_hb=60
plat3_wb=180
xpl3=WIDTH-180
ypl3=HEIGHT-200
platform3=pygame.Rect(xpl3,ypl3,plat3_wb,plat3_hb)
plat3_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat3_wb,plat3_hb))

#Platform 4 variables
plat4_hb=30
plat4_wb=120
xpl4=WIDTH-120
ypl4=HEIGHT/2-5
platform4=pygame.Rect(xpl4,ypl4,plat4_wb,plat4_hb)
plat4_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat4_wb,plat4_hb))

#Platform 5 variables
plat5_hb=60
plat5_wb=120
xpl5=0
ypl5=HEIGHT-200
platform5=pygame.Rect(xpl5,ypl5,plat5_wb,plat5_hb)
plat5_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat5_wb,plat5_hb))

#Platform 6 variables
plat6_hb=60
plat6_wb=450
xpl6=0
ypl6=HEIGHT-400
platform6=pygame.Rect(xpl6,ypl6,plat6_wb,plat6_hb)
plat6_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat6_wb,plat6_hb))

#Platform 7 variables
plat7_hb=20
plat7_wb=WIDTH/2
xpl7=WIDTH/2
ypl7=100
platform7=pygame.Rect(xpl7,ypl7,plat7_wb,plat7_hb)
plat7_img=pygame.transform.scale(pygame.image.load('FinalGame\R.png'),(plat7_wb,plat7_hb))

platformList=[platform1,platform2,platform3,platform4,platform5,platform6,platform7]

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
    yc2=character.y+char_hb
    os.system('cls')
    screen.blit(background1,(0,0))
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            playLvl1=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a] and character.x>=move and not platform1.colliderect(character_left) and not platform2.colliderect(character_left) and not platform3.colliderect(character_left) and not platform4.colliderect(character_left) and not platform5.colliderect(character_left) and not platform6.colliderect(character_left) and not platform7.colliderect(character_left):
        character.x-=move
        character_left.x-=move
        character_right.x-=move
        character_top.x-=move
        character_bottom.x-=move
    if keys[pygame.K_d] and character.x<=WIDTH-(char_wb+move) and not platform1.colliderect(character_right) and not platform2.colliderect(character_right) and not platform3.colliderect(character_right) and not platform4.colliderect(character_right) and not platform5.colliderect(character_right) and not platform6.colliderect(character_right) and not platform7.colliderect(character_right):
        character.x+=move
        character_left.x+=move
        character_right.x+=move
        character_top.x+=move
        character_bottom.x+=move
    if jumping==False and keys[pygame.K_SPACE] and Falling==False and bump==False:
        jumping=True

    if jumping:
        character.y-=jump_move
        character_left.y-=jump_move
        character_right.y-=jump_move
        character_top.y-=jump_move
        character_bottom.y-=jump_move
        jump_move-=2
        if jump_move==0 and GravityCancel==False:
            jumping=False
            jump_move=20
            Falling=True
    
    for i in range (len(platformList)):
        if platformList[i].colliderect(character_bottom):
            GravityCancel=True
            Falling=False
            fall_move=0
            jumping=False
            jump_move=20
            character.y=platformList[i].y-1-30
            character_left.y=platformList[i].y-1-20
            character_right.y=platformList[i].y-1-20
            character_top.y=platformList[i].y-1-40
            character_bottom.y=platformList[i].y-1
            if keys[pygame.K_SPACE]:
                jumping=True
        else:
            GravityCancel=False
    
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

    if jumping==False and character_bottom.y<HEIGHT and GravityCancel==False:
        Falling=True
        
    if Falling and GravityCancel==False:
        character.y-=fall_move
        character_left.y-=fall_move
        character_right.y-=fall_move
        character_top.y-=fall_move
        character_bottom.y-=fall_move
        fall_move-=2
        if yc2>HEIGHT:
            Falling=False
            fall_move=0
            character.y=HEIGHT-30
            character_left.y=HEIGHT-20
            character_right.y=HEIGHT-20
            character_top.y=HEIGHT-40
            character_bottom.y=HEIGHT
    if character.y<=370:
        shootProjectile=True
    if shootProjectile:
        projectile.x+=20
    if projectile.colliderect(character):
        playLvl1=False

    if character.colliderect(portal):
        playLvl1=False

    #mouse coordinates
    mouse_pos=pygame.mouse.get_pos()
    xm=mouse_pos[0]
    ym=mouse_pos[1]
    # print(xm,ym)

    #updating screen
    for i in range (len(platformList)):
        pygame.draw.rect(screen,platform_color, platformList[i])
    pygame.draw.rect(screen,enemy_color,enemy1,3)
    pygame.draw.rect(screen,enemy_color,enemy2,3)
    pygame.draw.rect(screen, char_color, character,3)
    pygame.draw.rect(screen,char_side_color,character_left)
    pygame.draw.rect(screen,char_side_color,character_right)
    pygame.draw.rect(screen,char_side_color,character_top)
    pygame.draw.rect(screen,char_side_color,character_bottom)
    pygame.draw.rect(screen,proj_color,projectile)
    pygame.draw.rect(screen,portal_color,portal,3)
    screen.blit(plat1_img,(xpl1,ypl1))
    screen.blit(plat2_img,(xpl2,ypl2))
    screen.blit(plat3_img,(xpl3,ypl3))
    screen.blit(plat4_img,(xpl4,ypl4))
    screen.blit(plat5_img,(xpl5,ypl5))
    screen.blit(plat6_img,(xpl6,ypl6))
    screen.blit(plat7_img,(xpl7,ypl7))
    pygame.time.delay(20)
    pygame.display.update()    