ages = [int(age) for age in input('enter all family members\' ages seperated by spaces').split(' ')]
cost = sum([age > 12 for age in ages]) * 15 + sum([age <= 12 and age >= 3 for age in ages]) * 10
print(f'the total price is {cost}$')
