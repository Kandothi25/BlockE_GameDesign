#Ishaan Kandoth
#4/21/22
#Level 1 of Final Game
import os, pygame, random
os.system('cls')
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
move=10
playLvl1=True
jump_move=20
jumping=False

#character variables
char_hb=30
char_wb=30
xc=0
yc=HEIGHT-30
character=pygame.Rect(xc,yc,char_wb,char_hb)

#enemy1 variables
enemy1_hb=30
enemy1_wb=30
xe1=0
ye1=HEIGHT/2
enemy1=pygame.Rect(xe1,ye1,enemy1_wb,enemy1_hb)

#Projectile variables
proj_hb=5
proj_wb=5
xp=0
yp=0
projectile=pygame.Rect(xp,yp,proj_wb,proj_hb)

#Platform variables
plat_hb=60
plat_wb=60
xpl=WIDTH/2
ypl=HEIGHT-60
platform1=pygame.Rect(xpl,ypl,plat_wb,plat_hb)

colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'purple':[128,0,128],'cyan':[0,255,255],'magenta':[255,0,255],
'white':[255,255,255],'black':[0,0,0]}

background1=pygame.image.load('FinalGame\\retrocity.png')
char_color=colors.get('blue')
enemy_color=colors.get('red')
proj_color=colors.get('yellow')
platform_color=colors.get('green')

while playLvl1:
    screen.blit(background1,(0,0))
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            playLvl1=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a] and character.x>=move:
            character.x-=move
    if keys[pygame.K_d] and character.x<=WIDTH-(char_wb+move):
        character.x+=move
    if jumping==False and keys[pygame.K_SPACE]:
            jumping = True
    if jumping:
        character.y-=jump_move
        jump_move-=2
        if jump_move< -20:
            jumping=False
            jump_move=20
    mouse_pos=pygame.mouse.get_pos()
    xm=mouse_pos[0]
    ym=mouse_pos[1]
    #print(xm,ym)
    #os.system('cls')
    pygame.draw.rect(screen,platform_color, platform1)
    pygame.draw.rect(screen, enemy_color, enemy1)
    pygame.draw.rect(screen, char_color, character)
    pygame.time.delay(20)
    pygame.display.update()    