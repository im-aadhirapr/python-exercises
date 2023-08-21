# BMI

weight = float(input("Enter the weight in kg"))
height = float(input("Enter the height in meter"))
bmi =round((weight) / (height ** 2))

if bmi < 18.5:
    print(f"Your bmi is {bmi} and you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi} and you have a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi} and you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi} and you are obese")
else:
    print(f"Your bmi is {bmi} and you are clinically obese")

# Write a program to check whether a year is leap year or not

year = int(input("Enter the year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")