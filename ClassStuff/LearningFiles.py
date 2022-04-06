#Ishaan Kandoth
#3/29/22
#Learning :
# a) open/create a file 
# b) write 'w'
# c) append 'a'
# d) read 'r'
# e) close()
import os, datetime, pygame
os.system('cls')
date=datetime.datetime.now()
score=123
name='Jesse'
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+' '+name+' '+date.strftime('%m/%d/%Y'+'\n')
print(scoreLine)
#open a file and write
#when you write it erases the previous text
myFile=open('ClassStuff\score.txt','w')
myFile.write(scoreLine)

myFile.close()
score=345
name='Jay'
print(date.strftime('%m/%d/%Y'))
scoreLine=str(score)+' '+name+' '+date.strftime('%m/%d/%Y'+'\n')
myFile=open('ClassStuff\score.txt','a')
myFile.write(scoreLine)
myFile.close()
myFile=open('ClassStuff\score.txt','r')
lines=myFile.readline()
print(lines)
lines=myFile.readline()
print(lines)
myFile.close()