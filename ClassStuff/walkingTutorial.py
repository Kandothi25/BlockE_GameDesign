import os, pygame
os.system('cls')
pygame.init()

win=pygame.display.set_mode((500,480))
pygame.display.set_caption('Image Tutorial')

walkRight=[pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R1.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R2.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R3.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R4.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R5.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R6.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R7.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R8.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\R9.png')]
walkLeft=[pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L1.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L2.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L3.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L4.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L5.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L6.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L7.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L8.png'), pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\L9.png')]
bg=pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\\bg.jpg')
char=pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\standing.png')
spikes=pygame.image.load('ClassStuff\images\Sunfury_(projectile).png')
rip=pygame.transform.scale(pygame.image.load('ClassStuff\images\R.png'),(38,38))

x=50
y=400
width=40
height=60
vel=5

background1=True
Falling=False
Area1=True
Area2=False
Dead=False
clock=pygame.time.Clock()

isJump=False
jumpCount=10

left=False
right=False
walkCount=0

def redrawGameWindow():
    global walkCount, Area1, Area2
    if Area1:
        bg=pygame.image.load('ClassStuff\images\Pygame-Tutorials-master\Pygame-Tutorials-master\Game\\bg.jpg')
    if Area2:
        bg=pygame.image.load('ClassStuff\images\\thumbnail.jpg')
    win.blit(bg,(0,0))
    if background1:
        win.blit(spikes,(250,250))  
    if walkCount+1>=27:
        walkCount=0 
    if left:  
        win.blit(walkLeft[walkCount//3],(x,y))
        walkCount+=1                          
    elif right:
        win.blit(walkRight[walkCount//3],(x,y))
        walkCount+=1
    else:
        if Dead:
            win.blit(rip,(x,y))
        else:
            win.blit(char,(x, y))
        walkCount=0 
    pygame.display.update()
    
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if 212<x<250 and 212<y<250:
        print('*dies*')
        isJump=False
        jumpCount=10
        Falling=True
    while Falling:
        if y==400:
            Dead=True
            Falling=False
        else:
            print('the loop is still working')
            y+=vel
            pygame.display.update()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > vel and not(Dead): 
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_d] and not(Dead):  
        if x < 500 - vel - width:
            x += vel
            left = False
            right = True
        else:
            x=0
            Area1=False
            Area2=True


    else:
        left = False
        right = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE] and not(Dead):
            isJump = True
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    redrawGameWindow() 
pygame.quit()