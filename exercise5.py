# Love calculator

'''
1 .The calculator would first get the names of the two people from the user.
2. It would then create a list of all the letters in the word "true love".
3. It would then count the number of times each letter in the word "true love" appears in each of the two names.
4. The calculator would then add up the number of times each letter appears in both names.
5. The higher the total number of letters that appear in both names, the higher the love compatibility score.
'''

name1 = input("What is your name ?")
name2 = input("What is his/her name ?")
combine_names = name1 + name2
lowercase_names = combine_names.lower()

t = lowercase_names.count('t')
r = lowercase_names.count('r')
u = lowercase_names.count('u')
e = lowercase_names.count('e')

l = lowercase_names.count('l')
o = lowercase_names.count('o')
v = lowercase_names.count('v')
e = lowercase_names.count('e')

true_score = t + r + u + e
love_score = l + o + v + e

total_score = int(str(true_score) + str(love_score))
print(f"Your love score is {total_score}%")

# Heads and tails

import random
a = random.randint(0,1)
if a == 1:
    print("Heads")
else:
    print("Tails")

# Write a program to select a random name from a list of names and the person selected will pay the bill

import random
names = input("Enter the names seperated by commas")
individual_names = names.split(',')
selected_person = random.choice(individual_names)
print(f"{selected_person} will pay the bill")

# Write a program to select a random name from a list of names and the person selected will pay the bill without choice()

import random
names = input("Enter the names seperated by commas")
individual_names = names.split(',')
length = len(individual_names)
print(f"individial name {individual_names}")
selected_person = random.randint(0,length-1)
print(f"{individual_names[selected_person]} has to pay the bill")