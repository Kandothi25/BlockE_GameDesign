#Ishaan Kandoth
#3/21/22
import pygame, os
os.system('cls')
pygame.init()

#screen
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Instructions')

#Colors
colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],
'blue':[0,0,255],'cyan':[0,255,255],'purple':[128,0,128],'magenta':[255,0,255],
'black':[0,0,0],'white':[255,255,255]}
background=colors.get('black')

#Fonts
TITLE_FNT=pygame.font.SysFont('comicsans',80)
MENU_FNT=pygame.font.SysFont('courier',40)
INST_FNT=pygame.font.SysFont('calibri',25)

#instructions screen variables
title=TITLE_FNT.render('Geometry Tag',1,'white')
Instructions=MENU_FNT.render('Instructions:',1,'white')
inst1=INST_FNT.render('1) There is one circle and one square.',1,'white')
inst2=INST_FNT.render('2) Move the square with arrow keys.',1,'white')
inst3=INST_FNT.render('3) Move the circle with WASD keys.',1,'white')
inst4=INST_FNT.render('4) The circle must eat the square and the square must escape.',1,'white')
inst5=INST_FNT.render('5) When they collide, the circle grows and the square is teleported.',1,'white')
play=MENU_FNT.render('Press [esc] to play',1,'white')

#displaying instructions screen
instr_Check=True
while instr_Check:
    screen.fill(background)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            instr_Check=False
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_ESCAPE]:
        instr_Check=False
    else:
        screen.blit(title,(80,20))
        screen.blit(Instructions,(200,200))
        screen.blit(inst1,(10,300))
        screen.blit(inst2,(10,350))
        screen.blit(inst3,(10,400))
        screen.blit(inst4,(10,450))
        screen.blit(inst5,(10,500))
        screen.blit(play,(125,600))
    pygame.display.update()
    pygame.time.delay(1)
