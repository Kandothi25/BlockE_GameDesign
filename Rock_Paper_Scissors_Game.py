#Ishaan Kandoth
#1/27/22
#Creating a rock paper scissors game

#Create an input for user choice
#Define the computer's choice with a random number from 1 to 3
#Write conditional statements to decide the winner
#Create a loop to restart the game

#if 'p' in user:
    #print('Paper!')

import os, random
os.system('cls')

def Menu():
    print('<[]========================================[]>')
    print(' {                                          }')
    print(' {            Rock Paper Scissors           }')
    print(' {                                          }')
    print('<[]========================================[]>')
    print('')
RunGame=True
while(RunGame):
    Menu()
    print("Let's play rock paper scissors! \ntype \"r\" for rock \"p\" for paper and \"s\" for scissors")
    Choice=True
    while(Choice):
        user=input('Enter your choice: ')
        if user.lower()=='r':
            user=int(1)
            print('Rock!')
            Choice=False
        elif user.lower()=='p':
            user=int(2)
            print('Paper!')
            Choice=False
        elif user.lower()=='s':
            user=int(3)
            print('Scissors!')
            Choice=False
        else:
            print('Not an option.')
    print("Computer's choice:")
    computer=random.randint(1,3)
    if computer==1:
        print('Rock!')
    elif computer==2:
        print('Paper!')
    elif computer==3:
        print('Scissors!')
    print('')
    if user==1:
        if computer==1:
            print("It's a tie!")
        elif computer==2:
            print('You lose!')
        elif computer==3:
            print('You win!')
    elif user==2:
        if computer==1:
            print('You win!')
        elif computer==2:
            print("It's a tie!")
        elif computer==3:
            print('You lose!')
    elif user==3:
        if computer==1:
            print('You lose!')
        elif computer==2:
            print('You win!')
        elif computer==3:
            print("It's a tie!")
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