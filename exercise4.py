# Write a program to find out how many days, weeks, months we have left to live until 90 years old

current_age = int(input("Enter you age"))
years_left = (90 - current_age)
days_left = ((90 - current_age ) * 365)
weeks_left = ((90 - current_age ) * 52)
months_left = ((90 - current_age ) * 12)
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months and {years_left} years left")