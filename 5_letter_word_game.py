#Ishaan Kandoth
#2/2/22
#Strings are arrays of characters
#Has Many Functions
import os, random
os.system ('cls')
myName = "Ishaan Kandoth"
myStatement = """My name is very nice because
whatever yay yay happy 

idk what im typing"""

#^^^ IF I USE TRIPLE QUOTATION MARKS - IT PRINTS EXACTLY HOW I TYPE (WITH THE SPACES AND EVERYTHING)
print (myName[6])
#^^ It takes the 6th letter and prints it
print ('My last name begins with ' +myName[6 ])
if 'yay' in myStatement:
    print ('true')
#Checks if the word is there then will give a output
print ('expert' not in myStatement)
#not in or in will make it check the statemtn and will print true or false depending on ur code
INDEX = myName.find("u")
#telling myName.find tells computer to tell me what location a certain character is in
#Find function returns index of the character you are looking for (FIRST INSTANCE)
print (INDEX)
#finding the length of your word
wordLength=len(myName)
#len function tells me how long a word is
print(wordLength) #your last index is len-1
#For loop in range 0 to limit
for i in range(wordLength-1):
    if "u" in myName[i]:
        print(i,end=", ")
print ('')
print ("done")
#FINDS ALL INSTANCES OF A CERTAIN LETTER, UNTIL IT REACHES THE LIMIT THAT YOU SET - IN THIS CASE, WORD LENGTH - 1
myStatement=myStatement.upper()
print (myStatement)



for elem in myName:
    print (elem, end = " ")
guess = random.choice(myName)
print ("\n"+ guess)
words= ["Radio", "Clues", "Suite", "Peter", "Robot"]
word = random.choice (words)
print (word)
check = True
while check:
    letter = input('Dear user, please give us a nice letter\n')
    if len(letter)>1 or not letter.isalpha(): #isaplha says ONLY LETTERS nothing else
        print ('BAD') 
    else:
        check = False
print ("ready to play the game")
for i in range(len(word)):
    if letter == word[i]:
        print (letter, end= " ")
    else:
        print ("_", end=" ")

