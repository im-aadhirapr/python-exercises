# Rock paper scissors (0 for rock, 1 for paper, 2 for scissors)

import random
users_choice = int(input("Enter your choice 0 for rock, 1 for paper, 2 for scissors"))
choosed_value_of_computer = random.randint(0,2)
print(f"Computer choose {choosed_value_of_computer}")
if users_choice == choosed_value_of_computer:
    print("Draw")
elif choosed_value_of_computer > users_choice:
    print("You lose")
elif users_choice > choosed_value_of_computer:
    print("You wins")
elif users_choice == 2 and choosed_value_of_computer == 0:
    print("You lose")
elif users_choice == 0 and choosed_value_of_computer == 2:
    print("You wins")
else:
    print("Wrong option")

# Program to calculate average height from a list of heights

heights = input("Enter the heights seperated by commas")
# 151, 153, 154
height_list = heights.split(',')
print(f"Height list is {height_list}")
count = 0
for height in height_list:
    count = count + 1

for i in range(count):
    height_list[i] = int(height_list[i])

sum = 0
for person in height_list:
    sum = sum + person

avg = sum/count
print(f"The average height is {round(avg)}")