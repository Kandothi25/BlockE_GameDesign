import os, random
os.system('cls')

# Today we are learning try and except, functions, elif

# Make menu a function key word def
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
#Checking for correct user input
RunGame=True
while(RunGame):
    Menu()
    Check=True
    while(Check):
        try:
            choice=int(input("Choice: "))
            Check=False
        except ValueError: 
            print('Sorry, not an option, please enter 1 to 3 only')

    if choice == 1:
        myNumber= random.randint(1,10)
    elif choice == 2:
        myNumber= random.randint(1,50)
    elif choice == 3:
        myNumber= random.randint(1,100)
    print(choice)
    GameOn=True
    while(GameOn):
        userGuess=int(input("give me a number "))
        if myNumber ==userGuess:
            print("You guessed it!")
            GameOn=False
        else:
            print("good luck next time", myNumber) #myNumber is there for testing purposes
    print("The number to guess was " + str(myNumber))
    os.system('cls')