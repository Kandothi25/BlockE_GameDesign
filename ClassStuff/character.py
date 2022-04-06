#Ishaan Kandoth
#4/4/2022
import os, pygame
os.system('cls')
pygame.init()
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LEVEL II')
bg=pygame.image.load('ClassStuff\images\\thumbnail.jpg')
screen.blit(bg,(0,0))

character=pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\standing.png')
screen.blit(character,(300,600))

x=300
y=600
wbox=64
hbox=64
move=5
left=False
right=False
walkCount=0
jump_move=5
jumping=False
land=True
air=False

check=True
while check:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x-=move
    if keys[pygame.K_d]:
        x+=move
    if land:
        if keys[pygame.K_w]:
            y-=move
        if keys[pygame.K_s]:
            y+=move
        
    if y<385 and jumping==False:
        y+=move
    elif 430<x<500 and y==350:
        jumping=False
        move=0

    if jumping==False and keys[pygame.K_SPACE]:
        jumping = True
    if jumping:
        y-=jump_move
        jump_move-=0.25
        if jump_move< -5:
            jumping=False
            jump_move=5
    screen.blit(character,(x,y))
    pygame.time.delay(15)
    pygame.display.update()