#Ishaan Kandoth
#2/16/22
import os
os.system('cls')
#Card War game
numberCards=[]
for i in range(2,11):
    numberCards.append(i)
    numberCards[i-2]=str(numberCards[i-2])
print(numberCards)
suits=['']
royals=['J', 'Q', 'K', 'A']
#Make a combined list [2,3,4,5,6,7,8,9,10,11,12,J,Q,K, etc...]
#Make combinations for every card ex: 2c, 2h, 5s ...