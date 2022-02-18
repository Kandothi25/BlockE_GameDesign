#Ishaan Kandoth
#2/16/22
import os
os.system('cls')
#Card War game
suits=['♠', '♦', '♣', '♥']
royals=['J', 'Q', 'K']
numberCards=[]
for i in range(2,11):
    numberCards.append(i) #Adding numbers to deck
numberCards.insert(0,'A') #Adding the ace to the deck
numberCards.extend(royals) #Adding royals to the deck (extend instead of append so it isn't list)
#Make a combined list for all cards [A♠,A♦,A♣,A♥,2♠,2♦,2♣,2♥,...J,Q,K, etc...]
finalDeck=[]
def Deck(cardnumber): #the function to add suits to each of the numbers
    global suits
    global numberCards
    global finalDeck
    for i in range(len(suits)):
        suits[i]=str(numberCards[cardnumber])+str(suits[i])
    finalDeck.extend(suits)
    suits=['♠', '♦', '♣', '♥'] #The suits list is reset so it can be added to the next number
for l in range(0,13):
    Deck(l) #The function is called for each item in the list, the final deck is created
print('Deck of Cards:\n\n'+str(finalDeck))