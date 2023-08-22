# Adventure park billing system

height = int(input("Enter the height in feet"))

if (height >= 3):
    print("You can go for the ride")
    age = (int(input("Enter the age")))
    if age < 12:
        bill = 150
    elif age >= 18:
        bill = 500
    else:
        bill = 250
    
    want_photos = (input("Want to click photos? (Y/N)"))
    if want_photos == 'Y' or want_photos == 'y':
        total = bill + 50
    else:
        total = bill

    print(f"Please pay the bill of {total}")

else:
    print("You cannot go for the ride")
print("Thank you, visit again")

# Pizza ordering system

size = input("What size of pizza you want? (S|M|L)")
if size == 's' or size == 'S':
    print("Small pizza Rs.100")
    bill = 100
elif size == 'm' or size == 'M':
    print("Medium pizza Rs.200")
    bill = 200
else:
    print("Large pizza Rs.300")
    bill = 300

toppings = input("Wanted to add pepperoni toppings for your pizza (Y|N)")
if toppings == 'y' or toppings == 'Y':
    if size == 's' or size == 'S': 
        print("Toppings for pepperoni for small pizza Rs.30")
        bill = bill + 30
    elif size == 'm' or size == 'M':
        print("Toppings for pepperoni for small pizza Rs.50")
        bill = bill + 50
    else:
        print("Toppings for pepperoni for small pizza Rs.50")
        bill = bill + 50
else:
    print("")

cheese_toppings = input("Wanted to add extra cheese (Y|N)")
if cheese_toppings == 'y' or cheese_toppings == 'Y':
    bill = bill + 20
else:
    print("")

print(f"You have a total amount of {bill}")
print("Thank you, Shop again...........")