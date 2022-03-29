#Ishaan Kandoth
#1/25/22
#Number guessing game
import os, random
os.system('cls')
def Menu():
    print('<[]========================================[]>')
    print(' {                                          }')
    print(' {             Guess the Number             }')
    print(' {                                          }')
    print('<[]========================================[]>')
    print('')
    print('        /+[]====================[]+\ ')
    print('    ---<=+[] type \"1\" for 1-10  []+=>---')
    print('        \+[]====================[]+/')
    print('')
    print('        /+[]====================[]+\ ')
    print('    ---<=+[] type \"2\" for 1-50  []+=>---')
    print('        \+[]====================[]+/')
    print('')
    print('        /+[]====================[]+\ ')
    print('    ---<=+[] type \"3\" for 1-100 []+=>---')
    print('        \+[]====================[]+/')
RunGame=True
while(RunGame):
    Menu()
    Check=True
    while(Check):
        try:
            Gamemode=int(input("\nChoose your gamemode: "))
            if Gamemode>0 and Gamemode<4:
                Check=False
            else:
                print('Sorry, not an option, please enter \"1\", \"2\" or \"3\" only')
        except ValueError: 
            print('Sorry, not an option, please enter \"1\", \"2\" or \"3\" only')
    if Gamemode==1:
        myNumber=random.randint(1,10)
        attempts=5
    elif Gamemode==2:
        myNumber=random.randint(1,50)
        attempts=10
    elif Gamemode==3:
        myNumber=random.randint(1,100)
        attempts=15
    #print('The number is', myNumber) #For testing the code
    GameOn=True
    while(GameOn):
        if attempts==1:
            GameOn=False
        else:
            GameOn=True
        print('You have ',attempts,' attempts left. Good luck!')
        if Gamemode==1:
            userGuess=input('Guess a number from 1-10: ')
        elif Gamemode==2:
            userGuess=input('Guess a number from 1-50: ')
        elif Gamemode==3:
            userGuess=input('Guess a number from 1-100: ')
        if str.isnumeric(userGuess):
            if int(myNumber) == int(userGuess):
                print('Correct!')
                GameOn=False
            elif int(myNumber)>int(userGuess):
                print('Incorrect! Too low.\nIf you give up, type \"quit\" to end the game.')
                attempts=attempts-1
            elif int(myNumber)<int(userGuess):
                print('Incorrect! Too high.\nIf you give up, type \"quit\" to end the game.')
                attempts=attempts-1
        elif str(userGuess.lower()) == 'quit':
            print('Better luck next time!')
            GameOn=False
        else:
            print('Incorrect! If you give up, type \"quit\" to end the game.')
            attempts=attempts-1
    print('The number was', myNumber)
    print('Would you like to play again? Type \"yes\" or \"no\"')
    PlayAgain=True
    while(PlayAgain):
        restart=input('')
        if restart.lower()==str('yes'):
            print('restarting...')
            PlayAgain=False
        elif restart.lower()==str('no'):
            PlayAgain=False
            RunGame=False
        else:
            print('That was not an option. Please type \"yes\" or \"no\"')
    os.system('cls')
    print('Game Over')