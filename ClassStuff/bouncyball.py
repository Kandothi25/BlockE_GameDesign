import os, pygame, random
os.system('cls')
pygame.init()
run=True
WIDTH=500
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Bonk')
move=2
rad=30
xc=250
yc=250
# cr_color= (255,255,255)
hb_color= (255,255,255)
paddle_color=(255,255,255)

c_wbox=30
c_hbox=30
xh=xc-(rad/1.5)
yh=yc-(rad/1.5)
hitbox=pygame.Rect(xh,yh,c_wbox,c_hbox)

p1_wbox=20
p1_hbox=100
xp1=30
yp1=200
paddle1=pygame.Rect(xp1,yp1,p1_wbox,p1_hbox)

move_trigger= random.randint(1,4)

while(run):
    screen.fill((0,0,0))
    for case in pygame.event.get():
            if case.type==pygame.QUIT:
                run=False
    keys=pygame.key.get_pressed()
    if move_trigger==1 and xc>=move:
            xc-=move
            hitbox.x-=move
            if xc==move:
                move_trigger=2
    if move_trigger==2 and xc<=WIDTH-move:
            xc+=move
            hitbox.x+=move
            if xc==WIDTH-move:
                move_trigger=1
    pygame.draw.rect(screen, hb_color, hitbox)
    pygame.draw.rect(screen, paddle_color, paddle1)
    #pygame.draw.circle(screen, cr_color, (xc,yc), rad)
    pygame.display.update()
    pygame.time.delay(5)