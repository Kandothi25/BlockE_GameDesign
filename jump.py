import os, pygame,time
os.system('cls')
pygame.init()
WIDTH=500
HEIGHT=500
check=True
x=0
y=470
wbox=30
hbox=30
s_wbox=30
s_hbox=10
move=1
jump_move=10
square=pygame.Rect(x,y,wbox,hbox)
s_square=pygame.Rect(x,y,wbox,hbox)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jump')
colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'cyan':[0,255,255],'purple':[128,0,128],'magenta':[255,0,255],
'black':[0,0,0],'white':[255,255,255]}
background=colors.get('black')
sq_color=colors.get('cyan')
shadow_color=colors.get('blue')
while check:
    screen.fill(background)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a] and square.x>=move:
        square.x-=move
    if keys[pygame.K_d] and square.x<=WIDTH-hbox:
        square.x+=move
    if keys[pygame.K_SPACE] and square.y>=jump_move:
        square.y-=jump_move
        s_square.y-=jump_move
        pygame.draw.rect(screen, sq_color, square)
        pygame.display.update()
        pygame.time.delay(50)
        pygame.draw.rect(screen, shadow_color, s_square)
        pygame.display.update()
        square.y-=jump_move
        s_square.y-=jump_move
        pygame.draw.rect(screen, sq_color, square)
        pygame.display.update()
        pygame.time.delay(50)
        pygame.draw.rect(screen, shadow_color, s_square)
        pygame.display.update()
        square.y-=jump_move
        s_square.y-=jump_move
        pygame.draw.rect(screen, sq_color, square)
        pygame.display.update()
        pygame.time.delay(50)
        pygame.draw.rect(screen, shadow_color, s_square)
        pygame.display.update()
        square.y+=jump_move
        s_square.y-=jump_move
        pygame.draw.rect(screen, sq_color, square)
        pygame.display.update()
        pygame.time.delay(50)
        pygame.draw.rect(screen, shadow_color, s_square)
        pygame.display.update()
        square.y+=jump_move
        s_square.y-=jump_move
        pygame.draw.rect(screen, sq_color, square)
        pygame.display.update()
        pygame.time.delay(50)
        pygame.draw.rect(screen, shadow_color, s_square)
        pygame.display.update()
        square.y+=jump_move
        s_square.y-=jump_move
        pygame.draw.rect(screen, sq_color, square)
        pygame.display.update()
    pygame.draw.rect(screen, sq_color, square)
    pygame.display.update()
    pygame.time.delay(1)