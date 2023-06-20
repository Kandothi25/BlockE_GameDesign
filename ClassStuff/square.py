import pygame, random
pygame.init()
run=True
square_width=50
square_length=50
square_x=225
square_y=225
square_color=[255,255,255]
WIDTH=500
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Square')
square=pygame.Rect(square_x,square_y,square_width,square_length)
while(run):
    screen.fill((0,0,0))
    for case in pygame.event.get():
            if case.type==pygame.QUIT:
                run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w] and square.y>=1:
        square.y-=1
    if keys[pygame.K_a] and square.x>=1:
        square.x-=1
    if keys[pygame.K_s] and square.y<=450:
        square.y+=1
    if keys[pygame.K_d] and square.x<=square.x<=450:
        square.x+=1
    
    pygame.draw.rect(screen,square_color,square)
    pygame.time.delay(2)
    pygame.display.update()