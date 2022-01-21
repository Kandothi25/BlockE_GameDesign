import os, random
os.system('cls')
print('============================================')
print('|                                          |')
print('|             Guess the Number             |')
print('|                                          |')
print('============================================')
print('')
print('            ====================')
print('            type \"1\" for 1-10')
print('            ====================')
print('')
print('            ====================')
print('            type \"2\" for 1-50')
print('            ====================')
print('')
print('            ====================')
print('            type \"3\" for 1-100')
print('            ====================')
Gamemode=input('\n')
if int(Gamemode)==1:
    myNumber=random.randint(1,10)
elif int(Gamemode)==2:
    myNumber=random.randint(1,50)
elif int(Gamemode)==3:
    myNumber=random.randint(1,100)
else:
    Gamemode=random.randint(1,3)
    if int(Gamemode)==1:
        myNumber=random.randint(1,10)
    elif int(Gamemode)==2:
        myNumber=random.randint(1,50)
    elif int(Gamemode)==3:
        myNumber=random.randint(1,100)
#print('The number is: ', myNumber) #For testing purposes
GameOn=True
while(GameOn):
    userGuess=input('Guess the number: ')
    if str.isnumeric(userGuess):
        if int(myNumber) == int(userGuess):
            print('Correct!')
            GameOn=False
        else:
            print('Incorrect! If you give up, type \"quit\" to end the game.')
    elif str(userGuess) == 'quit':
        print('Better luck next time!')
        GameOn=False
    else:
        print('Incorrect! If you give up, type \"quit\" to end the game.')
print('The number was', myNumber)