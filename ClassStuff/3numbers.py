import os
os.system('cls')
num1=int(input('what is your first number? \n'))
num2=int(input('what is your second number? \n'))
num3=int(input('what is your third number? \n'))
if num1 < num2 and num1 < num3:
    print('The first number was the smallest one')
elif num2 < num1 and num2 < num3:
    print('The second number was the smallest one')
elif num3 < num1 and num3 < num2:
    print('The third number was the smallest one')
#C:\Users\kandothi25\.vscode\BlockE_GameDesign\ClassStuff\3numbers.py