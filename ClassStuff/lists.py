#Ishaan Kandoth
#Lists and List methods
import os, random
os.system('cls')

fruits=['bananna', 'grape', 'mango', 'orange', 'watermelon', 'apple', 'strawberry']
Animals=['monkey', 'shark', 'pig', 'dog', 'cat', 'horse', 'fish', 'bird', 'chicken']
ComputerParts=['monitor', 'keyboard', 'mouse', 'trackpad', 'motherboard', 'processor']
#length of array
size=len(fruits)
print(size)
fruits.append('rambutan')
for i in range (size+1): #13 is not included
    print(fruits[i])
print(fruits[size-1])
print(fruits[-2])
print(fruits.count('bananna'))
fruits.append(Animals)
print(fruits)
fruits.extend(ComputerParts)
print('\n',fruits)