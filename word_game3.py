#Ishaan Kandoth
#2/16/22
#Word guessing game
import os, random, time
os.system('cls')
#Create a list for the computer to choose from
#3 different lists for the different categories
#Variable to pick a random word from list
#User input to guess letter
#check if it is a single alphabet
#Check if the letter is in the word
#If it is in the word then print the letter in the corresponding location in the word
#If not, print wrong and try again
#Create an attempts system
#Game ends when the word is guessed or all the attempts are used
#After the loop calculate the score
#Keep the high score

#Levels:
#   1. Fruits
#   2. Animals
#   3. Computer parts

HighScore=0
Score=0
RunGame=True

def Menu():
    print('<[]========================================[]>')
    print(' {                                          }')
    print(' {              Guess the Word              }')
    print(' {                                          }')
    print('<[]========================================[]>')
    print('')
    print('        /+[]====================[]+\ ')
    print('    ---<=+[]    "1" Fruits      []+=>---')
    print('        \+[]====================[]+/')
    print('')
    print('        /+[]====================[]+\ ')
    print('    ---<=+[]    "2" Animals     []+=>---')
    print('        \+[]====================[]+/')
    print('')
    print('        /+[]====================[]+\ ')
    print('    ---<=+[] "3" Computer parts []+=>---')
    print('        \+[]====================[]+/')
    print('')
    print('        /+[]====================[]+\ ')
    print('    ---<=+[]     "4" Score      []+=>---')
    print('        \+[]====================[]+/')
    print('')
    print('        /+[]====================[]+\ ')
    print('    ---<=+[]      "5" Exit      []+=>---')
    print('        \+[]====================[]+/')

word=""
guess=""
def selectWord():
    global word
    global HighScore
    global RunGame
    fruits=['bananna', 'grape', 'mango', 'orange', 'watermelon', 'apple', 'strawberry']
    Animals=['monkey', 'shark', 'pig', 'dog', 'cat', 'horse', 'fish', 'bird', 'chicken']
    ComputerParts=['monitor', 'keyboard', 'mouse', 'trackpad', 'motherboard', 'processor']

    # size=len(fruits)
    # randy=random.randint(0,size)
    # print(randy)
    # word=fruits[randy]
    # print(word)
    Check1=True
    while Check1:
        try:
            Gamemode=int(input("\nChoose a category: "))
            if Gamemode>0 and Gamemode<4:
                Check1=False
            elif Gamemode == 5:
                Check1=False
            else:
                if Gamemode==4:
                    print('Your highscore is:', HighScore)
                else:
                    print('Sorry, not an option, please enter "1", "2", "3", "4" or "5" only')
        except ValueError: 
            print('Sorry, not an option, please enter "1", "2", "3", "4" or "5" only')

    os.system('cls')
    if Gamemode==1:
        word=random.choice(fruits)
        print('Fruits!')
        time.sleep(1)
    elif Gamemode==2:
        word=random.choice(Animals)
        print('Animals!')
        time.sleep(1)
    elif Gamemode==3:
        word=random.choice(ComputerParts)
        print('Computer Parts!')
        time.sleep(1)
    elif Gamemode==5:
        print('')
        RunGame=False

def GuessFunction():
    global guess
    Check2=True
    while Check2:
        try:
            guess=input('\nGuess a letter in the word: ')
            if guess.isalpha() and len(guess)==1:
                Check2=False
            else:
                print('Only one letter please')
        except ValueError:
            print('Only one letter please')
    os.system('cls')

def PlayGame():
    global RunGame
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
        elif restart.lower()==str('nein'):
            PlayAgain=False
            RunGame=False
        else:
            print('That was not an option. Please type \"yes\" or \"no\"')

while RunGame:
    Menu()
    attempts=0
    letterGuessed=""
    word=""
    guess=""
    selectWord()
    if RunGame:
        print(len(word),'letter word')
        gameOn=True
        while gameOn:
            GuessFunction()
            letterGuessed += guess #+= means letterGuessed = letterGuessed + guess
            if guess not in word:
                attempts += 1
                print('You have used', attempts, 'attempts') #for testing purposes
            countletter=0
            for letter in word:
                if letter in letterGuessed:
                    print(letter, end=' ')
                    countletter+=1
                else:
                    print('_', end=' ')
            if attempts==5:
                print('\nSorry, out of attempts')
                Score=0
                gameOn=False
                time.sleep(1)
            if countletter == len(word):
                print('\nyou guessed it!')
                Score=len(word)*5-attempts*2
                gameOn=False
                time.sleep(1)
        print('The word was', word)
        if Score > HighScore:
            HighScore=Score
            print('New High Score:', HighScore)
            time.sleep(1)
            os.system('cls')
        else:
            print('Score:', Score)
            time.sleep(1)
            os.system('cls')
os.system('cls')
print('<[]========================================[]>')
print(' {                                          }')
print(' {                 Game Over                }')
print(' {                                          }')
print('<[]========================================[]>')
print('\nHigh Score:', HighScore, '\n')