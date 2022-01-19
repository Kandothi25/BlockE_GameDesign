# Ishaan Kandoth
# 1/19/22

#Objectives: Other operators +-*/ ** exponent % modulus
#               Format Printing escape character

#Program creating an equation, asking user input
#   and formating the output
import os
os.system('cls')

V1 = input('Enter value 1: ')
V2 = input('Enter value 2: ')
V3 = input('Enter value 3: ')
V4 = input('Enter value 4: ')
result = (3 * float(V1) - 2 * float(V2) ** 2 / float(V3))/float(V4)
print('Var1 = %8.2f'% float(V1),'\nVar2 = %8.2f'% float(V2),'\nVar3 = %8.2f'% float(V3),'\nVar4 = %8.2f'% (V4))
print('The result of the equation is: %6.3f'% int(result))