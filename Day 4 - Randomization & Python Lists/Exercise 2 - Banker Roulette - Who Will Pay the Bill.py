import random

# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above 

#Write your code below this line)
list_length = len(names)
number = random.randint(0,list_length - 1)

if list_length < number:
    payer = names[number]
    print(f'{payer} is going to buy the meal today!')

else:
    payer = names[number]
    print(f'{payer} is going to buy the meal today!')