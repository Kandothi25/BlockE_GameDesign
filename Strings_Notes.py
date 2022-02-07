#Ishaan Kandoth
#1/31/22
#Strings are arrays of characters
#Has many functions
import os, time, random
os.system('cls')
myName='Ishaan Kandoth'
#or
myName="Ishaan Kandoth"
print('Your name is:', myName)
for elem in myName:
    print(elem, end=' ')
guess=random.choice(myName)
print('\n'+guess)
words=["words", "funny", "robot"]
word=random.choice(words)
print(word)
check=True
while check:
    letter=input('Dear user, please give us a letter: ')
    if len(letter)>1 or not letter.isalpha():
        print('please try again')
    else:
        check=False
        print('You are ready')
for i in range(len(word)):
    if letter == word[i]:
        print(letter, end= " ")
    else:
        print('_', end=' ')


Statement='''this is an example of a statement



idk why I put this here...

anyway'''
# print(Statement)
# if 'idk' in Statement:
#     print('🤔')
# print('why' not in Statement)
# num=int(input('which letter do you want to print?\n'))
# print(myName[num])
# time.sleep(2)
#find will return the index of the character you are looking for (first instance)

INDEX=myName.find('a')
print(INDEX)
#Finding the length of your word
wordLen=len(myName)
#last index is 1 less than length
#For loop in range 0 to limit
for i in range(wordLen-1):
    if "a" in myName[i]:
        print(i, end=', ')
print(' ')
print('done')
Statement=Statement.capitalize()
print(Statement)

check=True
while check:
    letter=input('Dear user, please give us a letter: ')
    if len(letter)>1 or not letter.isalpha():
        print('please try again')
    else:
        check=False
        print('You are ready')
print('Thank you, the letter is '+letter)
if letter in Statement:
    print('GREAT')
else:
    print(':(')
# time.sleep(1)
# os.system('cls')