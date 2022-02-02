#Ishaan Kandoth
#1/31/22
#Strings are arrays of characters
#Has many functions
import os, time
os.system('cls')
myName='Ishaan Kandoth'
#or
myName="Ishaan Kandoth"
print('Your name is:', myName)
Statement=''' This is an example of a statement



idk why I put this here...

anyway'''
print(Statement)
if 'idk' in Statement:
    print('🤔')
print('why' not in Statement)
num=int(input('which letter do you want to print?\n'))
print(myName[num])
time.sleep(1)
os.system('cls')