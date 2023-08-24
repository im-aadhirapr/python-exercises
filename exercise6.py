# Rock paper scissors (0 for rock, 1 for paper, 2 for scissors)

import random
users_choice = int(input("Enter your choice 0 for rock, 1 for paper, 2 for scissors"))
choosed_value_of_computer = random.randint(0,2)
print(f"Computer choose {choosed_value_of_computer}")
if users_choice == choosed_value_of_computer:
    print("Draw")
elif choosed_value_of_computer > users_choice:
    print("Computer wins")
elif users_choice > choosed_value_of_computer:
    print("User wins")
elif users_choice == 2 and choosed_value_of_computer == 0:
    print("Computer wins")
elif users_choice == 0 and choosed_value_of_computer == 2:
    print("User wins")
else:
    print("Wrong option")
