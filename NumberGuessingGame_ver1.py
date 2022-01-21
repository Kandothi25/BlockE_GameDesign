import os, random
os.system('cls')
print('============================================')
print('|                                          |')
print('|              Guess the Number            |')
print('|                                          |')
print('============================================')
print('')
Gamemode=input('Pick a gamemode:\ntype \"1\" for 1-10\ntype \"2\" for 1-50\ntype \"3\" for 1-100\n')
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
print('The number is: ', myNumber) #For testing purposes
GameOn=True
while(GameOn):
    userGuess=input('Guess the number: ')
    if int(myNumber) == int(userGuess):
            print('Correct!')
            GameOn=False
    else:
        print('Incorrect! Try again.')
print('The number was', myNumber)