import os, random
os.system('cls')
def Menu():
    print('============================================')
    print('|                                          |')
    print('|             Guess the Number             |')
    print('|                                          |')
    print('============================================')
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
            Check=False
        except ValueError: 
            print('Sorry, not an option, please enter \"1\", \"2\" or \"3\" only')
    if int(Gamemode)==1:
        myNumber=random.randint(1,10)
    elif int(Gamemode)==2:
        myNumber=random.randint(1,50)
    elif int(Gamemode)==3:
        myNumber=random.randint(1,100)
    GameOn=True
    while(GameOn):
        userGuess=input('Guess the number: ')
        if str.isnumeric(userGuess):
            if int(myNumber) == int(userGuess):
                print('Correct!')
                GameOn=False
            elif int(myNumber)>int(userGuess):
                print('Incorrect! Too low.\nIf you give up, type \"quit\" to end the game.')
            elif int(myNumber)<int(userGuess):
                print('Incorrect! Too high.\nIf you give up, type \"quit\" to end the game.')
        elif str(userGuess) == 'quit':
            print('Better luck next time!')
            GameOn=False
        else:
            print('Incorrect! If you give up, type \"quit\" to end the game.')
    print('The number was', myNumber)
    restart=input('Would you like to play again? Type \"yes\" or \"no\"\n')
    if restart==str('yes'):
        print('restarting')
    elif restart==str('no'):
        RunGame=False
    os.system('cls')