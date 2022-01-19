# This is just a sample program

print('Hello world')
中文 = input('你会不会说中文？')
print('我不懂。' '\n因为我的中文不好，所以我要说英文。')
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name.capitalize()+' '+last_name.capitalize()
print('Hello '+full_name+'! 👋')
full_name_lowercase = full_name.lower()
letter = input('Enter any letter: ')
letter_lowercase = letter.lower()
if full_name_lowercase.count(letter_lowercase) == int(1):
    print('Your name has', full_name_lowercase.count(letter_lowercase), letter)
else:
    print('Your name has', full_name_lowercase.count(letter_lowercase), letter+"'s")

thisvariablehasnopurpose = input('Would you like to know what time it is? \n')
if thisvariablehasnopurpose.lower() == str('yes'):
    print('Well so do I')
else:
    print("Well I'll tell you anyway")
from datetime import datetime
print('Right now the time is', datetime.now())

print("Now let's play a game")
x=input('Enter a number: ')
y=input('Enter another number: ')
print('The sum of your numbers is:', int(x)+int(y))
print('The difference of your numbers is:', int(x)-int(y))
print('The product of your numbers is:', int(x)*int(y))
print('The quotient of your numbers is:', int(x)/int(y))
print('The first number raised to the power of the second number is:', int(x)**int(y))
print('That was a lot of math')

# Pseudo code from class
print('Remember the pseudo code from class?')
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
test3 = input('Enter the score for test 3: ')
sum = (int(test1)+int(test2)+int(test3))
quotient = (int(sum)/3)
print('The average is:', quotient)
if int(quotient) > 75:
    print('Not bad. 😎')
else:
    print('Bruh get gud. 😒')

# More Conditional Statements
print("Remember that game we played earlier? I'm going to use those numbers again.")
print('Your first number was', x, '\nYour second number was 🤔 ... I forgor 💀')
z = input('Please give me a second number different than your first number: ')
if int(x) > int(z):
    print('Your second number is less than your first number.')
else:
    print('Your second number is greater than your first number.')
if int(full_name_lowercase.count(letter_lowercase)) > int(z):
    print('Your second number is less than the number of', letter+"'s", 'in your name') 
else:
    print('Your second number is greater than the number of', letter+"'s", 'in your name')

# Number conversion
print('Now give me an 8 bit binary number and I will convert it to decimal')
bin_dig1 = input('Enter the first digit: ')
bin_dig2 = input('Enter the second digit: ')
bin_dig3 = input('Enter the third digit: ')
bin_dig4 = input('Enter the fourth digit: ')
bin_dig5 = input('Enter the fifth digit: ')
bin_dig6 = input('Enter the sixth digit: ')
bin_dig7 = input('Enter the seventh digit: ')
bin_dig8 = input('Enter the eighth digit: ')
print('Your binary number is', bin_dig1+bin_dig2+bin_dig3+bin_dig4+bin_dig5+bin_dig6+bin_dig7+bin_dig8)
if int(bin_dig1) == 1:
    dec_dig1 = 128
else:
    dec_dig1 = 0
if int(bin_dig2) == 1:
    dec_dig2 = 64
else:
    dec_dig2 = 0
if int(bin_dig3) == 1:
    dec_dig3 = 32
else:
    dec_dig3 = 0
if int(bin_dig4) == 1:
    dec_dig4 = 16
else:
    dec_dig4 = 0
if int(bin_dig5) == 1:
    dec_dig5 = 8
else:
    dec_dig5 = 0
if int(bin_dig6) == 1:
    dec_dig6 = 4
else:
    dec_dig6 = 0
if int(bin_dig7) == 1:
    dec_dig7 = 2
else:
    dec_dig7 = 0
if int(bin_dig8) == 1:
    dec_dig8 = 1
else:
    dec_dig8 = 0
print('Your decimal number is', int(dec_dig1)+int(dec_dig2)+int(dec_dig3)+int(dec_dig4)+int(dec_dig5)+int(dec_dig6)+int(dec_dig7)+int(dec_dig8))
print('Goodbye world')