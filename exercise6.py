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