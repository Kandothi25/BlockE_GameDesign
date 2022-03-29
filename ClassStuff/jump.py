import os, pygame
os.system('cls')
pygame.init()
WIDTH=500
HEIGHT=500
check=True
x=0
y=450
wbox=50
hbox=50
move=15
jump_move=10
jumping=False
square=pygame.Rect(x,y,wbox,hbox)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jump')
colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'cyan':[0,255,255],'purple':[128,0,128],'magenta':[255,0,255],
'black':[0,0,0],'white':[255,255,255]}
background=colors.get('black')
sq_color=colors.get('cyan')
while check:
    screen.fill(background)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a] and square.x>=move:
        square.x-=move
    if keys[pygame.K_d] and square.x<=440:
        square.x+=move
    
    if jumping==False and keys[pygame.K_SPACE]:
        jumping = True
    if jumping:
        square.y-=jump_move
        jump_move-=1
        if jump_move< -10:
            jumping=False
            jump_move=10
    
    pygame.draw.rect(screen, sq_color, square)
    pygame.time.delay(15)
    pygame.display.update()