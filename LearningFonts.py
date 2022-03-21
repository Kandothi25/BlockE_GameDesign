#Ishaan Kandoth
#3/21/22
import os, pygame, time
os.system('cls')
pygame.init()
window=pygame.display.set_mode((700,700))
pygame.display.set_caption('Testing Fonts')

#Creating different types of fonts
TITLE_FNT=pygame.font.SysFont('calibri',80)
MENU_FNT=pygame.font.SysFont('calibri',40)
INST_FNT=pygame.font.SysFont('calibri',25)
text=TITLE_FNT.render('yo',1,(255,255,255))
window.fill((0,0,0))
window.blit(text,(300,300))
pygame.display.update()
pygame.time.delay(999)
window.fill((0,0,0))
text=TITLE_FNT.render('sup',1,(255,255,255))
window.blit(text,(300,300))
pygame.display.update()
pygame.time.delay(999)
window.fill((0,0,0))
text=TITLE_FNT.render('bye',1,(255,255,255))
window.blit(text,(300,300))
pygame.display.update()
pygame.time.delay(100)