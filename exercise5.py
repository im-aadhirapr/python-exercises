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

# true love
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