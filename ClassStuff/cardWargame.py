#first let's import random since we will be shuffling
import random, os
os.system('cls')
deck=[]
numberCards = []
suits = ['♥',"♦", "♣", "♠"]
royals = ["J", "Q", "K", "A"]
def CreateDeck():
    global deck
    global numberCards
    global suits
    global royals
    #next, let's start building lists to build the deck
    #NumberCards is the list to hold numbers plus face cards
        

    #using loops and append to add our content to numberCards :
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the card faces to the base list
    #Create full deck
    for k in range(4):   # four suits
        for l in range(13): #13 cards per suit
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make
    #you can print the deck here, if you want to see how it looks

#now let's see the deck!
def printingDeck():
    global row
    global col
    global deck
    counter=0
    for row in range(4):
        for col in range(13):
            print(deck[counter], end=" ")
            counter +=1
        print()

#now let's shuffle our deck!
#Shuffle the deck cards
player1=[]
player2=[]
def shuffleAndAssign():
    global player1
    global player2
    random.shuffle(deck)
    # you could print it again here just to see how it shuffle
    #loop to devide the cards to each player
    for l in range(52):
        if l%2==0:
            player1.append(deck[l])
        else:
            player2.append(deck[l])


def SplitDeck():
    global halfDeck
    global plyr1
    global plyr2
    print("player1 ",player1)
    print()
    print("player2 ",player2)
    halfDeck=int(len(deck)/2)
    plyr1=0
    plyr2=0

    #ask user to hit a key to release cards

tempPlayer1=[]
tempPlayer2=[]
def TemporaryDecks(winner,i):
    winner.append(player1[i])
    winner.append(player2[i])
    player1.pop(i)
    player2.pop(i)
    print(winner)

def PlayGame():
    global click
    global halfDeck
    global plyr1
    global plyr2
    global player1
    global player2
    global GameOn
#while GameOn:
    CreateDeck()
    printingDeck()
    shuffleAndAssign()
    SplitDeck()
    for i in range (0,halfDeck):
        click=input("Press a any key to get cards: ")
        os.system('cls')
        if len(player1)>0 or len(player2)>0:
            print("Player 1     Player 2")
            print("     "+player1[i]+"      "+player2[i])
            if player1[i]>player2[i]:
                plyr1 +=1
                TemporaryDecks(tempPlayer1,i)
            elif player1[i]<player2[i]:
                plyr2 +=1
                TemporaryDecks(tempPlayer2,i)
            else:
                print('tie')
        else:
            print('Would you like to play again? Type \"yes\" or \"no\"')
            PlayAgain=True
            while(PlayAgain):
                restart=input('')
                if restart.lower()==str('yes'):
                    print('restarting...')
                    PlayAgain=False
                elif restart.lower()==str('no'):
                    PlayAgain=False
                    GameOn=False
                else:
                    print('That was not an option. Please type \"yes\" or \"no\"')
        print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2))
    if plyr1>plyr2:
        print("Player one won the game "+str(plyr1)+" to "+str(plyr2))
    elif plyr2>plyr1:
        print("Player two won the game "+str(plyr2)+" to "+str(plyr1))
    else:
        print('Its a tie!')

GameOn = True
PlayGame()
print('Game Over')