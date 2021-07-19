toppings = set()
while True:
    topping = input('enter a topping: ')
    if topping == 'quit':
        break
    else:
        toppings.add(topping)
        print(f'adding {topping} to pizza...')
print('the toppings are: ', end = '')
for topping in list(toppings):
    print(f'{topping}', end=', ')
print(f'\nprice: {10 + len(toppings) * 2.5}')
