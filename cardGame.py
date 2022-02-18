#Ishaan Kandoth
#2/16/22
import os
os.system('cls')
#Card War game
numberCards=[]
for i in range(2,11):
    numberCards.append(i)
numberCards.insert(0,'A')
suits=['♠', '♦', '♣', '♥']
royals=['J', 'Q', 'K']
#Make a combined list for all cards [A♠,A♦,A♣,A♥,2♠,2♦,2♣,2♥,...J,Q,K, etc...]
finalDeck=[]
def Deck(cardnumber):
    global suits
    global numberCards
    global finalDeck
    for i in range(len(suits)):
        suits[i]=str(numberCards[cardnumber])+str(suits[i])
    finalDeck.extend(suits)
    suits=['♠', '♦', '♣', '♥']
for l in range(0,8):
    Deck(l)
finalDeck.extend(royals)
print('Deck of Cards:\n\n'+str(finalDeck))