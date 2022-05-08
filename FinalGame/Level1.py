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
ye1=HEIGHT/2
enemy1=pygame.Rect(xe1,ye1,enemy1_wb,enemy1_hb)

#Projectile variables
proj_hb=5
proj_wb=5
xp=WIDTH
yp=HEIGHT-10
projectile=pygame.Rect(xp,yp,proj_wb,proj_hb)

#Platform variables
plat_hb=60
plat_wb=60
xpl=WIDTH/2
ypl=HEIGHT-120
platform1=pygame.Rect(xpl,ypl,plat_wb,plat_hb)

colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
'white':[255,255,255],'black':[0,0,0]}

background1=pygame.image.load('FinalGame\\retrocity.png')
char_color=colors.get('blue')
char_side_color=colors.get('cyan')
enemy_color=colors.get('red')
proj_color=colors.get('yellow')
platform_color=colors.get('black')

while playLvl1:
    yc2=character.y+char_hb
    os.system('cls')
    screen.blit(background1,(0,0))
    #projectile.x-=15
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            playLvl1=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a] and character.x>=move and not platform1.colliderect(character_left):
        character.x-=move
        character_left.x-=move
        character_right.x-=move
        character_top.x-=move
        character_bottom.x-=move
    if keys[pygame.K_d] and character.x<=WIDTH-(char_wb+move) and not platform1.colliderect(character_right):
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

    # if yc+char_hb+1>HEIGHT:
    #     jump_move=0
    #     jumping=True
    # if yc+char_hb+1<HEIGHT:
    #     yc=HEIGHT-30

    if platform1.colliderect(character_bottom):
        GravityCancel=True
        Falling=False
        fall_move=0
        jumping=False
        jump_move=20
        character.y=ypl-1-30
        character_left.y=ypl-1-20
        character_right.y=ypl-1-20
        character_top.y=ypl-1-40
        character_bottom.y=ypl-1
        if keys[pygame.K_SPACE]:
            jumping=True
    else:
        GravityCancel=False

    #if GravityCancel:
        #print('GC is on')
    #else:
        #print('GC is off')

    if platform1.colliderect(character_top):
        bump=True
        #Jumping=False
        #jump_move=20
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

    # if int(yc_b)>=int(HEIGHT):
    #     print('too low 1')
    #     yc=HEIGHT-30
    #     yc_l=HEIGHT-20
    #     yc_r=HEIGHT-20
    #     yc_t=HEIGHT-40
    #     yc_b=HEIGHT
    #     Falling=False

    if projectile.colliderect(character):
        playLvl1=False
    #mouse coordinates
    mouse_pos=pygame.mouse.get_pos()
    xm=mouse_pos[0]
    ym=mouse_pos[1]
    # print(xm,ym)
    #os.system('cls')

    #updating screen
    pygame.draw.rect(screen,platform_color, platform1)
    pygame.draw.rect(screen, enemy_color, enemy1,3)
    pygame.draw.rect(screen, char_color, character,3)
    pygame.draw.rect(screen,char_side_color,character_left)
    pygame.draw.rect(screen,char_side_color,character_right)
    pygame.draw.rect(screen,char_side_color,character_top)
    pygame.draw.rect(screen,char_side_color,character_bottom)
    pygame.draw.rect(screen,proj_color,projectile)
    pygame.time.delay(20)
    pygame.display.update()    