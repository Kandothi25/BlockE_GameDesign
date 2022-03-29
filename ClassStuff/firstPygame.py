#Ishaan Kandoth
#3/4/22
import os, time
import pygame as p

os.system('cls')

#initialize pygame
p.init()
#define colors
red=[255,0,0]
orange=[255,165,0]
yellow=[255,255,0]
green=[0,255,00]
blue=[0,0,255]
cyan=[0,255,255]
purple=[128,0,128]
magenta=[255,0,255]
black=[0,0,0]
white=[255,255,255]
colors=[red,orange,yellow,green,blue,cyan,purple,magenta,black,white]
colors={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,00],'blue':[0,0,255],'cyan':[0,255,255]}
#create your window/screen
WIDTH=600
HEIGHT=700
screen=p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption('My Window')
p.display.update()
screen.fill(red)
p.display.update()
time.sleep(0.25)
screen.fill(orange)
p.display.update()
time.sleep(0.25)
screen.fill(yellow)
p.display.update()
time.sleep(0.25)
screen.fill(green)
p.display.update()
time.sleep(0.25)
screen.fill(blue)
p.display.update()
time.sleep(0.25)
screen.fill(cyan)
p.display.update()
time.sleep(0.25)
screen.fill(purple)
p.display.update()
time.sleep(0.25)
screen.fill(magenta)
p.display.update()
time.sleep(0.25)
screen.fill(black)
p.display.update()
time.sleep(0.25)
screen.fill(white)
p.display.update()
time.sleep(0.25)
p.time.delay(5000)

x=20
y=30
wbox=50
hbox=50
square=p.Rect(x,y,wbox,hbox)
square2=p.Rect(x+200,y+200,wbox,hbox)

run=True
while run:
    for i in colors:
        screen.fill(i)
        p.display.update()
        time.sleep(0.25)
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    p.draw.rect(screen,(white),square)
    p.draw.rect(screen,(white),square2)
    p.display.update()