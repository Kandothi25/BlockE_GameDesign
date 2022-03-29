#Ishaan Kandoth
#1/27/22
#Creating a rock paper scissors game

#Create an input for user choice
#Define the computer's choice with a random number from 1 to 3
#Write conditional statements to decide the winner
#Create a loop to restart the game

#if 'p' in user:
    #print('Paper!')

import os, random, time
os.system('cls')

def Menu():
    print('<[]========================================[]>')
    print(' {                                          }')
    print(' {            Rock Paper Scissors           }')
    print(' {                                          }')
    print('<[]========================================[]>')
    print('')
    print('       /+[]=======================[]+\ ')
    print('   ---<=+[]   type "r" for rock   []+=>---')
    print('       \+[]=======================[]+/')
    print('')
    print('       /+[]=======================[]+\ ')
    print('   ---<=+[]   type "p" for paper  []+=>---')
    print('       \+[]=======================[]+/')
    print('')
    print('       /+[]=======================[]+\ ')
    print('   ---<=+[] type "s" for scissors []+=>---')
    print('       \+[]=======================[]+/')
UserScore=0
CompScore=0
RunGame=True
while(RunGame):
    Menu()
    Choice=True
    while(Choice):
        user=input('\nEnter your choice: ')
        if user.lower()=='r':
            user=int(1)
            print('Rock!')
            time.sleep(1)
            Choice=False
        elif user.lower()=='p':
            user=int(2)
            print('Paper!')
            time.sleep(1)
            Choice=False
        elif user.lower()=='s':
            user=int(3)
            print('Scissors!')
            time.sleep(1)
            Choice=False
        else:
            print('Not an option.')
    print("Computer's choice:")
    time.sleep(1)
    computer=random.randint(1,3)
    if computer==1:
        print('Rock!')
        time.sleep(1)
    elif computer==2:
        print('Paper!')
        time.sleep(1)
    elif computer==3:
        print('Scissors!')
        time.sleep(1)
    print('')
    if user==1:
        if computer==1:
            print("It's a tie!")
            time.sleep(2)
        elif computer==2:
            print('You lose!')
            time.sleep(2)
            CompScore=CompScore+1
        elif computer==3:
            print('You win!')
            time.sleep(2)
            UserScore=UserScore+1
    elif user==2:
        if computer==1:
            print('You win!')
            time.sleep(2)
            UserScore=UserScore+1
        elif computer==2:
            print("It's a tie!")
            time.sleep(2)
        elif computer==3:
            print('You lose!')
            time.sleep(2)
            CompScore=CompScore+1
    elif user==3:
        if computer==1:
            print('You lose!')
            time.sleep(2)
            CompScore=CompScore+1
        elif computer==2:
            print('You win!')
            time.sleep(2)
            UserScore=UserScore+1
        elif computer==3:
            print("It's a tie!")
            time.sleep(2)
    print('Score: ', UserScore, '-', CompScore)
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