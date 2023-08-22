# Program to add digits of a number

number = input("Enter the number ")
num1 = number[0]
num2 = number[1]
sum = int(num1) + int(num2)
print(sum)

# To calculate the BMI

weight = int(input("Enter the weight"))
height = int(input("Enter the height"))
calculate_bmi = weight / (height * height)
print("The body mass index of the person is " +str(calculate_bmi))

# To check even or odd

number = int(input("Enter a number"))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

