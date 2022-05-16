# Don't change the code below 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

#Write your code below this line 
acc_pizza = 0

if size == 'S':
    acc_pizza += 15
    if add_pepperoni == 'Y':
        acc_pizza += 2
        if extra_cheese == 'Y':
            acc_pizza += 1
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            acc_pizza += 1

elif size == 'M':
    acc_pizza += 20
    if add_pepperoni == 'Y':
        acc_pizza += 3
        if extra_cheese == 'Y':
            acc_pizza += 1
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            acc_pizza += 1

elif size == 'L':
    acc_pizza += 25
    if add_pepperoni == 'Y':
        acc_pizza += 3
        if extra_cheese == 'Y':
            acc_pizza += 1
    elif add_pepperoni == 'N':
        if extra_cheese == 'Y':
            acc_pizza += 1

print(f'Your final bill is: ${acc_pizza}.')