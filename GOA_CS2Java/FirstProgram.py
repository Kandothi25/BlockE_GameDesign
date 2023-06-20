# Ishaan Kandoth 6/19/2023
# Sources: I used https://www.w3schools.com/python/ref_string_upper.asp for the .upper() Method
#          I used https://www.w3schools.com/python/python_try_except.asp for Try Except
#          I used https://www.geeksforgeeks.org/python-random-module/ for the random module

import random # imports the random module which is used to generate the number
run=True # Boolean for the while loop
att=3 # variable for tracking attempts
num=random.randint(1,10) # generates a number between 1 and 10

def restart(): # defines the restart function which will be used at the end of each round
    global num, att, run
    rstrt=input('Would you like to play again? (Y/N): ') # asks the user if they want to restart
    if rstrt.upper()=='Y': 
        num=random.randint(1,10) # generates a new number
        att=3 # resets attempts
    elif rstrt.upper()=='N':
        run=False # sets Boolean to false, ending the loop

while run:
    guess=input('Enter number between 1 and 10: ') # asks the user to guess the number, converts input to an integer so it can be compared with the correct number
    valid=True #Boolean for input validity
    try: #checks if the input is valid
        int(guess)
    except: #if the input cannot be converted to an integer, it is invalid
        valid=False
    if valid and 1<=int(guess)<=10: # checks if the user inputted a number between 1 and 10
        if guess==num: # checks if the guess is correct
            print('Yes! You got it!')
            restart() # runs the restart function
        else:
            print("Nope, that's not it")
            att-=1 # decreases remaining attempts by 1
            if att==0: # checks if the user has run out of attempts
                print('The answer was:',num)
                restart() # runs the restart function
    else:
        print('Please enter a valid number.')