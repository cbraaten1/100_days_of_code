# Don't change the code below 
age = input("What is your current age?")
# Don't change the code above 

#Write your code below this line 
days = (90 * 365) - (365 * int(age))

weeks = (90 * 52) - (52 * int(age))

months = (90 * 12) - (12 * int(age))

print(f'You have {days} days, {weeks} weeks, and {months} months left.')