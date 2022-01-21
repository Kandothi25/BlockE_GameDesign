#Ishaan Kandoth
#1/21/22

import os, random
os.system('cls')

#learn the input() function, random
#type casting, branching, looping

#method 1:
# print('Enter a number from 1 to 10',end=': ')
# userinfo=int(input()) #input returns a string, we must type cast if we need a number
# print('The number is %.2f' %(userinfo/3))

#method 2:
# guess=int(input('Enter a number '))

#guess a number
#instead of using fixed number, we will use random
Gamemode=input('Pick a gamemode:\ntype \"1\" for 1-10\ntype \"2\" for 1-50\ntype \"3\" for 1-100\n')
if Gamemode==1:
    myNumber=random.randint(1,10)
elif Gamemode==2:
    myNumber=random.randint(1,50)
else:
    myNumber=random.randit(1,100)
GameOn=True
while(GameOn):
    userGuess=int(input('Guess a number'))
    if myNumber == userGuess:
        print('Correct!')
        GameOn=False
    else:
        print('Incorrect!')
print('The number was', myNumber)